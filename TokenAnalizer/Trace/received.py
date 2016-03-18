'''
Created on Mar 8, 2016

@author: Gustavo Rodriguez
'''

from HeaderAnalizer.EmailTracertErrors import InvalidToken
from email.utils import parsedate as ParseDate
from IPy import IP


class ExtendedDomain(object):
    '''
    The information related to the tokens FROM and BY is called an described
    on the RFC 5321, section 4.4 as Extended-Domain in Augmented BNF notation
    This object receive this strings and make the analisys/disection
    '''

    
    def __init__(self,value):
        
        #Values dictionary
        self.values = {'ip':'',
              'domain':'',
              'port':'',
              'extra':''
              }
        
        self.v_list = value.split()
        self.__r_chars = ['[',']','(',')']
        self.__fill_values(self.v_list)
        
        
    def __str__(self):
        string = ""
        for i in self.values.keys():
            string = string + i + ": " + self.values[i] + " "
        return string
            
        
    def __fill_values(self,value_list):            
        for val in value_list:
            val = self.__remove_chars(val, self.__r_chars)
            if self.__is_domain(val):
                self.values['domain'] = val
            else:
                try:
                    IP(val)
                except:
                    #Tiny fix to dectect ips/domains with port
                    if val.find(':') != -1:
                        ipdom,port = val.split(':')
                        self.values['port'] = port
                        try:
                            #Let see if it is an ip
                            IP(ipdom)
                            self.values['ip'] = ipdom
                        except:
                            #otherwise it should be a domain
                            if self.__is_domain(ipdom):
                                self.values['domain'] = ipdom
                    else:
                        self.values['extra'] = self.values['extra'] + val
                else:
                    self.values['ip'] = val
            
                
    def __remove_chars(self,value,chars_list):
        for char in chars_list:
            value = value.replace(char,"")
        return value
  
    def __is_domain(self,value):
        #Domain should have at least on dot
        if value.find('.') != -1:
            v_list = value.split(".")
            if v_list[-1].isalpha():
                return True
            else:
                return False
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
        tokens = ["from","by","via","with","for","id"]
               
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
                          'id':[],
                          'for':[],
                          'date': self.date
            }
            #TODO: This part brokes if the first word of the string is not
            # a token
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
    
    def __str__(self):
        string = ""
        for i in self.values.keys():
            if self.values[i] != []:
                string = string + i + ": " + str(self.values[i]) + " "
        return string