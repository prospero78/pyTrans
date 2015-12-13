# -*- coding: utf-8 -*-
'''
Класс главного окна сервера.
Позволяет просматривать всякую статистику и настройки.
'''

from PySide import QtGui, QtCore
from .resWinMain import Ui_MainWindow as clsUiWinMain

class clsWinMain(QtGui.QMainWindow, clsUiWinMain):
    def __init__(self, root):
        print('    clsWinMain.__init__()')
        self.__root = root
        self.cmd = {}
        super(clsWinMain, self).__init__()
        self.setupUi(self)
        self.connect(self.btnRunServer, QtCore.SIGNAL('clicked()'), self.server_start)
        self.connect(self.btnStopServer, QtCore.SIGNAL('clicked()'), self.server_stop)
        self.show()
    
    def server_start(self):
        print('server_start')
        self.btnRunServer.setDisabled(True)
        self.btnStopServer.setEnabled(True)
        self.cmd['server_start'](int(self.entPort.text()))
    
    def server_stop(self):
        print('server_stop')
        self.btnRunServer.setEnabled(True)
        self.btnStopServer.setDisabled(True)
        self.cmd['server_stop']()