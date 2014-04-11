# -*- coding: utf-8 -*- 
import traceback
import Queue
import logging
import threading
import telnetlib
import ConfigParser

COMMAND = 'aaa.bat'  

logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename='client.log',
    filemode='a')
'''Telnet远程登录：Windows客户端连接Linux服务器'''
  
# 配置选项
#Host = '192.168.1.105' # Telnet服务器IP
#username = 'test'   # 登录用户名
#Host = '192.2.4.31' # Telnet服务器IP
#username = 'eason'   # 登录用户名
#password = '123456'  # 登录密码


def fetchAll(**kwargs):
    print kwargs
    cf = ConfigParser.ConfigParser()
    cf.read('client.ini')
    result_queue = Queue.Queue()

    try:
        if not kwargs.has_key('hosts'):
            kwargs['hosts'] = cf.get('Client', 'host').split(',')
        if not kwargs.has_key('username'):
            kwargs['username'] = cf.get('Client', 'username')
        if not kwargs.has_key('password'):
            kwargs['password'] = cf.get('Client', 'password')
    except Exception as e:
        error_log = 'Get Host and Directions FAIL!Please Check the client.ini format!'
        logging.error(error_log)
        logging.error(traceback.format_exc())
        return 1, error_log
    
    threads = [threading.Thread(target=fetchOne,kwargs={'host':item,\
      'username':kwargs['username'],'password':kwargs['password'],'result':result_queue}) for item in kwargs['hosts']]
    for t in threads:
        t.start()
    
    for t in threads:
        t.join()

    status = 0
    error_res = '' 
    while not result_queue.empty():
        result = result_queue.get()
        if result['status']:
            error_res = error_res + 'Fetch File From Server:%s Failed!\n' %(result['host']) 
            status =1    

    if not status:
        return 0, 'Fetch Task Execute Success!'
    else:
        return 1, 'Fetch Task Execute FAILED!Because:\n' + error_res + 'Check the client.log for detail info!' 

def fetchOne(**kwargs):
    # 连接Telnet服务器
    HOST = kwargs['host']
    try:
        tn = telnetlib.Telnet(HOST)
        tn.set_debuglevel(3)
        # 输入登录用户名
        tn.read_until('login: ')
        tn.write(kwargs['username'].encode('ascii') + '\r')
        # 输入登录密码
        tn.read_until('password: ')
        tn.write(kwargs['password'].encode('ascii') + '\r')
 
        # 登录完毕后，执行ls命令
        tn.expect([b">"])
        tn.write(COMMAND + '\n\r')
 
        #命令执行完毕后，终止Telnet连接（或输入exit退出）
        tn.close() # tn.write('exit\n')
        received_log = 'Received File From Server:"%s" SUCCESS!' %(HOST)
        logging.debug(received_log)
        kwargs['result'].put({
            'status':0,
            'host':HOST
        })
    except Exception as e:
        error_log = 'Receive File From Server:"%s" FAILED, Please check the client.log file for detail!' %(HOST)
        logging.error(error_log)
        logging.error(traceback.format_exc())
        kwargs['result'].put({
            'status':1,
            'host':HOST
        })
        
