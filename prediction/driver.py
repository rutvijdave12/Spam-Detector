#driver script
import config
from login import mail
from clean import clean
from csv import reader
from reduce import filter
import pandas as pd
from login_gui import Ui_MainWindow
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np

# login_gui.gui()
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
credentials = ui.credentials
if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtWidgets.QApplication.instance().exec_()

try:
    #print(credentials)
    my_mail = mail()
    my_mail.login(credentials[0],credentials[1])
    my_mail.initiate()

    #Input a value and retrieve the emails.
    prompt = int(input("How many emails do you want to read: "))
    sender_lst = []
    subject_lst = []
    body_lst = []
    count = 0
    for num in range(prompt):
        sender,subject,body =  my_mail.main_content(num)
        sender = sender[1:-1]
        subject = filter(subject)
        #print(body)
        clean_body = clean(body)
        #print(clean_body)
        clean_body = filter(clean_body)
        sender_lst.append(sender)
        subject_lst.append(str(subject)[1:-1])
        body_lst.append(str(clean_body)[1:-1])

        # print(f"Sender's email address:{sender}")
        # print(f"Subject: {subject}")
        # print(clean_body)
        count += 1
        print(count)
    #print(clean_body)
    print("done")
    # Spam = [0]*len(subject_lst)
    # print(Spam)


    df = pd.DataFrame(list(zip(sender_lst,subject_lst,body_lst,Spam)),columns = ['Sender','Subject','Body','Spam'])
    #print(df)
    df.to_csv('my_emails.csv')
    #import trial

except IndexError:
    print("Insufficient Data")

except Exception:
    print("Login Error")
