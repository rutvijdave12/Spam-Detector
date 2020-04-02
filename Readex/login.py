#'(UID BODY[1])'
#'(RFC822)'
#'(UID BODY[TEXT])'

import imaplib
import email
import config

class mail:

    def login (self,UNM,PASS):
        self.msvr = imaplib.IMAP4_SSL('imap.gmail.com',993)
        self.msvr.login(UNM,PASS)

    def initiate (self):
        self.msvr.select("Inbox")
        typ, data = self.msvr.search(None, 'ALL')
        ids = data[0]
        self.id_list = ids.split()
        self.id_list = self.id_list[::-1]
        latest_email_id = int( self.id_list[0] )

    def retrieve (self,num):
        status,data = self.msvr.fetch(self.id_list[num],'(RFC822)' )
        return data[0][1]
