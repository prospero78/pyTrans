# -*- coding: utf-8 -*-
'''
TCP-сервер ожидает подключения клиентов.
После чего раскидывает их по своим сокетам.

Все сообщения -- сигналами, т. к. этот товарищ
пилит не в потоке, где определяется, а в своём!!!
'''

from PySide import QtCore, QtNetwork

class clsTcpServer(QtNetwork.QTcpServer):
    def __init__(self, root):
        print('        clsTcpServer.__init__()')
        self.__root = root
        self.adress = QtNetwork.QHostAddress()
        self.port = 0
        super(clsTcpServer, self).__init__()
        self.connect(self, 
                     QtCore.SIGNAL('run_tsp_server()'), 
                     self.__run_tsp_server)
        self.connect(self,  QtCore.SIGNAL('stop_tcp_server()'),  self.__stop)
    
    @QtCore.Slot()
    def __run_tsp_server(self):
        print('        clsTcpServer.listen()')
        res = self.listen(adress = self.adress, port = self.port)
    
    def __stop(self):
        print('        clsTcpServer.close()')
        self.close()
