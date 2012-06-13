#! /usr/bin/python

from raman import *

def normList(L, normalizeTo=1):
    vMax = max(L)
    return [ float('%1.4f'%(x/(vMax*1.0)*normalizeTo)) for x in L]

excelfile = sys.argv[1]
_selection_gradient_ = sys.argv[2]
_inducer_gradient_ = sys.argv[3]

expt1 = Experiment(excelfile)

CurveFit_params = {}
Residual_RMSD = {}
Final_OD = {}

timepoints = []
for i in range(expt1.total_timepoints()):
    timepoints.append(i+1)
x = np.array(timepoints)



for keys in plate_to_excel:
    well = TimeCourse(keys, expt1.extract_timecourse(keys))
    y = np.array(well.data())
    y_norm = np.array(normList(well.data())) #normalized to 1 for calculating residuals

    fitdata = ModifiedRichards(x, y)
    fitdata_norm = ModifiedRichards(x, y_norm)

    if not CurveFit_params.has_key(keys):
        CurveFit_params[keys] = []
    CurveFit_params[keys] = fitdata.Get_Coefficients()
    
    if not Residual_RMSD.has_key(keys):
        Residual_RMSD[keys] = float('%5.4f'%fitdata_norm.Get_Residuals_RMSD())

    if not Final_OD.has_key(keys):
        Final_OD[keys] = 0.0
    Final_OD[keys] = well.final_val()

#for keys in CurveFit_params.keys():
#    print keys, Residual_RMSD[keys], Final_OD[keys], CurveFit_params[keys][0], CurveFit_params[keys][1], CurveFit_params[keys][2], CurveFit_params[keys][3]

Good_CurveFits = []

for keys in plate_to_excel:
    GoodFit = True

    if (Residual_RMSD[keys] > 0.70) or (Final_OD[keys] < 0.2) or (CurveFit_params[keys][0] < 0) or (CurveFit_params[keys][3] > 1) or (CurveFit_params[keys][3] < 0):
        GoodFit = False
#    print "GoodFit", keys, GoodFit
    if GoodFit == True:
        Good_CurveFits.append(keys)
    
#        sys.stdout.write('%s %5.4f %5.4f %5.4f %5.4f\n'%(keys, Residual_RMSD[keys], Final_OD[keys], CurveFit_params[keys][0], CurveFit_params[keys][3]))

#print "Good_CurveFits"
#print Good_CurveFits

param_x0 = {}
param_y0 = {}
param_c = {}
param_k = {}
        
for keys in Good_CurveFits:
#    print keys, CurveFit_params[keys]
    if not param_x0.has_key(keys):
        param_x0[keys] = 0.0
    param_x0[keys] = CurveFit_params[keys][0]
    if not param_k.has_key(keys):
        param_k[keys] = 0.0
    param_k[keys] = CurveFit_params[keys][3]

param_x0_ = WellContent(param_x0)
param_k_ = WellContent(param_k)
selection_gradient_ = WellContent(_selection_gradient_)
inducer_gradient_ = WellContent(_inducer_gradient_)
Final_OD_ = WellContent(Final_OD)

heat_map_x0 = Plotter('junk_x0', selection_gradient_, inducer_gradient_, param_x0_)
heat_map_c = Plotter('junk_k', selection_gradient_, inducer_gradient_, param_k_)
heat_map_Final_OD = Plotter('junk_final_od', selection_gradient_, inducer_gradient_, Final_OD_)


    

