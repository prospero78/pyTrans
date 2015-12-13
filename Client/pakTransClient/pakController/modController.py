# -*- coding: utf-8 -*-
'''
Обеспечивает логику работы всей программы.
'''
import sys

from .pakTcpClient.modTcpClient import clsTcpClient

class clsController:
    def __init__(self, root):
        self.__root = root
        self.tcpClient = clsTcpClient(root)
        self.__cmd = {'show_winConnect':self.__show_winConnect, 
                      'connect':self.__connect, 
                      'exit_app':self.__exit_app}
    
    def __show_winConnect(self):
        print('show_winConnect')
        w = self.__root.Gui.winConnect
        w.cmd = self.__cmd
        w.show()
    
    def __connect(self):
        print('clsControl.__connect()')
        port = self.__root.Gui.winConnect.entPort.text()
        ip = self.__root.Gui.winConnect.entIP.text()
        self.tcpClient.connect(ip,  port)
        
    def run(self):
        self.__root.Gui.winMain.cmd = self.__cmd
        self.__root.exec_()
    
    def __exit_app(self):
        sys.exit()
