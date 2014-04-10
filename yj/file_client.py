#!/usr/bin/env python
import socket
import sys
import logging
import traceback
import os

logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename='client.log',
    filemode='a')

HOST, PORT = '127.0.0.1', 12345
#data = ' '.join(sys.argv[1:])


def fetch(**kwargs):
    if kwargs.has_key('hosts'):
        print kwargs['hosts']
    if kwargs.has_key('dirs'):
        print kwargs['dirs']
    '''
    for item in dirs:
        if not os.path.isdir(item):
            error_log = '"%s" is not an available director!' % item
            error_mark = True
            print error_log
            logging.error(error_log)
    if not error_mark:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((HOST,PORT))
            file_name = sock.recv(50).strip()
            file_length = sock.recv(8).strip()
            file_content = sock.recv(1024).strip()
            print file_name
            print file_length
            print file_content
            received_log = 'Received "%s" From Server SUCCESS, File Length is %s' %(file_name, file_length)
            print received_log
            logging.debug(received_log)
            for item in dirs:
                fp = open(os.path.join(item, file_name),'w')
                fp.write(file_content)
                saved_log = 'Saved the file into "%s" direction as "%s" SUCCESS!' %(item, file_name)
                print saved_log
                logging.debug(saved_log)
        except Exception as e:
            print 'Receive "%s" From Server FAILED, Please check the client.log file for detail!' %(file_name)
            logging.error(traceback.format_exc())
        finally:
            sock.close()
    '''
