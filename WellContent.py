#! /usr/bin/python

from phil import *

class WellContent:

    def __init__(self, name):
        self.name = name
        print "Initializing WellContent object ...", self.name
        self.parse()

    def parse(self):
        _wellcontent_tmp = {}
        _wellcontent = open(self.name,'r')
        line = _wellcontent.readline()
        while line:
            l = string.split(line)
            if not _wellcontent_tmp.has_key(l[0]):
                _wellcontent_tmp[l[0]] = float(l[1])
            line = _wellcontent.readline()
        print _wellcontent_tmp
