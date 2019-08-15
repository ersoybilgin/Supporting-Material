"""the email module is part of the mt_email package


Naming Conventions:

Package:            thispackage (short name)
Module:             this_module (short name)
Class:              ThisIsAClass
Function:           this_is_a_function
Public Method:      this_is_a_public_method
Non-Public Method:  _this_is_a_non_public_method
Variables:          thisIsAVariable
Constant:           THIS_IS_A_CONSTANT

"""

__status__ = "development"
__version__ = 'mdl 1.0.0'
__date__ = "6 August 2018"
__author__ = 'Bilgin Sherifov <bilgin.sherifov@onthebeach.co.uk>'

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from os.path import basename
from email.header import Header
from email import encoders


class Email(object):

    def __init__(self, dataIn):
        self.username = dataIn['username']
        self.password = dataIn['password']
        self.myAddress = dataIn['my address']
        self.addressBook = dataIn['address book']
        self.subject = dataIn['subject']
        self.attachmentPathName = dataIn['attachment path name']
        self.html = dataIn['html']

    def set_parameters(self, dataIn):
        '''
            Does something
            TO DO:  something
            '''
        message_ = {
            'error': None,
            'method': 'mt_email.Email.Email.set_paramaters',
            'description': "What does it do",
            'misc': None
        }


        try:
            self.username = dataIn['username']
            self.password = dataIn['password']
            self.myAddress = dataIn['my address']
            self.addressBook = dataIn['address book']
            self.subject = dataIn['subject']
            self.attachmentPathName = dataIn['attachment path name']

        except Exception as e:
            message_['error'] = "Something went wrong doing the function " + message_['method']+ ": " + str(e)
            data = ''
            print(message_['error'])
            pass

        return message_


    def send_mail(self):
        '''
            Does something
            TO DO:  something
            '''
        message_ = {
            'error': None,
            'method': 'mt_email.Email.Email.send_mail',
            'description': "What does it do",
            'misc': None
        }


        try:
            msg = MIMEMultipart()
            msg['Subject'] = self.subject
            msg['From'] = self.myAddress
            msg['To'] = self.addressBook

            html = self.html
            emailText = MIMEText(html, 'html')
            msg.attach(emailText)

            if self.attachmentPathName is not None:
                for eachAttachment in self.attachmentPathName:
                    with open(eachAttachment, "rb") as file_to_attach:
                        part = MIMEApplication(
                            file_to_attach.read(),
                            Name=basename(eachAttachment)
                        )
                        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(eachAttachment)
                        msg.attach(part)



            s = smtplib.SMTP('mail.........')
            s.ehlo()
            s.starttls()
            s.login(self.username, self.password)

            s.sendmail(self.myAddress, self.addressBook.split(","), msg.as_string())
            s.quit()

        except Exception as e:
            message_['error'] = "Something went wrong doing the function " + message_['method']+ ": " + str(e)
            #print(message_['error'])
            pass

        return message_