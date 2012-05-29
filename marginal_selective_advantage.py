#! /usr/bin/python

from phil import *
from Experiment import *
from TimeCourse import *

def Help():
    print 'This script generates a plot of differences in mean/median growth rate across adjacent wells for a fixed selection or inducer value'
    print 'Usage: <excel sheet>'
    exit()

excelfile = sys.argv[1]
expt1 = Experiment(excelfile)

plate_row = ['A','B','C','D','E','F','G','H']
diff_data = {}
for items in plate_row:
    junk = []
    for i in range(12):
        if i+2<=12:
            first_well = '%s%s'%(items,i+2)
            second_well = '%s%s'%(items,i+1)
            tmp1 = TimeCourse(first_well,expt1.extract_timecourse(first_well))
            tmp2 = TimeCourse(second_well, expt1.extract_timecourse(second_well))
            diff = tmp2.median() - tmp1.median()
            junk.append(float('%1.4f'%diff))
    if not diff_data.has_key(items):
        diff_data[items] = []
    diff_data[items] = junk

for keys in diff_data:
    outfile = open('%s_outfile'%keys,'w')
    for items in diff_data[keys]:
        outfile.write('%s\n'%items)
    outfile.close()
