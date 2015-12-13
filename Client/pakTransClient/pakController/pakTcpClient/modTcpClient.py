# -*- coding: utf8 -*-
"""
Модуль предоставляет класс для TCP-подключения к серверу.
"""

class clsTcpClient:
    def __init__(self,  root):
        print('   clsTcpClient.__init__()')
        self.__root = root
        
    def connect(selfself,  ip,  port):
        print('  clsTcpClient.connect()',  ip,  port)
