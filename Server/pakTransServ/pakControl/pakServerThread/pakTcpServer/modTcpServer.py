# -*- coding: utf-8 -*-
'''
TCP-сервер ожидает подключения клиентов.
После чего раскидывает их по своим сокетам.

Все сообщения -- сигналами, т. к. этот товарищ
пилит не в потоке, где определяется, а в своём!!!
'''

import socketserver

class clsTcpServer(socketserver.TCPServer):
    def __init__(self, root):
        print('        clsTcpServer.__init__()')
        self.__root = root
        self.adress = ''
        self.port = 37523
        self.listening = False
        super(socketserver.TCPServer,  self)
    
    def run(self):
        print('        clsTcpServer.listen()')
        #port = 53352
        #TODO: надо думать как красиво сделать обработку запросов.
        self.listening = True
        self.server_address = ('', 38572)
        #self.serve_forever()
        conn,  adr = self.get_request()
        self.close()
        self.listening=False
        print('{conn}, {adr}'.format(conn,  adr))
    
    def service_actions(self):
        print('clsTcpServer.listen()')
        #self.serve_forever()
    
    def stop(self):
        print('        clsTcpServer.close()')
        self.close()
