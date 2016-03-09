'''
Created on Mar 8, 2016

@author: Gustavo Rodriguez
'''

import HeaderAnalizer.EmailTracertErrors.InvalidToken as InvalidToken
import email.utils.parsedate as ParseDate

class Received(object):
    '''
    Aanalize the Received values and return a dic object
    Please refer to RFC 5321, section 4.4
    https://tools.ietf.org/html/rfc5321#section-4.4
    '''
    
    def __init__(self, received_value):
        self.received_value = received_value
               
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
            
            #Searching tokens
            #BY tokens MUST exist and appears both on internal jump
            #as well in normal jumps
            by_found = from_list.count("by")
            
            #On internal jumps the token FROM doesn't appears (against RFC?)
            from_found = from_list.count("from")
            
            #The following are optional tokens
            via_found = from_list.count("via")
            with_found = from_list.count("with")
            id_found = from_list.count("id")
            for_found = from_list.count("for")
            
            #This matrix will order the tokens once having the index value
            m_received = []
            
            #Each received string must have a "BY" token
            if by_found == 0:
                raise InvalidToken(self.received_value,"BY")
            else:
                by_id = from_list.index("by")
                m_received.append(['by', by_id])
            
            #FROM token appears on normal jumps, otherwise
            #it is a internal jump
            if from_found == 1:
                from_id = from_list.find("from")
                self.internal_jump = False
                m_received.append(['from',from_id])
            else:
                self.internal_jump = True
            
            #Index values on optional tokens
            if via_found == 1:
                via_id = from_list.index("via")
                m_received.append(['via',via_id])
            
            if with_found == 1:
                with_id = from_list.index("with")
                m_received.append(['with',with_id])
                
            if id_found == 1:
                id_id = from_list.index("id")
                m_received.append(['id',id_id])
            
            if for_found == 1:
                for_id = from_list.index("for")
                m_received.append(['for',for_id])
            
            m_received.sort(key=lambda x: x[1])
            
        if not self.internal_jump:
            self.from_value = from_list[from_id+1:by_id]
        
            
        else:
            raise InvalidToken(self.received_value,";")
        
        
        
    def getReceivedDict(self):
        pass
    
    def getIP(self):
        pass
    
    def getDomain(self):
        pass
    
    def getTCPInfo(self):
        pass
    
    def getOptInfo(self):
        pass
    
    def getVia(self):
        pass
    
    def getWith(self):
        pass
    
    def getID(self):
        pass
    
    def getFor(self):
        pass
    