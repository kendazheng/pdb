#coding=utf-8
import threading, logging, traceback, subprocess
from SocketServer import BaseRequestHandler, TCPServer, ThreadingMixIn

logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename='server.log',
    filemode='a')

class MyHandler(BaseRequestHandler):
    
    def handle(self):
        self.data = ''
        c_thread = threading.current_thread()
        handler_info = "{0} hanlde request from {1}".format(c_thread.name, self.client_address[0])
        logging.debug(handler_info) 
        res = 'Server has received success!'
        '''
        excute bat script here and read the file content to send
        '''
        p = subprocess.Popen("aa.bat",stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
        echo_name = p.stdout.readlines()[-1].strip()
        fp = open(echo_name,'r')
        file_content = fp.read()
        file_name = echo_name.rjust(50)
        file_length = str(len(file_content)).rjust(8)
        data = file_name + file_length + file_content
        self.request.sendall(data)

class ThreadTCPServer(ThreadingMixIn, TCPServer):
    pass
 
if __name__ == '__main__':
    HOST, PORT = "127.0.0.1", 12345
    print "file server is listening %s:%s" %(HOST, PORT)
    server = ThreadTCPServer((HOST, PORT), MyHandler)
    server.serve_forever()
