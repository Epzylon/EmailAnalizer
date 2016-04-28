'''
Created on Mar 8, 2016
@author: grodriguez
'''
from email import message_from_string as m_string
from email.utils import parseaddr as address
from email.utils import parsedate as date
from HeaderAnalizer.EmailTracertErrors import NotMessageObject



class HeaderAnalizer(object):
    '''
    Receive a Mail message and analyze the Trace headers
    '''
    from_emails = []

    def __init__(self, message_string):
        try:
            self.message = m_string(message_string)
        except:
            pass
        else:
            #############################################
            # Headers that should appears at most once  #
            #############################################
            
            #Odd header            
            self.orig_date = date(self.message.get('orig-date'))
            
            #Address type headers
            self.sender = address(self.message.get('sender'))
            self.reply_to = address(self.message.get('reply-to'))
            
            #ID type headers
            self.message_id = self.message.get('message-id')
            self.in_reply_to = self.message.get('in-reply-to')
            self.references = self.message.get('references')
            
            #Subject
            self.subject = self.message.get('subject')
            
            
            #############################################
            # Headers that could appears more than once #
            #############################################
            
            #From,bcc,cc,reply-to
            
            

            
            

       
       


    def getHeaders(self):
        pass
    
    def getBody(self):
        pass
    
    def getTraceHeaders(self):
        pass
    
    def getTraceIPList(self):
        pass
    
    def getTraceTimming(self):
        pass
    
    def getMailEditor(self):
        pass
    
