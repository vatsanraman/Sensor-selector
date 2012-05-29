#! /usr/bin/python

from phil import *
from Experiment import *
from TimeCourse import *
from WellContent import *
from Plotter import *

import numpy as np
import scipy
from scipy.optimize import curve_fit
import pylab

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
expt1.extract_all_timecourses()
print expt1.all_timecourses

for keys in expt1.all_timecourses:
    print keys, expt1.all_timecourses[keys].data()
exit()
#print expt1.total_timepoints()
#print expt1.total_timecourses()
#print expt1.extract_timecourse('A1')
#A1 = TimeCourse('A1',expt1.extract_timecourse('A1'))
#A1.display()
#print A1.mean()

def sigmoid(x, x0, k):
    y = 1/(1 + np.exp(-k*(x-x0)))
    return y

#test_key_set = ['A1','A2','A3','A4']
test_key_set = ['D3']

plate_data_object_list = []
#for item in plate_to_excel.keys(): #turn on later
for item in test_key_set:
    tmp = TimeCourse(item,expt1.extract_timecourse(item))
    plate_data_object_list.append(tmp)




selection = []
inducer = []
OD = []


for item in plate_data_object_list:
    tmp1 = []
    tmp2 = []
    count = 1
    for ll in item.data():
        tmp1.append(count)
        tmp2.append(ll)
        count += 1

    xdata = np.array(tmp1)
    ydata = np.array(tmp2)
    print tmp1, xdata
    print tmp2, ydata
    popt, pcov = scipy.optimize.curve_fit(sigmoid, xdata, ydata)
    print popt
    x = np.linspace(0,85,85)
    y = sigmoid(x, *popt)
    pylab.plot(xdata, ydata, 'o', label='data')
    pylab.plot(x,y, label='fit')
#    pylab.ylim(0, 1.05)
    pylab.legend(loc='best')
    pylab.show()

exit()
#    print item.name, item.mean(),selection_gradient.conc_at(item.name),inducer_gradient.conc_at(item.name)
#    selection.append(selection_gradient.conc_at(item.name))
#    inducer.append(inducer_gradient.conc_at(item.name))
#    OD.append(item.mean())
    
    

exit()
heat_map = Plotter('junk',selection,inducer,OD)
heat_map.plot()


