# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainWindow1.ui'
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
        self.btn_test.setStyleSheet("background-color: rgb(170, 0, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.btn_test.setObjectName("btn_test")
        self.btn_run = QtWidgets.QPushButton(self.centralwidget)
        self.btn_run.setGeometry(QtCore.QRect(300, 80, 171, 41))
        self.btn_run.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 0);")
        self.btn_run.setObjectName("btn_run")
        self.btn_stop = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stop.setGeometry(QtCore.QRect(500, 80, 161, 41))
        self.btn_stop.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.btn_stop.setObjectName("btn_stop")
        self.btn_logs = QtWidgets.QPushButton(self.centralwidget)
        self.btn_logs.setGeometry(QtCore.QRect(710, 80, 161, 41))
        self.btn_logs.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.btn_logs.setObjectName("btn_logs")
        self.testslist = QtWidgets.QTreeWidget(self.centralwidget)
        self.testslist.setGeometry(QtCore.QRect(110, 140, 256, 561))
        self.testslist.setObjectName("testslist")
        self.testslist.headerItem().setText(0, "1")
        self.rmv_all_btn = QtWidgets.QPushButton(self.centralwidget)
        self.rmv_all_btn.setGeometry(QtCore.QRect(250, 730, 93, 71))
        self.rmv_all_btn.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 85, 255);")
        self.rmv_all_btn.setObjectName("rmv_all_btn")
        self.slc_all_btn = QtWidgets.QPushButton(self.centralwidget)
        self.slc_all_btn.setGeometry(QtCore.QRect(110, 730, 93, 71))
        self.slc_all_btn.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 85, 0);")
        self.slc_all_btn.setObjectName("slc_all_btn")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(493, 146, 381, 551))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 30, 511, 31))
        self.label.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
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
        self.btn_test.setText(_translate("MainWindow", "Choose Tests"))
        self.btn_run.setText(_translate("MainWindow", "Run"))
        self.btn_stop.setText(_translate("MainWindow", "Stop"))
        self.btn_logs.setText(_translate("MainWindow", "Logs"))
        self.rmv_all_btn.setText(_translate("MainWindow", "Remove All"))
        self.slc_all_btn.setText(_translate("MainWindow", "Select All"))
        self.label.setText(_translate("MainWindow", "Automation for Tests"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
