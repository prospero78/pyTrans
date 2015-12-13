# -*- coding: utf-8 -*-
'''
Модуль предоставляет выбор для подключения к серверу.
'''


from PySide import QtGui,  QtCore
from .resWinConnect import Ui_Dialog

class clsWinConnect(QtGui.QDialog, Ui_Dialog):
    def __init__(self, root):
        print('clsWinConnect.__init__()')
        self.__root = root
        self.__ip = None
        self.__port = None
        self.cmd = None
        super(clsWinConnect, self).__init__()
        self.setupUi(self)
        self.connect(self.btnConnect, QtCore.SIGNAL('clicked()'), self.__connect)
        self.hide()
    
    def __connect(self):
        self.hide()
        self.__ip = self.entIP.text()
        self.__port = self.entPort.text()
        self.cmd['connect']()
    
    @property
    def ip(self):
        return self.__ip
    
    @property
    def port(self):
        return self.__port
        
