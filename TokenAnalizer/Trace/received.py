'''
Created on Mar 8, 2016

@author: Gustavo Rodriguez
'''

import HeaderAnalizer.EmailTracertErrors.InvalidToken as InvalidToken
import HeaderAnalizer.EmailTracertErrors.InvalidValue as InvalidValue
import email.utils.parsedate as ParseDate
import ipaddr.IPAddress as IP

class ExtendedDomain(object):
    '''
    The information related to the tokens FROM and BY is called an described
    on the RFC 5321, section 4.4 as Extended-Domain in Augmented BNF notation
    This object receive this strings and make the analisys/disection
    '''
    values = {'ip':'',
              'domain':'',
              'extra':''
              }
    def __init__(self,value):
        self.v_list = value.split()
        #Get a list wit the values
        if len(self.v_list) == 1:
            
            single_value = self.v_list[0]
            single_value = self.__remove_brackets(single_value)
            single_value = self.__remove_parenthesis(single_value)
            
            if self.__is_domain(single_value):
                self.values['domain'] = single_value
            else:
                try:
                    IP(single_value)
                except:
                    raise InvalidValue(self.value)
                else:
                    self.values['ip'] = single_value
        if len(self.v_list) > 1:
            pass
                   
        else:
            pass
        
    def __remove_brackets(self,value):
        value = value.replace("[","")
        value = value.replace("]","")
        return value
    
    def __remove_parenthesis(self,value):
        value = value.replace("(","")
        value = value.replace(")","")

    
    def __is_domain(self,value):
        v_list = value.split(".")
        if v_list[-1].isalpha():
            return True
        else:
            return False


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