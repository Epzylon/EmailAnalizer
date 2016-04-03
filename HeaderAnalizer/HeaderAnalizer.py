'''
Created on Mar 8, 2016
@author: grodriguez
'''
import email.message.Message as message
import email.utils.parseaddr as address
from HeaderAnalizer.EmailTracertErrors import NotMessageObject



class HeaderAnalizer(object):
    '''
    Receive a Mail message and analyze the Trace headers
    '''
    from_emails = []

    def __init__(self, message_string ):
        if not isinstance(message_string, message):
            raise NotMessageObject()
        else:
            self.message = message_string     
        self.from_emails = self._get_from()  
       
       
    
    def _get_from(self):
        email_list = []
        #As per RFC an email MUST have only on From field
        froms = self.message.get('from')
        for email in froms:
            email_list.append(address(email))
        return email_list
    

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
    
