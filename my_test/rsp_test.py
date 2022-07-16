import json
import os
import urllib
import requests


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


def make_url_rpa_name_map(report_result):
    # 从返回信息中提取cvs的url
    url_rpa_name_map = {}
    for data in report_result.get("data"):
        url_rpa_name_map[data.get("url")] = data.get("rpaName")
    print(url_rpa_name_map)
    return url_rpa_name_map


def download_file(url_rpa_name_map):
    for url, rap_name in url_rpa_name_map.items():
        # todo 可以使用re模块使得解析更加准确
        path = './' + rap_name
        # 先创建文件夹
        if not os.path.exists(path):
            os.mkdir(path)
        url = urllib.parse.unquote(url)
        work_book_sheet_position = url.split("/")[6].split("?")[0]
        with open(path + "/" + work_book_sheet_position, "wb") as file:
            file.write(requests.get(url).content)


if __name__ == '__main__':
    # 链接参数配置
    config = Config()
    config.set_config(env="pro")
    config.token = "fe3525ff-c17c-4a95-b979-d0c173e200b3"
    # 初始化请求结构参数
    report_infos = ReportInfos()
    # 分页默认一页10条

    for page in range(0, 10):
        report_infos.page = page
        report_infos.limit = 500
        report_infos.rpaIdList = []
        # report_infos.startTime = "2021-07-20 00:00:00"
        # report_infos.endTime = "2021-07-25 00:00:00"
        param = report_infos.get_param_body()
        # 请求报表信息
        report_result = report_infos.query_report_list(param)
        print(report_result)
        # print(report_result)
        # 解析报表的url
        url_list = make_url_rpa_name_map(report_result)
        download_file(url_list)
