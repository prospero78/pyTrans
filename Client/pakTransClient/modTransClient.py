# -*- coding: utf-8 -*-
'''
Главный класс клиента.
'''
import sys
from PySide import QtGui
from .pakGui.modGui import clsGui
from .pakController.modController import clsController

class clsTransClient(QtGui.QApplication):
    def __init__(self):
        print('clsTransClient.__init__()')
        super(clsTransClient, self).__init__(sys.argv)
        self.Controller = clsController(self)
        self.Gui = clsGui(self)
        
    def run(self):
        print('clsTransClient.run()')
        self.Controller.run()
        