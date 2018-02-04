# -*- coding: UTF-8 -*-
"""
Created on 2017年12月27日
@author: Leo

暂时还没能使用,用来测试用
"""

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接服务器
ssh.connect(hostname='', port=22, username='', password='')
# 执行命令
stdin, stdout, stderr = ssh.exec_command('jps')
# 获取命令结果
result = stdout.read().decode("UTF-8").rstrip().split("\n")
print(result)
# 关闭连接
ssh.close()