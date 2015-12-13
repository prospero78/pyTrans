# -*- coding: utf-8 -*-
'''
Объединяет в себе все окна.
'''

from .pakWinMain.modWinMain import clsWinMain
from .pakWinConnect.modWinConnect import clsWinConnect

class clsGui:
    def __init__(self, root):
        print('  clsGui.__init()')
        self.__root = root
        self.winMain = clsWinMain(root)
        self.winConnect = clsWinConnect(root)
        self.cmd=None
    