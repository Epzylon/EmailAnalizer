'''
Created on 4/5/2016

@author: epzylon
'''
from ipaddress import IPv4Address as ip4
from ipaddress import IPv6Address as ip6

class WhatIs(object):
    '''
    Try to determine what is the given value
    '''


    def __init__(self, value):
        self.value = value
    
    def this(self):
        if self.IsDomain():
            return ('domain')
        elif self.IsIP():
            if self.IsIPv4():
                return ('ip4')
            elif self.IsIPv6():
                return ('ip6')
        elif self.IsEmailAddr():
            return ('email')
        elif self.IsHeader():
            return ('header')
        else:
            return ('unknown')
    

    def IsDomain(self):
        pass
    
    def IsIP(self):
        '''
        If it is a ip (v4 or v6) it returns True
        '''
        if self.IsIPv4():
            return(True)
        elif self.IsIPv6():
            return(True)
        else:
            return(False)
    
    def IsIPv4(self):
        '''
        It retutns true only if it is a ipv4 (on a 4 octets form)
        '''
        #IPv4Addess allows one, two or tree decimal doted
        #digits as valid address, but we only want 4 octets
        if len(self.value.split('.')) == 4:
            try:
                ip4(self.value)
            except:
                return(False)
            else:
                return(True)        
    
    def IsIPv6(self):
        '''
        It returns true only if it is a ipv6
        '''
        try:
            ip6(self.value)
        except:
            return(False)
        else:
            return(True)
        
    
    def IsEmailAddr(self):
        pass
    
    def IsHeader(self):
        pass
    