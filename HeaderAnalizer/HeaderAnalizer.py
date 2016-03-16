'''
Created on Mar 8, 2016

@author: grodriguez
'''
import email.message.Message as message
from HeaderAnalizer.EmailTracertErrors import NotMessageObject



class HeaderAnalizer(object):
    '''
    Receive a Mail message and analyze the Trace headers
    '''


    def __init__(self, message_string ):
        if not isinstance(message_string, message):
            raise NotMessageObject()
        else:
            self.message = message_string   
    
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
    
    

        