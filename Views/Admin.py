# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admin.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSizeGrip
import sys
import database

class Ui_AdminWindow(QtWidgets.QDialog):
    def setupUi(self, AdminWindow):
        AdminWindow.setObjectName("AdminWindow")
        AdminWindow.resize(480, 320)

        AdminWindow.setFixedSize(480,320)
        AdminWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.centralwidget = QtWidgets.QWidget(AdminWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lstEmployees = QtWidgets.QListView(self.centralwidget)
        self.lstEmployees.setGeometry(QtCore.QRect(0, 40, 471, 221))
        self.lstEmployees.setObjectName("lstEmployees")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnCancel = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancel.setGeometry(QtCore.QRect(0, 262, 471, 31))
        self.btnCancel.setObjectName("btnCancel")
        AdminWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AdminWindow)
        self.statusbar.setObjectName("statusbar")
        AdminWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AdminWindow)
        QtCore.QMetaObject.connectSlotsByName(AdminWindow)

    def retranslateUi(self, AdminWindow):
        _translate = QtCore.QCoreApplication.translate
        AdminWindow.setWindowTitle(_translate("AdminWindow", "AdminWindow"))
        self.label.setText(_translate("AdminWindow", "Select Employee to Register:"))
        self.btnCancel.setText(_translate("AdminWindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminWindow = QtWidgets.QMainWindow()
    ui = Ui_AdminWindow()
    ui.setupUi(AdminWindow)
    AdminWindow.show()
    sys.exit(app.exec_())
