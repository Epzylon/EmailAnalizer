'''
Created on 2/5/2016

@author: epzylon
'''
from HeaderAnalizer.EmailTracertErrors import InvalidValue

class MessageID(object):
    '''
    Analize the Message-ID header
    '''

    def __init__(self, value):
        self.raw = value
        try:
            left,right = self.value.split('@')
        except ValueError:
            raise InvalidValue
        
        self.id_left = left.strip('<')
        self.id_right = right.strip('>')
        
    
    def __str__(self):
        return (self.id_left + '@' + self.id_right)
    
    def __repr__(self):
        return ('MessageID(\'' + self.raw + '\'')
    
        
    
    
        
        