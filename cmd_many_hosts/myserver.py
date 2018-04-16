#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author = "susu"
import  paramiko,getpass,os,sys,getpass
base_dir=os.path.dirname(os.path.abspath(__file__))
sys.path.append(base_dir)
print(base_dir)
# _password = getpass.getpass("密码:").strip()

_password=input("密码:")
#读取IP
def get_hosts():
    with open(base_dir+"/hosts",'rb') as f:
        my_hosts=eval(f.read())
        return  my_hosts
#Linux操作 
def run(my_hosts,_password,cmd):
	with open(base_dir+"/host_info.txt",'w',encoding="utf8") as f:
		for i in my_hosts:
			ssh = paramiko.SSHClient()
			ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			ssh.connect(hostname=i, port=22, username='root', password=_password)
			stdin, stdout, stderr = ssh.exec_command(cmd)
			result = stdout.read()
			ssh.close()
			f.write("===================={}====================\n".format(my_hosts[i]))
			f.write("IP地址:{}\n".format(i))
			f.write(stderr.read().decode())
			f.write(result.decode())
cmd=input("[linux]#").strip()
run(get_hosts(),_password,cmd)