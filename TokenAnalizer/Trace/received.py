'''
Created on Mar 8, 2016

@author: Gustavo Rodriguez
'''

#Email utils
from email.utils import parsedate as ParseDate
from email.utils import parseaddr as ParseAddr

#Customized raised errors
from HeaderAnalizer.EmailTracertErrors import InvalidValue, InvalidToken

#Ip object
from ipaddress import ip_address as ip

#Utils to parse some strings
from TokenAnalizer.utils import WhatIs, TextUtils

#Pyparsing objects
from pyparsing import OneOrMore, Group, Optional, Dict, Word, CaselessKeyword,\
    ParseException, printables

#TODO: Create a FOR class




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
            val = TextUtils(val).remove_chars(self.__r_chars)

            #Test if it is a domain
            if self.__is_domain(val):
                self._values['domain'] = val
            #Test if it is a ipv4
            elif WhatIs(val).IsIPv4():
                self._values['ip'] = ip(val)
            #Test if it is a ipv6
            #TODO:Check
            #BUG:Check if it really degtect IPv6
            elif WhatIs(val).IsIPv6():
                self._values['ip'] = ip(val)
            #Otherwise
            else:
                #It could be a tuple ip:port
                if val.find(':') != -1:
                    possible_ip,*port = val.split(':')
                    if WhatIs(possible_ip).IsIP():
                        self._values['ip'] = ip(possible_ip)
                        self._values['port'] = port
                #Or somenthing else
                else:
                    self._values['extra'].append(val)


    #TODO: Replace with utils function
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
        self.address = ''

        #fill attributes
        #TODO: Fix that! type(val) != ip
        if True:
            self.ip = self._values['ip']

        if len(self._values['domain']) != 0:
            self.domain = self._values['domain']

        if len(self._values['port']) != 0:
            self.domain = self.port = self._values['port']

        if len(self._values['extra']) != 0:
            for e in self._values['extra']:
                self.extra = self.extra + ' ' + e

        #This attribute is a easy way to get the ip or the domain
        if self.ip != '':
            self.address = str(self.ip)
        elif self.domain != '':
            self.address = self.domain


class Received(object):
    '''
    Aanalize the Received values and return a dic object
    Please refer to RFC 5321, section 4.4
    https://tools.ietf.org/html/rfc5321#section-4.4
    '''

    tokens = {
    'FROM': 'from',
    'BY': 'by',
    'VIA': 'via',
    'WITH': 'with',
    'ID': 'id',
    'FOR': 'for'
    }

    def __init__(self, received_value, rec_dict={}):
        # The received_value could be a dict or a string
        if rec_dict != {}:
            self.received = rec_dict
        else:
            try:
                # In case of string it MUST have ; to separate the date
                # Split the rec string and the date
                self._rec, self._date_string = received_value.split(';')

            except AttributeError:
                raise InvalidToken(received_value, ";")
            else:
                # Strip new line strings
                #TODO: Use dateutil to parse the date string
                self.received = self._parse_rec_string()
                self.received['date'] = ParseDate(self._date_string.replace('\n',''))
                self.DATE = self.received['date']

        self._fill_values()

    def _parse_rec_string(self):
        '''
        Pyparsing parser to the received string
        '''
        #any word
        word = Word(printables)

        #recognized tokens
        from_t = CaselessKeyword(self.tokens['FROM'])
        by_t = CaselessKeyword(self.tokens['BY'])
        with_t = CaselessKeyword(self.tokens['WITH'])
        id_t = CaselessKeyword(self.tokens['ID'])
        via_t = CaselessKeyword(self.tokens['VIA'])
        for_t = CaselessKeyword(self.tokens['FOR'])

        #A group of non tokens
        phrase = from_t | by_t | with_t | id_t | via_t | for_t

        #Group phrase with token
        from_g = Optional(Group(from_t + OneOrMore(word, stopOn=phrase).setParseAction(' '.join)))
        by_g = Optional(Group(by_t + OneOrMore(word, stopOn=phrase).setParseAction(' '.join)))
        with_g = Optional(Group(with_t + OneOrMore(word, stopOn=phrase).setParseAction(' '.join)))
        id_g = Optional(Group(id_t + OneOrMore(word, stopOn=phrase).setParseAction(' '.join)))
        via_g = Optional(Group(via_t + OneOrMore(word, stopOn=phrase).setParseAction(' '.join)))
        for_g = Optional(Group(for_t + OneOrMore(word, stopOn=phrase).setParseAction(' '.join)))


        grouped_data = from_g & by_g & with_g & id_g & via_g & for_g

        parse_to_dict = Dict(grouped_data)
        try:
            rec_dict = parse_to_dict.parseString(self._rec)
        except ParseException as e:
            rec_dict = {}

        return rec_dict

    def _fill_values(self):
        space = " "
        for token in self.tokens.keys():
            if token.lower() in self.received.keys():
                if type(self.received[token.lower()]) != str and len(self.received[token]) >1:
                    value = space.join(self.received[token.lower()])
                else:
                    value = self.received[token.lower()]
                setattr(self, token, value)

    def _analize_values(self):
        pass

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        repr_str = "Received(rec_dict={"
        for token in self.received.keys():
            if self.__getattribute__(token.upper()) != "":
                repr_str += "\'" + token.lower() + "\':\'" + str(self.__getattribute__(token.upper())) + "\',"
        # Remove the last ,
        repr_str = repr_str[:-1]
        repr_str += "})"

        return repr_str
