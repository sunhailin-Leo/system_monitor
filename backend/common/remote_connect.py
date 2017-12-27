# -*- coding: UTF-8 -*-
"""
Created on 2017年12月27日
@author: Leo
"""

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接服务器
ssh.connect(hostname='120.77.153.78', port=22, username='root', password='Moliny@1996')
# 执行命令
stdin, stdout, stderr = ssh.exec_command('jps')
# 获取命令结果
result = stdout.read().decode("UTF-8").rstrip().split("\n")
print(result)
# 关闭连接
ssh.close()