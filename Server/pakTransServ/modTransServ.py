# -*- coding: utf-8 -*-
'''
Главный класс сервера.
'''

import sys
from PySide import QtGui
from .pakGui.modGui import clsGui
from .pakControl.modControl import clsControl

class clsTransServ(QtGui.QApplication):
    def __init__(self):
        print('clsTransServ.__init__()')
        super(clsTransServ, self).__init__(sys.argv)
        self.Gui = clsGui(self)
        self.Control = clsControl(self)
        self.setStyle('Windows')
    
    def run(self):
        print('clsTransServ.run()')
        self.Gui.run()
        self.exec_()
        
