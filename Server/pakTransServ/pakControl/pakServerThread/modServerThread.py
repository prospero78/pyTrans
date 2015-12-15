# -*- coding: utf-8 -*-
'''
В этом потоке сервер создаёт один поток. Он принимает запрос на 
стандартный порт сервера HTTP .
После чего работает с дескриптором клиента.
'''

from PySide import QtCore
from .pakHttpRequest.modHttpRequest import clsHttpRequest
from http.server import HTTPServer as clsHttpServer

class clsServerThread(QtCore.QThread):
    def __init__(self, root):
        print('      clsServerThread.__init__()')
        self.__root = root
        self.running = False
        super(clsServerThread, self).__init__()
        
    def run(self):
        print('      clsServerThread.serve_forever()')
        self.__srv = clsHttpServer(('', 80),  clsHttpRequest)
        self.__srv.serve_forever()
