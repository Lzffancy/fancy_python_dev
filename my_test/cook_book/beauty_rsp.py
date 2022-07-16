# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic:回参美化
Desc :urldecode --> urlparse --> json_loads --> pprint
"""
import json
import urllib.parse
import pprint


def beauty_rep(encode_rep):
    decode_rep = urllib.parse.unquote(encode_rep, encoding="utf-8", errors="replace")
    parse_url = urllib.parse.parse_qs(decode_rep, separator="&")
    print(parse_url)
    pprint.pprint(json.loads(parse_url["content"][0]))


def main():
    while 1:
        input_str = input("输入类型：1、urlencode-->json  2、&")

        if input_str == "1":
            input_str = input("输入:")
            beauty_rep(input_str)
        else:
            input_str = input("输入:")
            beauty_rep2(input_str)

def beauty_rep2(encode_rep):
    pprint.pprint(encode_rep.split("&"))

if __name__ == '__main__':
    main()

