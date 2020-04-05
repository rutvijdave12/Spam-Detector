#idex tries to extract all the ids from the mail read after cleaning all the html tags.
import re
from email.parser import BytesParser, Parser
from email.policy import default

#my_str = "Hi my name is John and email address is john.doe@somecompany.co.uk and my friend's email is jane_doe124@gmail.com"
#emails = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", my_str)

#check function will try to extract all the email ids from the given input which is an already cleaned content
def check(my_str):
#Input my_str is the clean content passed into the check function to get the email ids.
    #print(my_str)
    emails = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", my_str)
    for mail in emails:
        print(mail)

#details function will take clean content as the input and output the 'To', 'From', 'Subject'.        
def details(string):
    headers = Parser(policy=default).parsestr(string)

    #  Now the header items can be accessed as a dictionary:
    print('To: {}'.format(headers['to']))
    print('From: {}'.format(headers['from']))
    print('Subject: {}'.format(headers['subject']))

    # You can also access the parts of the addresses:
    print('Recipient username: {}'.format(headers['to'].addresses[0].username))
    print('Sender name: {}'.format(headers['from'].addresses[0].display_name))
