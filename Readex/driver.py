#driver script
import config
from login import mail
from clean import clean
from idex import check,details

my_mail = mail()
my_mail.login(config.SENDER_EMAIL_ADDRESS,config.PASSWORD)
my_mail.initiate()

#Input a value and retrieve the emails.
prompt = int(input("How many emails do you want to read"))
for num in range(prompt):
    content = my_mail.retrieve(num)
    print(1)
    clean_content = clean(content)
    print(clean_content)
    print("END"*50)
    print("\n"*10)

check(clean_content)
details(clean_content)
