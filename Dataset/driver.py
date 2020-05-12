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
        subject_lst.append(subject)
        body_lst.append(clean_body)
        # print(f"Sender's email address:{sender}")
        # print(f"Subject: {subject}")
        # print(clean_body)
        count += 1
        print(count)
    #print(clean_body)
    print("done")


    df = pd.DataFrame(list(zip(sender_lst,subject_lst,body_lst)),columns = ['Sender','Subject','Body'])
    #print(df)
    print(1)
    df.to_csv('my_emails.csv')
    print(2)

except IndexError:
    print("Insufficient Data")

except Exception:
    print("Login Error")
