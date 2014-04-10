# -*- coding: utf-8 -*- 
 
import telnetlib
  
'''Telnet远程登录：Windows客户端连接Linux服务器'''
  
# 配置选项
Host = '192.168.1.105' # Telnet服务器IP
username = 'test'   # 登录用户名
password = '123456'  # 登录密码
finish = ':~$ '      # 命令提示符（标识着上一条命令已执行完毕）

# 连接Telnet服务器
tn = telnetlib.Telnet(Host)
 
# 输入登录用户名
tn.read_until('login: ')
a = tn.write(username + '\n\r')
print 'after login' 
# 输入登录密码
tn.read_until('password: ')
a = tn.write(password + '\n\r')
print 'after Password' 
 
# 登录完毕后，执行ls命令
tn.read_until('\>')
print 'after >'
tn.write('dir'+'\n\r')
 
print 'after dir' 
# ls命令执行完毕后，终止Telnet连接（或输入exit退出）
tn.read_until(finish)
tn.close() # tn.write('exit\n')
