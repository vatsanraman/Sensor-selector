#! /usr/bin/python

from phil import *
from Experiment import *

def Help():
    print 'Script for testing objects'
    print 'Usage:'
    exit()

if len(argv) < 2:
    print Help()

inputfile = sys.argv[1]

expt1 = Experiment(inputfile)