'''
Created on Mar 8, 2016

@author: grodriguez
'''

class NotMessageObject(Exception):
    '''
    EmailTracert handles email.Message objects to study the email headers
    when we expect a email.Message and receive other stuff, we raise
    this Exception
    '''
    def __init__(self):
        pass
    
