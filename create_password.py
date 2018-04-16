#!-*-coding:utf-8-*-
import string
import random
import os
webname=input("请输入网站名字：")
web_ip=input("IP地址：")
sqlname=webname.replace('.','_')
a=string.ascii_lowercase+string.ascii_lowercase.upper()+'0123456789'
sql_password='yestar'+"".join(random.sample(a,14))
ftp_password='yestar'+"".join(random.sample(a,14))
with open("密码.txt",'w') as f:
    f.write("网站：{}\n".format(webname))
    f.write("数据库：{}\n".format(sqlname))
    f.write("用户:{}\n".format(sqlname))
    f.write("密码:{}\n".format(sql_password))
    f.write("ftp://{}:{}@{}".format(webname,ftp_password,web_ip))
os.system('pause')