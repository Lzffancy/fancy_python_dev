import requests


def SaveOpenidInfoOnce():
    firstCallFlag = 0
    next_openid = ""
    url_begin = "https://api.weixin.qq.com/cgi-bin/user/get?access_token=" + "&next_openid=" + next_openid
    if firstCallFlag == 0:
        data = requests.get(url_begin)
        next_openid = handle_data(data)

        while next_openid:  # 如果handle_data(data)返回了next_openid则继续执行，为空则退出while循环
            data = requests.get(next_openid)
            next_openid = handle_data(data)


def handle_data(data):
    # 拼接sql 处理数据  返回下一个next_openid
    data = {}
    next_openid = ""
    return next_openid


if __name__ == '__main__':
    flag = 1
    while flag:
        print(flag)
        flag = 1
