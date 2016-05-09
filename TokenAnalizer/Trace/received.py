'''
Created on Mar 8, 2016

@author: Gustavo Rodriguez
'''

from email.utils import parsedate as ParseDate
from email.utils import parseaddr as ParseAddr
from HeaderAnalizer.EmailTracertErrors import InvalidValue, InvalidToken
from ipaddress import ip_address as ip
from TokenAnalizer.utils import WhatIs





class ExtendedDomain(object):
    '''
    The information related to the tokens FROM and BY is called an described
    on the RFC 5321, section 4.4 as Extended-Domain in Augmented BNF notation
    This object receive this strings and make the analisys/disection
    '''

    
    def __init__(self,value=None,ip=None,domain=None,port=None,extra=None):
        
        #Values dictionary
        self._values = {'ip':'',
              'domain':'',
              'port':'',
              'extra':[]
              }
        self.__r_chars = ['[',']','(',')']
        
        if value == None:
            if ip != None:
                self._values['ip'] = ip
            if domain != None:
                self._values['domain'] = domain
            if port != None:
                self._values['port'] = port
            if extra != None:
                self._values['extra'] = extra
        else:
            self.__fill_values(value)
            
        #TODO: Please fix this uggly uggly method!
        self.__generate_attributes()
        
    def __str__(self):
        return self.__repr__()
    
    def __repr__(self):
        r = "ExtendedDomain("
        r_attr = ""
        for key in self._values.keys():
            if self._values[key] == '' or self._values[key] == []:
                pass
            else:
                r_attr = r_attr + str(key) + "=\"" + str(self._values[key]) + "\","
        if r_attr == "":
            return ""
        else:
            #Strip the last ,
            r = r + r_attr[:-1]
            r = r + ")"
            return r
    
    def __fill_values(self,value_list):            
        for val in value_list:
            #TODO: Before remove brackets and parenthesis
            #we should agroup this info
            val = self.__remove_chars(val, self.__r_chars)
            
            #Test if it is a domain
            if self.__is_domain(val):
                self._values['domain'] = val
            #Test if it is a ipv4
            elif WhatIs(val).IsIPv4():
                self._values['ip'] = ip(val)
            #Test if it is a ipv6
            elif WhatIs(val).IsIPv6():
                self._values['ip'] = ip(val)
            #Otherwise
            else:
                #It could be a tuple ip:port
                if val.find(':') != -1:
                    possible_ip,port = val.split(':')
                    if WhatIs(possible_ip).IsIP():
                        self._values['ip'] = ip(possible_ip)
                        self._values['port'] = port
                #Or somenthing else
                else:
                    self._values['extra'].append(val)
                         
            
                
    def __remove_chars(self,value,chars_list):
        for char in chars_list:
            value = value.replace(char,"")
        return value
           
  
    def __is_domain(self,value):
        #Domain should have at least on dot
        #TODO: Please improve this!!!!
        if value.find('.') != -1:
            v_list = value.split(".")
            if v_list[-1].isalpha():
                return True
            else:
                return False
        else:
            return False
    
    def __generate_attributes(self):
        # This function is to load the values in the dict
        # to an attributes of the ExtendedDomain Object
        
        #Create attributes with no values
        self.ip = ''
        self.domain = ''
        self.port = ''
        self.extra = ''
        
        #fill attributes
        if type(self._values['ip']) == ip:
            self.ip = self._values['ip']   
        
        if len(self._values['domain']) != 0:
            self.domain = self._values['domain']
        
        if len(self._values['port']) != 0:
            self.domain = self.port = self._values['port']
            
        if len(self._values['extra']) != 0:
            for e in self._values['extra']:
                self.extra = self.extra + ' ' + e 
            

class Received(object):
    '''
    Aanalize the Received values and return a dic object
    Please refer to RFC 5321, section 4.4
    https://tools.ietf.org/html/rfc5321#section-4.4
    '''
    
    def __init__(self, received_value=None,
                 from_val=None,
                 by_val=None,
                 via_val=None,
                 with_val=None,
                 for_val=None,
                 id_val=None,
                 date_val=None):

        self._values = {
                       'from':[],
                       'by':[],
                       'via':[],
                       'with':[],
                       'id':[],
                       'for':[],
                       'date': ''
                       }    
        if received_value != None:
            self.received_value = received_value
        
            #Value must have two parts, FROM part and DATE part
            #divided by a colon
            if self.received_value.find(";"):
                from_field,date_field = self.received_value.split(";")
            
                #Time of arrive to the server
                self._values['date'] = ParseDate(date_field)
                #Lets turn to Lower case to avoid errors on find method
                from_field = from_field.lower()
            
                #Lets break the from_field in to a list
                from_list = from_field.split()
                #Detect and loads values for each token
                self._fill_values(from_list)

                if self._values['from'] == []:
                    self.internal_jump = True
                else:
                    self.internal_jump = False
                    
                self._generate_attributes()
                
            else:
                raise InvalidToken(self.received_value,";")
        else:
            if from_val != None:
                self._values['from'] = from_val
            if by_val != None:
                self._values['by'] = by_val
            if with_val != None:
                self._values['with'] = with_val
            if for_val != None:
                self._values['for'] = for_val
            if id_val != None:
                self._values['id'] = id_val
            if via_val != None:
                self._values['via'] = via_val
            if date_val != None:
                self._values['date'] = date_val

            self._generate_attributes()

        if date_val == None and received_value == None:
            raise InvalidValue()
        
    def _generate_attributes(self):
        
        #Empty values
        self.from_val = []
        self.by = []
        self.via = []
        self.with_val = []
        self.id = []
        self.for_val = []
        self.date = ''
        
        #Lets parse values
        self._parse_by()
        self._parse_for()
        self._parse_from()
        
        #Fill attributes
        if self._values['from'] != []:
            self.from_val = self._values['from']
        if self._values['by'] != []:
            self.by = self._values['by']
        if self._values['via'] != []:
            self.with_val = self._values['with']
        if self._values['id'] != []:
            self.id = self._values['id']
        if self._values['for'] != []:
            self.for_val = self._values['for']
        if self._values['date'] != []:
            self.date = self._values['date']
            
            
    
            
    def _fill_values(self,from_list):
                
        #Valid Tokens
        tokens = ["from","by","via","with","for","id"]
        got_token = False
        for word in from_list:
            if word in tokens:
                got_token = True
                token_found = word
            else:
                if got_token:
                    self._values[token_found].append(word)
   
    def _parse_from(self):
        if self._values['from'] != []:
            self._values['from'] = ExtendedDomain(value=self._values['from'])
            
    def _parse_by(self):
        if self._values['by'] != []:
            self._values['by'] = ExtendedDomain(value=self._values['by'])  
    
    def _parse_for(self):
        if self._values['for'] != []:
            self._values['for'] = ParseAddr(self._values['for'])
    
    def __str__(self):
        return self.__repr__()
    
    def __repr__(self):
        string = "Received("
        vals = ""
        for key in self._values.keys():
            if self._values[key] == '' or self._values[key] == []:
                pass
            else:
                vals = vals + str(key) + "=" + str(self._values[key]) + ","
        if vals == "":
            return ""
        else:
            return string + vals[:-1] + ")"
