#coding=utf-8
import threading, logging, traceback
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
        file_name = 'file_name'.rjust(50)
        file_length = '8'.rjust(8)
        file_content = 'file_content'
        data = file_name + file_length + file_content
        self.request.sendall(data)

class ThreadTCPServer(ThreadingMixIn, TCPServer):
    pass
 
if __name__ == '__main__':
    HOST, PORT = "127.0.0.1", 12345

    server = ThreadTCPServer((HOST, PORT), MyHandler)
    server.serve_forever()
