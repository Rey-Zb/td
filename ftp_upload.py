#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path
import datetime
from ftplib import FTP

host = 'x.x.x.x'
port = 21
username = 'xxx'
password = 'xxxxx'

ftp = FTP()
ftp.connect(host, port)
ftp.login(username, password)
print 'Login successful !'

base_dir = "E:\\test\\"
l = os.listdir(base_dir)

l.sort(key=lambda fn: os.path.getmtime(base_dir+fn) if not os.path.isdir(base_dir+fn) else 0)
d = datetime.datetime.fromtimestamp(os.path.getmtime(base_dir+l[-1]))
new_file = l[-1]

print 'The latest file is :', new_file


local_path = 'E:/test/' + new_file


fp = open(local_path, 'rb')

print 'start Uploading==========>'

bufsize = 1024
ftp.storbinary('STOR ' + new_file, fp, bufsize)


ftp.set_debuglevel(0)
fp.close()

print 'Uploading Fininshed=======>'

zb = raw_input("please anykey quit ~")
