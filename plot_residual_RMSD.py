#! /usr/bin/python

from phil import *
from CurveFit import *
from Experiment import *
from TimeCourse import *
from WellContent import *
import numpy as np
from alt_format_plate_wells_to_excel_sheet_mapping import plate_to_excel
from Plotter import *


def normList(L, normalizeTo=1):
    vMax = max(L)
    return [ float('%1.4f'%(x/(vMax*1.0)*normalizeTo)) for x in L]

excelfile = sys.argv[1]
_selection_gradient_ = sys.argv[2]
_inducer_gradient_ = sys.argv[3]

expt1 = Experiment(excelfile)

CurveFit_params = {}
Residual_RMSD = {}

#plate_to_excel = ['A1','B2','C3','D4','E5','F6','G7','H8' ]

for keys in plate_to_excel:
    timepoints = []
    well = TimeCourse(keys, expt1.extract_timecourse(keys))
    y = np.array(normList(well.data()))# !!! normalizes to 1
#    y = np.array(well.data())
    for i in range(len(well.data())):
        timepoints.append(i+1)
    x = np.array(timepoints)

    fitdata = ModifiedRichards(x, y)
    fitdata.Plot_CurveFit(keys)
    if not CurveFit_params.has_key(keys):
        CurveFit_params[keys] = []
    CurveFit_params[keys] = fitdata.Get_Coefficients()
    if not Residual_RMSD.has_key(keys):
        Residual_RMSD[keys] = float('%5.4f'%fitdata.Get_Residuals_RMSD())

#print Residual_RMSD

Residual_RMSD_ = WellContent(Residual_RMSD)
selection_gradient_ = WellContent(_selection_gradient_)
inducer_gradient_ = WellContent(_inducer_gradient_)
#print "Residual_RMSD_", Residual_RMSD_.conc_at('A1')

heat_map_Residual_RMSD = Plotter('Residual_RMSD', selection_gradient_, inducer_gradient_, Residual_RMSD_)

exit()

param1_wellcontent = open('param1_wellcontent','w')
param2_wellcontent = open('param2_wellcontent','w')
param3_wellcontent = open('param3_wellcontent','w')
param4_wellcontent = open('param4_wellcontent','w')

for keys in CurveFit_params:
#    print keys, CurveFit_params[keys][0], CurveFit_params[keys][1], CurveFit_params[keys][2], CurveFit_params[keys][3]
    param1_wellcontent.write('%s %5.4f\n'%(keys, CurveFit_params[keys][0]))
    param2_wellcontent.write('%s %5.4f\n'%(keys, CurveFit_params[keys][1]))
    param3_wellcontent.write('%s %5.4f\n'%(keys, CurveFit_params[keys][2]))
    param4_wellcontent.write('%s %5.4f\n'%(keys, CurveFit_params[keys][3]))


param1_wellcontent.close()
param2_wellcontent.close()
param3_wellcontent.close()
param4_wellcontent.close()

selection_gradient_ = WellContent(_selection_gradient_)
inducer_gradient_ = WellContent(_inducer_gradient_)
param1_wellcontent_ = WellContent('param1_wellcontent')
param2_wellcontent_ = WellContent('param2_wellcontent')
param3_wellcontent_ = WellContent('param3_wellcontent')
param4_wellcontent_ = WellContent('param4_wellcontent')

selection_gradient__ = []
inducer_gradient__ = []
param1_wellcontent__ = []
param2_wellcontent__ = []
param3_wellcontent__ = []
param4_wellcontent__ = []

for keys in plate_to_excel:
    selection_gradient__.append(selection_gradient_.conc_at(keys))
    inducer_gradient__.append(inducer_gradient_.conc_at(keys))
    
    param1_wellcontent__.append(param1_wellcontent_.conc_at(keys))
    param2_wellcontent__.append(param2_wellcontent_.conc_at(keys))
    param3_wellcontent__.append(param3_wellcontent_.conc_at(keys))
    param4_wellcontent__.append(param4_wellcontent_.conc_at(keys))

heat_map_param1 = Plotter('param1', selection_gradient__, inducer_gradient__, param1_wellcontent__)
heat_map_param1.plot()

heat_map_param2 = Plotter('param2', selection_gradient__, inducer_gradient__, param2_wellcontent__)
heat_map_param2.plot()

heat_map_param3 = Plotter('param3', selection_gradient__, inducer_gradient__, param3_wellcontent__)
heat_map_param3.plot()

heat_map_param4 = Plotter('param4', selection_gradient__, inducer_gradient__, param4_wellcontent__)
heat_map_param4.plot()


exit()

D3 = TimeCourse('D3',expt1.extract_timecourse('D3'))
y =np.array(D3.data())

timepoints = []
for i in range(len(D3.data())):
    timepoints.append(i+1)

x = np.array(timepoints)


#print x
#print y

fit = ModifiedRichards(x,y)
print fit.Get_Coefficients()
fit.Plot_CurveFit()
