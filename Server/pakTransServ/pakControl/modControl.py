# -*- coding: utf-8 -*-
'''
Контроллер сервера.
Вся динамика здесь.
'''

#from PySide import QtCore
from .pakServerThread.modServerThread import clsServerThread

class clsControl:
    def __init__(self, root):
        print('  clsControl.__init__()')
        self.__root = root
        self.__ServThread = clsServerThread(root = root)
        self.cmd={
            'server_start':self.__server_start,
            'server_stop':self.__server_stop,}
        root.Gui.winMain.cmd = self.cmd
        
    def __server_start(self, port):
        print('  clsControl.__server_start()', port)
        self.__ServThread.running = True
        self.__ServThread.start()
    
    def __server_stop(self):
        print('  clsControl.__server_stop()')
        self.__ServThread.running = False
