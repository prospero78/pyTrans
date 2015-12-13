# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Ya.dsk\Личное\01_python\project_3\2015\pyTrans\Server\pakTransServ\pakGui\pakWinMain\resWinMain.ui'
#
# Created: Sun Dec 13 10:35:00 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))
        MainWindow.setMaximumSize(QtCore.QSize(600, 400))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 211, 61))
        self.groupBox.setObjectName("groupBox")
        self.entPort = QtGui.QLineEdit(self.groupBox)
        self.entPort.setGeometry(QtCore.QRect(90, 20, 113, 20))
        self.entPort.setObjectName("entPort")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 23, 51, 20))
        self.label.setObjectName("label")
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 80, 211, 61))
        self.groupBox_2.setObjectName("groupBox_2")
        self.btnRunServer = QtGui.QPushButton(self.groupBox_2)
        self.btnRunServer.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.btnRunServer.setObjectName("btnRunServer")
        self.btnStopServer = QtGui.QPushButton(self.groupBox_2)
        self.btnStopServer.setEnabled(False)
        self.btnStopServer.setGeometry(QtCore.QRect(110, 20, 75, 23))
        self.btnStopServer.setObjectName("btnStopServer")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "pyTransServ", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Сетевые настройки", None, QtGui.QApplication.UnicodeUTF8))
        self.entPort.setText(QtGui.QApplication.translate("MainWindow", "38752", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Порт:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Управление сервером", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRunServer.setText(QtGui.QApplication.translate("MainWindow", "Запуск", None, QtGui.QApplication.UnicodeUTF8))
        self.btnStopServer.setText(QtGui.QApplication.translate("MainWindow", "Остановка", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

