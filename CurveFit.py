#! /usr/bin/python

from phil import *
import numpy as np
import scipy.optimize
import matplotlib.pyplot as plt


#Base class for CurveFit
#Under this base class, we can declare different types of
#functional forms

class CurveFit:
    def __init__(self, x, y):
        self.x = x
        self.y = y
#        print "Initializing CurveFit object ..."

#Derived class ModifiedRichards
class ModifiedRichards(CurveFit):
    def get_array(self):
        print self.x
        print self.y

    def __ModifiedRichardsFunc(self, p, x):
        x0, y0, c, k=p
        y = c/(1 + np.exp(-k*(x-x0))) + y0
        return y

    def __Residuals(self, p, x, y):
        return y - self.__ModifiedRichardsFunc(p, x)

    def __Coefficients(self):
        x = self.x
        y = self.y
#        p_guess = (1, 1, 1, 0) ### NB: Hardcoded initial guess. This may not work all the time ####
        p_guess = (np.median(x), np.median(y), max(y), min(y))
        (p, cov, infodict, mesg, ier) = scipy.optimize.leastsq(self.__Residuals, p_guess,args=(x,y),full_output=1)

        x0,y0,c,k=p  
#        print('''Reference data:\  
#    x0 = {x0}
#    y0 = {y0}
#    c = {c}
#    k = {k}
#    '''.format(x0=x0,y0=y0,c=c,k=k))  

        # Create a numpy array of x-values

        return p

    def __Plot_CurveFit(self, fig_name):
        x = self.x
        y = self.y
        p = self.__Coefficients()
        numPoints = np.floor((x.max()-x.min())*100)
        xp = np.linspace(x.min(), x.max(), numPoints)
        print 'numPoints is:  ',numPoints
        print 'xp is:  ',xp
        print 'p is:  ',p
        
        pxp=self.__ModifiedRichardsFunc(p,xp)
        print 'pxp is:  ',pxp
        plt.clf()
        plt.plot(x, y, '>', xp, pxp, 'g-')
        plt.xlabel('Timepoints') 
        plt.ylabel('OD, A600',rotation='vertical')
        plt.ylim([0,1])
        plt.title('%s'%fig_name)

        plt.grid(True)
        plt.savefig('%s.png'%fig_name)
#        plt.show()


    def Get_Coefficients(self):
#        print "Getting Coefficients"
        return self.__Coefficients()

    
    def Plot_CurveFit(self, fig_name):
        self.__Plot_CurveFit(fig_name)

    def Get_Residuals_RMSD(self):
#        print "Getting Residuals..."
        x = self.x
        y = self.y
        p_guess = (np.median(x), np.median(y), max(y), min(y))
        return self.__RMSD(self.__Residuals(p_guess, x, y))
        

    def __RMSD(self, data):
        return (np.sqrt(np.mean(data**2)))
        
        
