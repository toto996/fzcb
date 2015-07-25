# -*- coding: utf-8 -*-

import urllib
import traceback
import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('123.57.147.89', 7080))
    # s.connect(('127.0.0.1', 80))
    # data = s.recv(1024)
    # print(data)
    # f = urllib.urlopen("http://www.baidu.com")
    #f = urllib.urlopen("http://123.57.147.89:80")
    #s = f.read()
    #print(s)
except Exception, exp:
    print(traceback.format_exc())