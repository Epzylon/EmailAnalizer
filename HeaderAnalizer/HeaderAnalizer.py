'''
Created on Mar 8, 2016
@author: grodriguez
'''
from email import message_from_string as m_string
from email.utils import parseaddr as address
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
            self.from_address = address(self.message.get('from'))
            

       
       


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
    
