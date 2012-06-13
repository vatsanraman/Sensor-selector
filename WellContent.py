#! /usr/bin/python

from phil import *

class WellContent:

    def __init__(self, data):
        self.data = data
#        print "Initializing WellContent object ...", self.name
        self.parse()

    def parse(self):# parses both dictionary and text files
        __wellcontent = {}
        if isinstance(self.data, dict):#checking for dictionary
#            print "Is a dict", self
            __wellcontent = self.data
        else:
            _wellcontent = open(self.data,'r')
            line = _wellcontent.readline()
            while line:
                l = string.split(line)
                if not __wellcontent.has_key(l[0]):
                    __wellcontent[l[0]] = float(l[1])
                line = _wellcontent.readline()
        self.wellcontent = __wellcontent
#        print self.wellcontent
    
    def conc_at(self,wellid):
        return self.wellcontent[wellid]

    def key_list(self):
        return self.wellcontent.keys()

    def val(self):
        return self.wellcontent.values()
    
        

