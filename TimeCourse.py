#! /usr/bin/python

from phil import *
import stats

class TimeCourse:
    def __init__(self,name,datapoints):
        self.name = name
        self.datapoints = datapoints
        print "Initializing TimeCourse object ..", self.name
    
    def name(self):
        return self.name

    def data(self):
        return self.datapoints
    
    def mean(self):
        return float('%1.4f'%stats.lmean(self.datapoints))

    def median(self):
        return float('%1.4f'%stats.lmedian(self.datapoints))

