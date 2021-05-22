import re
import os
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

class Plotcrap:

    def __init__(self):
        #locatefile variables
        self.homefolder = None  # input directory of where file is
        self.nameofile = None   # input the name of CSV file
        self.fileloc = None     # joined homefolder + nameofile
        #LSMtimecourse variables
        self.csv = None         #CSV array
        self.col0 = None
        self.col1 =None
        self.col2 = None
        self.col3 = None
        self.col4 =None




    def locatefile(self):
        self.homefolder = input('Are the files in the folder /home/pi/tempfiles/ (y or n)? ')
        if self.homefolder == 'y':
            self.homefolder = '/home/pi/tempfiles/'
        else:
            self.homefolder = input('enter the datapath in /folder/subfolder/ format:')
        if os.path.exists(self.homefolder):  # note this will check once and only once...don't screw up 2x
            print('good path')
        else:
            print('path does not exist.')
            self.homefolder = input('enter the datapath in /folder/subfolder/ format:')
        self.nameofile = input('Name of CSV file with the data (include extension):')
        self.fileloc = os.path.join(self.homefolder, self.nameofile)
        if os.path.exists(self.fileloc): # note this will check once and only once...don't screw up 2x
            print('good file')
        else:
            print('file does not exist.')
            self.nameofile = input('Name of CSV file with the data (include extension):')
            self.fileloc = os.path.join(self.homefolder, self.nameofile)

    def LSMtimecourse(self):
        self.csv = np.loadtxt(self.fileloc, delimiter=",", skiprows=1)
        # print(self.csv)
        self.col0 = np.array(self.csv[:,0], dtype = int)
        self.col1 = np.array(self.csv[:,1], dtype = float)
        self.col2 = np.array(self.csv[:,2], dtype = float)
        self.col3 = np.array(self.csv[:,3], dtype = int)
        self.col4 = np.array(self.csv[:,4], dtype = int)
        self.col5 = np.array(self.csv[:, 5], dtype=float)
        self.col6 = np.array(self.csv[:, 6], dtype=float)

        # print(self.col4)

    def plotthecsv(self):
        # Sets figure size in inches
        fig = plt.figure(figsize=(6, 9))

        ax = fig.add_subplot(3, 1, 1)
        ax.scatter(self.col0, self.col3, s=3, color=[1, 0, 0], label='ROI 1')
        ax.scatter(self.col0, self.col4, s=3, color=[0, 1, 0], label='ROI 2')
        # Here we set x and y labels as strings, they can be whatever you want them to be
        ax.set_xlabel('Frame')
        self.fig1y=input('Figure 1 Y - title')
        ax.set_ylabel(self.fig1y)
        ax.set_ylim(0, )
        # Here we eliminate the top and righthand parts of the box enclosing the figure
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.yaxis.set_ticks_position('left')
        ax.xaxis.set_ticks_position('bottom')
        # ax.xaxis.set_tick_params(rotation=90)
        # tempaxis1 = ax.xaxis.get_ticklabels()
        # tempaxis1 = list(set(tempaxis1) - set(tempaxis1[::rangeofint]))
        # for label in tempaxis1:
        #     label.set_visible(False)

        bx = fig.add_subplot(3, 1, 2)
        bx.scatter(self.col0, self.col5, s=3, color=[1, 0, 0], label='ROI 1')
        bx.scatter(self.col0, self.col6, s=3, color=[0, 1, 0], label='ROI 2')
        # Here we set x and y labels as strings, they can be whatever you want them to be
        bx.set_xlabel('Frame')
        self.fig2y=input('Figure 2 Y - title')
        bx.set_ylabel(self.fig2y)
        bx.set_ylim(0, )
        # Here we eliminate the top and righthand parts of the box enclosing the figure
        bx.spines['right'].set_visible(False)
        bx.spines['top'].set_visible(False)
        bx.yaxis.set_ticks_position('left')
        bx.xaxis.set_ticks_position('bottom')
        plt.legend(loc='lower left')
        # bx.xaxis.set_tick_params(rotation=90)
        # tempaxis2 = bx.xaxis.get_ticklabels()
        # tempaxis2 = list(set(tempaxis2) - set(tempaxis2[::rangeofint]))
        # for label in tempaxis2:
        #     label.set_visible(False)

        dx = fig.add_subplot(3, 1, 3)
        dx.scatter(self.col0, self.col2, s=3, color=[0, 0, 0])
        # Here we set x and y labels as strings, they can be whatever you want them to be
        dx.set_xlabel('Frame')
        dx.set_ylabel('5-HT Concentration (uM)')
        dx.set_ylim(-1, )
        # Here we eliminate the top and righthand parts of the box enclosing the figure
        dx.spines['right'].set_visible(False)
        dx.spines['top'].set_visible(False)
        dx.yaxis.set_ticks_position('left')
        dx.xaxis.set_ticks_position('bottom')
        # dx.xaxis.set_tick_params(rotation=90)
        # maxval = np.amax(self.data_baro_array)
        # maxlim = maxval + 0.5
        # minval = np.amin(self.data_baro_array)
        # if minval > 0:
        #     minlim = minval - 0.5
        # else:
        #     minlim = 99
        # dx.set_ylim([minlim, maxlim])
        #
        # tempaxis3 = dx.xaxis.get_ticklabels()
        # tempaxis3 = list(set(tempaxis3) - set(tempaxis3[::rangeofint]))
        # for label in tempaxis3:
        #     label.set_visible(False)

        plt.legend(loc='lower left')
        plt.subplots_adjust(left=0.12, bottom=0.1, right=0.95, top=0.95, wspace=0.2, hspace=1.00)
        plt.show()
        # fig.savefig(location_f)