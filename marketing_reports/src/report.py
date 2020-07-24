"""the gnrl_database_interaction module is part of the dbutility package


Naming Conventions:

Package:            thispackage (short name)
Module:             this_module (short name)
Class:              ThisIsAClass
Function:           this_is_a_function
Public Method:      this_is_a_public_method
Non-Public Method:  _this_is_a_non_public_method
Variables:          thisIsAVariable
Constant:           THIS_IS_A_CONSTANT

"""

__status__ = "development"
__version__ = 'mdl 1.0.0'
__date__ = "25 August 2017"
__author__ = 'Bilgin Sherifov <my.email@onthebeach.co.uk>'



import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import seaborn as sns
import os
import numpy as np
from datetime import datetime
import pandas as pd
from matplotlib.font_manager import FontProperties

class GenerateReport(object):

    figure = ''
    bidUploadTime = ''


    def __init__(self, dataIn):

        self.data = dataIn['data']
        self.device = dataIn['device']
        self.bidUploadTime = dataIn['bid upload date']
        self.rootPath = dataIn['root path']
        self.plotPosition = dataIn['plot position']
        self.filePrefix = dataIn['file name']

    def report_aggregated_kw_curve(self, strToday):
        '''
            produces the table holding click data for each date provided in dataIn
            TO DO:  something
            '''
        message_ = {
            'error': None,
            'method': 'src.hr_report.ManipulateData.report',
            'description': "creates a figure for the hourly data",
            'misc': None
        }

        try:

            labels = ['Last year', 'Last month', 'Last week', 'Yesterday', 'Today']

            colors_ = ['lilac', 'powder blue', 'sky blue', 'azure', 'coral']
            sns.set_palette(sns.color_palette(sns.xkcd_palette(colors_)))


            myFig = plt.figure(figsize=(30, 18))
            sns.set_style("whitegrid")


            for index, key in enumerate (self.plotPosition):
                plt.subplot(2,3,index+1)
                for label_, clmn in zip(labels, self.data[key].columns):
                    plt.plot(self.data[key].index.values, self.data[key][clmn].values, linewidth=4, markersize=3,
                             label=label_ + ': ' + str(
                                 datetime.strptime(clmn, '%Y-%m-%d').date().strftime('%a %d %b %Y')),
                             alpha=1.0)

                    # get the index for all dates for up to the current hour
                    if clmn == strToday:
                        temp = self.data[key][clmn]
                        indexCurrentHour = temp[~temp.isnull()].index

                plt.title(key, fontsize=22, fontweight='bold')
                plt.xlim(0, 23)
                plt.xticks(range(0, 23, 3), fontsize=20, fontweight='bold')
                plt.yticks(fontsize=20, fontweight='bold')
                if index >= 3:
                    plt.xlabel('Time (h)', fontsize=20, fontweight='bold')
                if key == 'Average position':
                    plt.gca().invert_yaxis()

                # add Totals for the day so far for cost data
                if key == 'Cost (£)':
                    textFontProps = FontProperties()
                    textFontProps.set_size('x-large')
                    #textFontProps.set_family(['monospace', 'sans-serif'])
                    textAlignment_0 = {'horizontalalignment': 'left', 'verticalalignment': 'baseline'}
                    textAlignment_1 = {'horizontalalignment': 'right', 'verticalalignment': 'baseline'}

                    cumulativeCost = self.data[key].loc[indexCurrentHour].sum(axis=0)
                    maxValue = self.data[key].max().max()
                    textFontProps.set_weight('semibold')
                    plt.text(1, 0.95 * maxValue, 'Total for the day so far:',
                             fontproperties=textFontProps, **textAlignment_0)
                    textFontProps.set_weight('normal')
                    for j, sums_ in enumerate(cumulativeCost.iteritems()):
                        temp = labels[j] + ': ' + str(format(sums_[1], ',.0f'))
                        plt.text(10.0, (0.95 - (j+1)*.06) * maxValue, temp,
                                 fontproperties=textFontProps, **textAlignment_1)

            plt.legend(bbox_to_anchor=(-2.5, -0.18, 3.6, -0.), loc=6,
                       ncol=5, mode="expand", borderaxespad=2, fontsize=20, markerscale=10, frameon=False)

            #myFig.suptitle(self.device, fontsize=20, fontweight='bold')

            # plt.text('Bids last uploaded',0,0,0,0, fontsize= 16, fontweight= 'bold')
            #bidString = 'Bids last uploaded: ' + self.bidUploadTime['JobCreated'][0]
            myFig.suptitle(self.device + '    (Bids last uploaded: ' + self.bidUploadTime['JobCreated'][0] + ') ', fontsize=20, fontweight='bold')
            #plt.gcf().text(0.12, 0.001, bidString, fontsize=20, fontweight='bold')
            myFig.show()
            self.figure = myFig


        except Exception as e:
            message_['error'] = "Something went wrong doing the function " + message_['method']+ ": " + str(e)
            dataOut = ''
            #print(message_['error'])
            return dataOut, message_

        return message_


    def save_file(self):
        '''
            Does something
            TO DO:  something
            '''
        message_ = {
            'error': None,
            'method': 'src.hr_report.ManipulateData.report',
            'description': "What does it do",
            'misc': None
        }


        try:
            #fileName = (self.filePrefix +'_' + self.device + ' ' + datetime.now().strftime('%d-%m-%y %I %p') + '.png')
            fileName = (self.filePrefix + '_' + self.device + '.png')
            savePath = os.path.join(self.rootPath, 'MarketingReports', 'reports', 'figures', fileName)
            self.figure.savefig(savePath, papertype='a4', orientation='landscape')

        except Exception as e:
            message_['error'] = "Something went wrong doing the function " + message_['method']+ ": " + str(e)
            savePath = ''
            ##print(message_['error'])
            pass

        return savePath, message_



