# -*- coding: utf-8 -*-
'''
Предоставляет всю графику для сервера.
'''

from .pakWinMain.modWinMain import clsWinMain

class clsGui:
    def __init__(self, root):
        print('  clsGui.__init__()')
        self.__root = root
        self.winMain = clsWinMain(root)
    
    def run(self):
        self.winMain.show()