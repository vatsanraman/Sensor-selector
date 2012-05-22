#! /usr/bin/python

from phil import *
from Experiment import *
from TimeCourse import *
from WellContent import *
from Plotter import *

def Help():
    print 'Script for testing objects'
    print 'Usage:'
    exit()

if len(argv) < 2:
    print Help()

excelfile = sys.argv[1]
wellcontent_file1 = sys.argv[2]
wellcontent_file2 = sys.argv[3]
outputfile = sys.argv[4]


selection_gradient = WellContent(wellcontent_file1)
inducer_gradient = WellContent(wellcontent_file2)
#print selection_gradient.conc_at('A1')
#print inducer_gradient.conc_at('A1')

expt1 = Experiment(excelfile)
#print expt1.total_timepoints()
#print expt1.total_timecourses()
#print expt1.extract_timecourse('A1')

#A1 = TimeCourse('A1',expt1.extract_timecourse('A1'))
#A1.display()
#print A1.mean()

test_key_set = ['A1','A2','A3','A4']

plate_data_object_list = []
#for item in plate_to_excel.keys(): #turn on later
for item in test_key_set:
    tmp = TimeCourse(item,expt1.extract_timecourse(item))
    plate_data_object_list.append(tmp)



selection = []
inducer = []
OD = []

for item in plate_data_object_list:
    print item.name, item.mean(),selection_gradient.conc_at(item.name),inducer_gradient.conc_at(item.name)
    selection.append(selection_gradient.conc_at(item.name))
    inducer.append(inducer_gradient.conc_at(item.name))
    OD.append(item.mean())

#normalized_OD = normList(OD) #NOTE: we are plotting OD normalized to 1
heat_map = Plotter('junk',selection,inducer,OD)
heat_map.plot()


