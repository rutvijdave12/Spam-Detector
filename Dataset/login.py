#login has a class called mail consisting of 3 functions.


#'(UID BODY[1])'-----------------> used to get just the body of the email.
#'(RFC822)'----------------------> gets you the whole email contents.
#'(UID BODY[TEXT])'--------------> again gets you just the body of the email but with some changes(see for yourself).

import imaplib
import email
import config
from email.parser import BytesParser, Parser
from email.policy import default

class mail:

#login function helps you to login to your email by passing your email credentials.
#This function is invoked in the driver script after instantiating the class mail.
    def login (self,UNM,PASS):
        #A server is created using the imap library.
        #For gmail it is imap.gmail.com and the port used for reading the mails is the standard 993.
        self.msvr = imaplib.IMAP4_SSL('imap.gmail.com',993)
        self.msvr.login(UNM,PASS)

#initiate will select the inbox of your email you can change it to other stuff by printing msvr.list() and typing one of the list contents...
#instead of "Inbox"
    def initiate (self):
        self.msvr.select("Inbox")
        typ, data = self.msvr.search(None, 'ALL')
        #typ while give you 'OK' and data stores the corresponding mail ids in bytes for eg. b'100'.
        ids = data[0]
        self.id_list = ids.split()
        #Creating a list of id for easy access and then reversing the list so that the latest mail is the first element of the list (like a stack).
        self.id_list = self.id_list[::-1]
        latest_email_id = int( self.id_list[0] )

#retrieve uses a fetch method which will fetch you a particular email depending on the parameter passed in your driver script.
    def main_content (self,num):
        #data is a two dimensional array which whose (0,1)th element will have the data stored.
        status,data = self.msvr.fetch(self.id_list[num], '(RFC822)')
        script = data[0][1].decode("utf-8",errors = 'ignore')
        #print(script)
        email_m = email.message_from_string(script)
        sender = email_m['From'].split()[-1]
        sub = email_m['Subject']
        typ,dat = self.msvr.fetch(self.id_list[num],'(UID BODY[1])')
        text = dat[0][1].decode(encoding = "utf-8",errors = 'ignore')
        '''
        print("rm")
        print(rm)
        print("done")
       # mail1 = email.message_from_string(data[0][1])
        print("printing mail")
        #print(mail1)
        print("printed")'''
        return sender,str(sub),str(text)




'''
    typ, data = M.fetch(num, '(RFC822)')
mail = email.message_from_string(data[0][1])
headers = HeaderParser().parsestr(data[0][1]) 
message = parse_message(mail)  #body
org = headers['From']


email.utils.parseaddr(address)'''