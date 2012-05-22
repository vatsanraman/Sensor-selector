#! /usr/bin/python

from phil import *

#for matplotlib
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

class Plotter:
    def __init__(self, name, _X, _Y, _Z):
        self.name = name
        self.X = _X
        self.Y = _Y
        self.Z = _Z
        print "Initializing plotter object ...", self.name

    def plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_xscale('log')
        ax.set_yscale('log')
        ax.scatter(self.X,self.Y,c=self.Z,cmap = plt.jet(), s=670, lw = 0.1, marker = 's')
        bar = fig.colorbar(ax.collections[0])
        plt.show()
        fig.savefig('%s.png'%self.name)
