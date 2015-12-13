# -*- coding: utf-8 -*-
'''
Главное окно всего приложения.
'''

from PySide import QtCore, QtGui
from .resWinMain import Ui_MainWindow as clsUiWinMain

class clsWinMain(QtGui.QMainWindow, clsUiWinMain):
    def __init__(self, root):
        print('    clsWinMain.__init__()')
        self.root = root
        self.cmd = None
        super(clsWinMain, self).__init__()
        self.setupUi(self)
        self.connect(self.mnuConnect, QtCore.SIGNAL('activated()'), self.__show_winConnect)
        self.connect(self.mnuExit,  QtCore.SIGNAL('activated()'), self.__exit)
        self.show()
    
    def __exit(self):
        self.hide()
        self.cmd['exit_app']()
    
    def __show_winConnect(self):
        self.cmd['show_winConnect']()
