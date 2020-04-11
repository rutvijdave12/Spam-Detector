#driver script
import config
from login import mail
from clean import clean
from csv import reader
from reduce import filter
import pandas as pd

my_mail = mail()
my_mail.login(config.SENDER_EMAIL_ADDRESS,config.PASSWORD)
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
df.to_csv('emails.csv')
