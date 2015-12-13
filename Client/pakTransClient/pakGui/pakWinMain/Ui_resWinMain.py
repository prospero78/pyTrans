# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Ya.dsk\Личное\01_python\project_3\2015\pyTrans\Client\pakTransClient\pakGui\pakWinMain\resWinMain.ui'
#
# Created: Sun Dec 13 10:39:05 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(458, 281)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 458, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.mnuConnect = QtGui.QAction(MainWindow)
        self.mnuConnect.setObjectName("mnuConnect")
        self.action_2 = QtGui.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.mnuExit = QtGui.QAction(MainWindow)
        self.mnuExit.setObjectName("mnuExit")
        self.menu.addAction(self.mnuConnect)
        self.menu.addAction(self.action_2)
        self.menu.addSeparator()
        self.menu.addAction(self.mnuExit)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "pyTransClient", None, QtGui.QApplication.UnicodeUTF8))
        self.menu.setTitle(QtGui.QApplication.translate("MainWindow", "Сервер", None, QtGui.QApplication.UnicodeUTF8))
        self.mnuConnect.setText(QtGui.QApplication.translate("MainWindow", "Подключиться", None, QtGui.QApplication.UnicodeUTF8))
        self.action_2.setText(QtGui.QApplication.translate("MainWindow", "Отключиться", None, QtGui.QApplication.UnicodeUTF8))
        self.mnuExit.setText(QtGui.QApplication.translate("MainWindow", "Выход", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

