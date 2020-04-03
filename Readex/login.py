#login has a class called mail consisting of 3 functions.


#'(UID BODY[1])'-----------------> used to get just the body of the email.
#'(RFC822)'----------------------> gets you rhe whole email contents.
#'(UID BODY[TEXT])'--------------> again gets you just the body of the email but with some changes(see for yourself).

import imaplib
import email
import config

class mail:

#login function helps you to login to your email by passing your email credentials.
#This function is invoked in the driver script after instantiating the class mail.
    def login (self,UNM,PASS):
        self.msvr = imaplib.IMAP4_SSL('imap.gmail.com',993)
        self.msvr.login(UNM,PASS)

#initiate will select the inbox of your email you can change it to other stuff by printing msvr.list() and typing one of the list contents...
#instead of "Inbox"
    def initiate (self):
        self.msvr.select("Inbox")
        typ, data = self.msvr.search(None, 'ALL')
        ids = data[0]
        self.id_list = ids.split()
        self.id_list = self.id_list[::-1]
        latest_email_id = int( self.id_list[0] )

#retrieve uses a fetch method which will fetch you a particular email depending on the parameter passed in your driver script.
    def retrieve (self,num):
        status,data = self.msvr.fetch(self.id_list[num],'(RFC822)' )
        return data[0][1]
