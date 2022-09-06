"""

账号实名认证信息比对 认证接口 post请求需要带上token
"""
import hashlib
import time

key_sort = ["appid", "cmd", "nonce", "timestamp"]
print(sorted(key_sort))
cmd = "userCertIdCheck"
appid = "hpe1509d50d0f04225"
timestamp = str(int(time.time()))
timestamp = "1660706509"
nonce = "321654"
secret = "a2317304e113999f"
raw_sig = "http://9.140.129.65/cgi-bin/Hope.fcgi?" + "appid=" + appid + "&cmd=" + cmd + "&nonce=" + nonce + "&timestamp=" + timestamp + secret

print(raw_sig)
md5_coder = hashlib.md5()
md5_coder.update(raw_sig.encode(encoding="utf-8"))
sig = md5_coder.hexdigest()
print(sig.lower())
raw_sig = "http://9.140.129.65/cgi-bin/Hope.fcgi?" + "appid=" + appid + "&cmd=" + cmd + "&nonce=" + nonce + "&timestamp=" + timestamp + "&sign=" + sig
print(raw_sig)
# 测试
"command=CmdL5&type=getip&cmdid=393216&modid=64455041"
"ip=9.140.129.65&port=80"



