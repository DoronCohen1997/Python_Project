# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1104, 848)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(930, 720, 141, 28))
        self.pushButton.setObjectName("pushButton")
        self.btn_test = QtWidgets.QPushButton(self.centralwidget)
        self.btn_test.setGeometry(QtCore.QRect(110, 80, 161, 41))
        self.btn_test.setObjectName("btn_test")
        self.btn_run = QtWidgets.QPushButton(self.centralwidget)
        self.btn_run.setGeometry(QtCore.QRect(300, 80, 171, 41))
        self.btn_run.setObjectName("btn_run")
        self.btn_stop = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stop.setGeometry(QtCore.QRect(500, 80, 161, 41))
        self.btn_stop.setObjectName("btn_stop")
        self.btn_logs = QtWidgets.QPushButton(self.centralwidget)
        self.btn_logs.setGeometry(QtCore.QRect(710, 80, 161, 41))
        self.btn_logs.setObjectName("btn_logs")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(410, 140, 451, 561))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.testslist = QtWidgets.QTreeWidget(self.centralwidget)
        self.testslist.setGeometry(QtCore.QRect(110, 140, 256, 561))
        self.testslist.setObjectName("testslist")
        self.testslist.headerItem().setText(0, "1")
        self.rmv_all_btn = QtWidgets.QPushButton(self.centralwidget)
        self.rmv_all_btn.setGeometry(QtCore.QRect(250, 730, 93, 71))
        self.rmv_all_btn.setObjectName("rmv_all_btn")
        self.slc_all_btn = QtWidgets.QPushButton(self.centralwidget)
        self.slc_all_btn.setGeometry(QtCore.QRect(110, 730, 93, 71))
        self.slc_all_btn.setObjectName("slc_all_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1104, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "\"Click me\""))
        self.btn_test.setText(_translate("MainWindow", "Tests"))
        self.btn_run.setText(_translate("MainWindow", "Run"))
        self.btn_stop.setText(_translate("MainWindow", "Stop"))
        self.btn_logs.setText(_translate("MainWindow", "Logs"))
        self.rmv_all_btn.setText(_translate("MainWindow", "Remove All"))
        self.slc_all_btn.setText(_translate("MainWindow", "Select All"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
