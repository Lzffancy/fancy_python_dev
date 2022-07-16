import csv
import json
import requests
import urllib


class Config(object):
    def __init__(self):
        self.host = None
        self.token = None

    def set_config(self, env):
        if not env:
            return {"ret": 10001, "msg": u"参数不能为空"}
        if env == "sim":
            self.host = "https://rpa-server-pre.ziniao.com/erp_report/list"
        elif env == "pro":
            self.host = "https://rpa-server.ziniao.com/erp_report/list"


class ReportInfos(Config):
    def __init__(self):
        super(ReportInfos, self).__init__()
        self.page = 1
        self.limit = 10
        self.rpaIdList = []
        self.startTime = None
        self.endTime = None
        self.header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
                       "Content-Type": "application/json",
                       "token": config.token}
        self.host = config.host

    def get_param_body(self):
        param = {"page": self.page, "limit": self.limit}
        if self.rpaIdList:
            param["rpaIdList"] = self.rpaIdList
        if self.startTime:
            param["startTime"] = self.startTime
        if self.endTime:
            param["endTime"] = self.endTime

        print(param)
        return param

    def query_report_list(self, param):
        """
            获取数据库实例下的table名称
        :return:
        """
        try:
            json_data = json.dumps(param).encode(encoding='utf-8')
            res = requests.post(url=self.host, data=json_data, headers=self.header)
            if res.status_code not in range(200, 300):
                return {"ret": 10002, "msg": u"请求服务器失败"}
            response_data = json.loads(res.content)
            if response_data.get("code") != 0:
                return {"ret": 10002, "msg": response_data.get("msg", u"服务端代码异常")}
            data = response_data.get("data")
            return {"ret": 0, "msg": u"获取数据成功", "data": data.get("result"), "count": response_data.get("count")}
        except Exception as e:
            print(e)
            return {"ret": 10003, "msg": u"获取异常", "error_msg": e.message}


def make_download_url_list(report_result):
    # 从返回信息中提取cvs的url
    url_list = []
    for data in report_result.get("data"):
        url_list.append(data.get("url"))
    return url_list


def download_file(url_list):
    for url in url_list:
        # todo 可以使用re模块使得解析更加准确
        url = urllib.parse.unquote(url)
        is_csv = None
        work_book_sheet_position = url.split("/")[6].split("?")[0]
        if work_book_sheet_position[-3:] == "csv":
            is_csv = True
        else:
            is_csv = False
        print(work_book_sheet_position)

        # 请求下载
        content = requests.get(url).text.strip()
        rows = content.split("\n")

        # excl
        # todo csv 和 excel数据要整合到excel

        if is_csv:
            print("处理csv数据")
            # with open("data.csv", "a", newline='', encoding='utf-8-sig') as csv_file:
            #     writer = csv.writer(csv_file)
            #     row_i = 0
            print(rows)
            for row in rows:
                if row == "":
                    continue
                print("row", row)
                row_list = row.split(",")
                # row_list = list(eval(row))
                # print("row list",row_list)
                # row_list = list(row)
                print(row_list)
                # if row_i == 0:
                #     # 表头
                #     row_list.insert(0, "workbook-sheet-position")
                # else:
                #     row_list.insert(0, work_book_sheet_position)
                # # print(row_list)
                # writer.writerow(row_list)
                # row_i += 1


if __name__ == '__main__':
    # 链接参数配置
    config = Config()
    config.set_config(env="pro")
    config.token = "fe3525ff-c17c-4a95-b979-d0c173e200b3"
    # 初始化请求结构参数
    report_infos = ReportInfos()
    # 分页默认一页10条
    report_infos.page = 1
    report_infos.limit = 2
    report_infos.rpaIdList = []
    # report_infos.startTime = "2021-07-20 00:00:00"
    # report_infos.endTime = "2021-07-25 00:00:00"
    # report_infos.startTime = "2022-02-10 00:00:00"
    # report_infos.endTime = "2021-02-11 00:00:00"
    param = report_infos.get_param_body()
    # 请求报表信息
    report_result = report_infos.query_report_list(param)
    # print(report_result)
    # 解析报表的url
    url_list = make_download_url_list(report_result)
    download_file(url_list)
