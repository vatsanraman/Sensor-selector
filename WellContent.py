#! /usr/bin/python

from phil import *

class WellContent:

    def __init__(self, name):
        self.name = name
        print "Initializing WellContent object ...", self.name
        self.parse()

    def parse(self):
        __wellcontent = {}
        _wellcontent = open(self.name,'r')
        line = _wellcontent.readline()
        while line:
            l = string.split(line)
            if not __wellcontent.has_key(l[0]):
                __wellcontent[l[0]] = float(l[1])
            line = _wellcontent.readline()
        self.wellcontent = __wellcontent
        print __wellcontent
    
    def conc_at(self,wellid):
        return self.wellcontent[wellid]

