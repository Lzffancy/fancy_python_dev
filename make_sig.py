import hashlib
import time
import requests

now_time = int(time.time())
print(now_time)
md5_coder = hashlib.md5()
# now_time=1643025827
row_sig = "CmdGetGameItemInfo_" + str(now_time) + "KF-SDK-0124200347-WUCz7O-69112_ofnImetIemaGteGdmC"
print(row_sig)
md5_coder.update(row_sig.encode(encoding="utf-8"))
sig = md5_coder.hexdigest().upper()
print(sig)


def send_get_req():
    make_req_url = 'http://9.138.64.30:8208/cgi-bin/CmdGetGameItemInfo?command=CmdGetGameItemInfo&item_type=13&item_id=10602&page_size=10&page_index=0&_getSize=1&skfSerial=KF-SDK-0124200347-WUCz7O-69112&skfTimestamp='+str(now_time)+'&skfSign=' + sig
    print(make_req_url)
    resp=requests.get(make_req_url).content

    print(resp)


if __name__ == '__main__':
    send_get_req()
