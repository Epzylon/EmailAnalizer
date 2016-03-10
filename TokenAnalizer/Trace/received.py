'''
Created on Mar 8, 2016

@author: Gustavo Rodriguez
'''

import HeaderAnalizer.EmailTracertErrors.InvalidToken as InvalidToken
import email.utils.parsedate as ParseDate

class ExtendedDomain(object):
    '''
    The information related to the tokens FROM and BY is called an described
    on the RFC 5321, section 4.4 as Extended-Domain in Augmented BNF notation
    This object receive this strings and make the analisys/disection
    '''
    def __init__(self,value):
        self.value = value.split()
        #If the value has only one string, it must be the domain
        if len(self.value) == 1:
            self.domain = self.value[0]
        else:
            pass
        
    
    
        

class Received(object):
    '''
    Aanalize the Received values and return a dic object
    Please refer to RFC 5321, section 4.4
    https://tools.ietf.org/html/rfc5321#section-4.4
    '''
    
    def __init__(self, received_value):
        self.received_value = received_value
        
        #Valid Tokens
        tokens = ["from","by","via","with","id"]
               
        #Value must have two parts, FROM part and DATE part
        #divided by a colon
        if self.received_value.find(";"):
            from_field,date_field = self.received_value.split(";")
            
            #Time of arrive to the server
            self.date = ParseDate(date_field)
            
            #Lets turn to Lower case to avoid errors on find method
            from_field = from_field.lower()
            
            #Lets break the from_field in to a list
            from_list = from_field.split()
            
            self.values = {
                          'from':[],
                          'by':[],
                          'via':[],
                          'with':[],
                          'id':[]
            }
            
            for word in from_list:
                if word in tokens:
                    token_found = word
                else:
                    self.values[token_found].append(word)
            if self.values['from'] == []:
                self.internal_jump = True
            else:
                self.internal_jump = False
        else:
            raise InvalidToken(self.received_value,";")