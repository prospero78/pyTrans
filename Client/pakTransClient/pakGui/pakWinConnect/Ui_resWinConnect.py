# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Ya.dsk\Личное\01_python\project_3\2015\pyTrans\Client\pakTransClient\pakGui\pakWinConnect\resWinConnect.ui'
#
# Created: Tue Dec  8 21:42:22 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(318, 130)
        self.g1 = QtGui.QGroupBox(Dialog)
        self.g1.setGeometry(QtCore.QRect(10, 10, 301, 80))
        self.g1.setObjectName("g1")
        self.lblIP = QtGui.QLabel(self.g1)
        self.lblIP.setGeometry(QtCore.QRect(60, 20, 46, 13))
        self.lblIP.setObjectName("lblIP")
        self.entIP = QtGui.QLineEdit(self.g1)
        self.entIP.setGeometry(QtCore.QRect(120, 20, 113, 20))
        self.entIP.setObjectName("entIP")
        self.label = QtGui.QLabel(self.g1)
        self.label.setGeometry(QtCore.QRect(10, 50, 101, 16))
        self.label.setObjectName("label")
        self.entPort = QtGui.QLineEdit(self.g1)
        self.entPort.setGeometry(QtCore.QRect(120, 50, 113, 20))
        self.entPort.setObjectName("entPort")
        self.btnConnect = QtGui.QPushButton(Dialog)
        self.btnConnect.setGeometry(QtCore.QRect(10, 100, 101, 23))
        self.btnConnect.setObjectName("btnConnect")
        self.btnCancel = QtGui.QPushButton(Dialog)
        self.btnCancel.setGeometry(QtCore.QRect(200, 100, 101, 23))
        self.btnCancel.setObjectName("btnCancel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Подключение к серверу", None, QtGui.QApplication.UnicodeUTF8))
        self.g1.setTitle(QtGui.QApplication.translate("Dialog", "Параметры подключения", None, QtGui.QApplication.UnicodeUTF8))
        self.lblIP.setText(QtGui.QApplication.translate("Dialog", "Адрес IP", None, QtGui.QApplication.UnicodeUTF8))
        self.entIP.setText(QtGui.QApplication.translate("Dialog", "127.0.0.1", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Порт подключения", None, QtGui.QApplication.UnicodeUTF8))
        self.entPort.setText(QtGui.QApplication.translate("Dialog", "38752", None, QtGui.QApplication.UnicodeUTF8))
        self.btnConnect.setText(QtGui.QApplication.translate("Dialog", "Подключиться", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCancel.setText(QtGui.QApplication.translate("Dialog", "Отмена", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

