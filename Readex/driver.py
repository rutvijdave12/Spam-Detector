#driver script
import config
from login import mail
from clean import clean
from idex import check,details
from csv import reader
import pandas as pd

my_mail = mail()
my_mail.login(config.SENDER_EMAIL_ADDRESS,config.PASSWORD)
my_mail.initiate()

#Input a value and retrieve the emails.
prompt = int(input("How many emails do you want to read"))
sender_lst = []
subject_lst = []
body_lst = []
for num in range(prompt):
    sender,subject,body =  my_mail.main_content(num)
    sender = sender[1:-1]
    sender_lst.append(sender)
    subject_lst.append(subject)
    body_lst.append(body)
    print(f"Sender's email address:{sender}")
    print(f"Subject: {subject}")
    clean_body = clean(body)
    print(clean_body)
    print("END"*50)
    print("\n"*10)
#print(clean_body)

df = pd.DataFrame(list(zip(sender_lst,subject_lst,body_lst)),columns = ['Sender','Subject','Body'])
print(df)
df.to_csv('test.csv')
