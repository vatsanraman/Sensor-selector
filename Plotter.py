#! /usr/bin/python

from phil import *
from WellContent import *
#for matplotlib
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from alt_format_plate_wells_to_excel_sheet_mapping import plate_to_excel

class Plotter:
    def __init__(self, name, _X, _Y, _Z):
        self.name = name
#        self.X = _X
#        self.Y = _Y
#        self.Z = _Z
#        self.Z = self.normalize(_Z)
#        print "Initializing plotter object ...", self.name
#        plate_to_excel = ['A1','B2','C3','D4','E5','F6','G7','H8' ]
        X_ = []
        Y_ = []
        Z_ = []
        xmin = min(_X.val())/10.0 
        xmax = 10.0*max(_X.val())
        ymin = min(_Y.val())/10.0
        ymax = 10.0*max(_Y.val())
#        print "_Z.key_list", _Z.key_list()
        for keys in _Z.key_list():
            X_.append(_X.conc_at(keys))
            Y_.append(_Y.conc_at(keys))
            Z_.append(_Z.conc_at(keys))

        self.__Plot(X_, Y_, Z_, xmin, xmax, ymin, ymax)


    def __Plot(self, X, Y, Z, xmin, xmax, ymin, ymax):
        fig = plt.figure()
        ax = fig.add_subplot(111)

        ax.set_xscale('log')
        ax.set_yscale('log')
        ax.scatter(X,Y,c=Z,cmap = plt.jet(), s=670, lw = 0.6, marker = 's')

        bar = fig.colorbar(ax.collections[0])
        ax.set_xlim([xmin, xmax])
        ax.set_ylim([ymin, ymax])
        plt.show()
        fig.savefig('%s.png'%self.name)

    

    def normalize(self, L):
        normalizeTo = 1
        vMax = max(L)
        return [ float('%1.4f'%(x/(vMax*1.0)*normalizeTo)) for x in L]
