import sys
import random
import os
import subprocess
import time
import threading
import shlex

from PyQt5.QtCore import QDate
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from subprocess import Popen
from subprocess import call
from asyncio.windows_utils import PIPE
from Naked.toolshed.shell import execute_js, muterun_js

date = QDate.currentDate().toString("yyyy.MM.dd")
newdate = date.replace('.', '-')
print (date)
print(newdate)



from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QTreeWidgetItemIterator
import ui_mainWindow1
# from ui_mainWindow import Ui_MainWindow



class MainWindow(QtWidgets.QMainWindow, ui_mainWindow1.Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.click_me)
        self.btn_test.clicked.connect(self.open_test_files)
        self.btn_run.clicked.connect(self.run_selected_tests)
        self.btn_logs.clicked.connect(self.print_all_logs)
        self.slc_all_btn.clicked.connect(self.select_all_checkboxs)
        self.rmv_all_btn.clicked.connect(self.remove_all_checkboxs)
        self.btn_stop.clicked.connect(self.stop_all_running_processes)
        self.list_of_test = []
        self.checked_item = []
        self.processes = []
        self.file_types = {
            ".js": "node",
            ".py": "python"
        }

        self.dir = ""

    def click_me(self):
        mylist = ["doron", "yoval", "siraz", "dani", "yaron"]

        self.pushButton.setText(random.choice(mylist))

#this function choosed files from specific folder & print to array all relevant tests (end JS).
    def open_test_files(self):
        self.dir = QtWidgets.QFileDialog.getExistingDirectory(self, "select folder")
        if self.dir:
            self.testslist.clear()
            for choosetest in os.listdir(self.dir):
                if choosetest.endswith('.js'):
                    item = QtWidgets.QTreeWidgetItem(self.testslist, [choosetest])
                    item.setCheckState(0, QtCore.Qt.Unchecked)
                    self.list_of_test.append(choosetest)
                    print(self.list_of_test)


#this function checks which tests is selected and print selected tests in array.
    def found_test_checked(self):
        iterator = QTreeWidgetItemIterator(self.testslist)
        while iterator.value():
            item=iterator.value()
            print(item)
            if item.checkState(0):
                item.text(0)
                self.checked_item.append(item.text(0))
                print(self.checked_item)
                self.btn_run.setEnabled(False)
                self.btn_test.setEnabled(False)
            iterator += 1


        return self.checked_item


    def generate_command_for_file_names(self, file_names):
        command_list = list(map(lambda file_name: f"{self.run_file_with(file_name)} {file_name}", file_names))
        return " && ".join(command_list)

    def run_file_with(self, file_name):
        if not self.file_types:
            return ""
        for eof in self.file_types:
            if file_name.endswith(eof):
                return self.file_types[eof]
        return ""

#this function run the tests that selected.
    def run_selected_tests(self):
        #try:
            checked_files = self.found_test_checked()
            print(checked_files)
            if not checked_files:
                return ""
            else:
                for test in self.checked_item:
                    time.sleep(2)
                    # print("C:/Users/Dafna Cohen/Desktop/CRM Project"+"/"+test)
                run_command = self.generate_command_for_file_names(checked_files)
                process = Popen(run_command, shell=True, cwd=self.dir)
                self.processes.append({"id": process.pid})
                print(self.processes)
                Terminate = process.poll()


            if Terminate is not None:
             self.btn_run.setEnabled(True)
             self.btn_test.setEnabled(True)




        #except:
            #print("Error")

    def clear(self):
        self.testslist.clear()

#this function print all Logs from current day to the screen.
    def print_all_logs(self):
        logger_file_path = self.dir + "/log/"
        print(logger_file_path)
        for file in os.listdir(logger_file_path):
            if (file.endswith(".log") and (file == str(newdate) +  "-results.log")):
                        logger_file_full_path = logger_file_path + file
                        print(logger_file_full_path)
                        with open(logger_file_full_path, "r") as logger_file:
                            self.textEdit.append(logger_file.read())

# this function select all checkbox & after that disable the button.
    def select_all_checkboxs(self):
        iterator = QTreeWidgetItemIterator(self.testslist)
        while iterator.value():
            item = iterator.value()
            print(item)
            item.setCheckState(0, QtCore.Qt.Checked)
            iterator += 1
            self.slc_all_btn.setEnabled(False)
            self.rmv_all_btn.setEnabled(True)


# this function remove all checkbox that was selected.
    def remove_all_checkboxs(self):
        iterator = QTreeWidgetItemIterator(self.testslist)
        while iterator.value():
            item = iterator.value()
            print(item)
            item.setCheckState(0, QtCore.Qt.Unchecked)
            iterator += 1
            self.rmv_all_btn.setEnabled(False)
            self.slc_all_btn.setEnabled(True)


    def kill(self, process_pid):
        #self.thread.stop()
        subprocess.Popen("taskkill /F /T /PID %i" % process_pid, shell=True)
        #Popen("TASKKILL /F /PID {pid} /T".format(pid=proc_pid))


#this function stop the Process that running with kill command.
    def stop_all_running_processes(self):
        warning_msg = "Are you sure you want to stop all processes??"
        question = QtWidgets.QMessageBox.question(self, "Note:", warning_msg, QtWidgets.QMessageBox.Yes,
                                              QtWidgets.QMessageBox.No)
        if question == QtWidgets.QMessageBox.Yes:
            for process in self.processes:
                self.kill(process["id"])
                self.btn_run.setEnabled(True)
                self.btn_test.setEnabled(True)





app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
