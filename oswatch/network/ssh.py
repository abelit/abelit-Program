#!/usr/bin/python 
import paramiko 
hostname="172.28.1.221"
port=22
username="root"
password="passw0rd"
def sshremote():
    s=paramiko.SSHClient() 
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
    s.connect(hostname,port,username,password) 
    stdin,stdout,sterr=s.exec_command("alias") 
    print(stdout.read())
    s.close()

# import subprocess
# # 本机
# # p = subprocess.Popen('uptime', stdout=subprocess.PIPE)   
# # 远程服务器，需要配置youserver.com自动登录（通过密钥文件自动登录）
# p = subprocess.Popen(['ssh', 'root@172.28.1.221', 'uptime'], stdout=subprocess.PIPE)
# info = p.stdout.readline()
# print(info)
