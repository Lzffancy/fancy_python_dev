import json
import os

path = "/user/lzf/data/data.csv"

from socket import socket, AF_INET, SOCK_STREAM


def echo_client(client_sock, addr):
    print('Got connection from', addr)
    # Make text-mode file wrappers for socket reading/writing
    client_in = open(client_sock.fileno(), 'rt', encoding='latin-1',
                     closefd=False)
    client_out = open(client_sock.fileno(), 'wt', encoding='latin-1',
                      closefd=False)

    # Echo lines back to the client using file I/O
    for line in client_in:
        client_out.write(line)
        client_out.flush()
    client_sock.close()


def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    while True:
        client, addr = sock.accept()
        echo_client(client, addr)


s = '{"name": "ACME", "shares": 50, "price": 490.1}'


class JSONObject:
    def __init__(self, d):
        print(d)
        # 直接将魔法属性__dict__赋予整个字典,python将其处理为实例属性
        self.__dict__ = d


data = json.loads(s, object_hook=JSONObject)
print(data.name)
print(data.__dict__)


def serialize_instance(obj):
    d = {'__classname__': type(obj).__name__}
    print("-"*50)
    print(vars(obj)) #通过vars()获取
    d.update(vars(obj))
    return d


print(serialize_instance(data))
