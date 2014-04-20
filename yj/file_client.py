#!/usr/bin/env python
import socket
import string
import sys
import logging
import traceback
import os
import threading
import Queue
import ConfigParser 

logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename='client.log',
    filemode='a')

result_queue = Queue.Queue()

def fetchAll(**kwargs):
    cf = ConfigParser.ConfigParser()
    cf.read('client.ini')
    
    try:
        if not kwargs.has_key('hosts'):
            kwargs['hosts'] = cf.get('Client', 'host').split(',')
        if not kwargs.has_key('dirs'):
            kwargs['dirs'] = cf.get('Client', 'dirs').split(',')
    except Exception as e:
        error_log = 'Get Host and Directions FAIL!Please Check the client.ini format!'
        logging.error(error_log)
        logging.error(traceback.format_exc())
        return 1, error_log
    
    for item in kwargs['dirs']:
        if not os.path.isdir(item):
            error_log = '"%s" is not an available director!' % item
            logging.error(error_log)
            return 1, error_log   
    
    threads = [threading.Thread(target=fetchOne,kwargs={'host':item,'dirs':kwargs['dirs'],'result':result_queue})
                  for item in kwargs['hosts']]
    for t in threads:
        t.start()
    
    #wait for child threads complete
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
    print kwargs
    if 1:
        HOST, PORT = kwargs['host'], 12345
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        try:
            sock.connect((HOST,PORT))
            file_name = sock.recv(50).strip()
            file_length = string.atoi(sock.recv(8).strip())
            file_content = sock.recv(file_length).strip()
            received_log = 'Received "%s" From Server:"%s" SUCCESS, File Length is %s' %(file_name, HOST, file_length)
            print received_log
            logging.debug(received_log)
            for item in kwargs['dirs']:
                fp = open(os.path.join(item, file_name),'w')
                fp.write(file_content)
                saved_log = 'Saved the file into "%s" direction as "%s" SUCCESS!' %(item, file_name)
                print saved_log
                logging.debug(saved_log)
            
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
        finally:
            sock.close()
