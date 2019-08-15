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
__author__ = 'Bilgin Sherifov <bilgin.sherifov@onthebeach.co.uk>' 


import numpy as np
from datetime import datetime
import pandas as pd


class ManipulateData(object):

    data = []

    def __init__(self, dataIn, device):

        self.device = device

        if device == 'All Devices':
            #print('Analysing all devices')
            self.data = dataIn
        elif device == 'Desktop':
            self.data = dataIn[dataIn['Device'] == 'Desktop']
            #print('Analysing Desktop')
        elif device == 'Mobile':
            self.data = dataIn[dataIn['Device'] == 'Mobile']
            #print('Analysing Mobile')
        elif device == 'Tablet':
            self.data = dataIn[dataIn['Device'] == 'Tablet']
            #print('Analysing Tablet')
        else:
            self.data = []
            #print('Device not recognised')


    def clicks(self):
        '''
            produces the table holding click data for each date provided in dataIn
            TO DO:  something
            '''
        message_ = {
            'error': None,
            'method': 'src.hr_data_manipulation.ManipulateData.clicks',
            'description': "What does it do",
            'misc': None
        }

        try:
            dataOut = self.data[['TrafficDate', 'HourOfDay', 'Clicks']].groupby(['TrafficDate','HourOfDay']).sum().unstack(
            level=0)
            dataOut.columns = dataOut.columns.get_level_values(1)


        except Exception as e:
            message_['error'] = "Something went wrong doing the function " + message_['method']+ ": " + str(e)
            dataOut = ''
            #print(message_['error'])
            pass

        return dataOut, message_

    def cost(self):
        '''
            produces the table holding cost data for each date provided in dataIn
            TO DO:  something
            '''
        message_ = {
            'error': None,
            'method': 'src.hr_data_manipulation.ManipulateData.cost',
            'description': "What does it do",
            'misc': None
        }

        try:
            dataOut = self.data[['TrafficDate', 'HourOfDay', 'Cost']].groupby(['TrafficDate','HourOfDay']).sum().unstack(
            level=0)
            dataOut.columns = dataOut.columns.get_level_values(1)


        except Exception as e:
            message_['error'] = "Something went wrong doing the function " + message_['method']+ ": " + str(e)
            dataOut = ''
            #print(message_['error'])
            pass

        return dataOut, message_

    def average_cost_per_click(self):
        '''
            produces the table holding average_cost_per_click data for each date provided in dataIn
            TO DO:  something
            '''
        message_ = {
            'error': None,
            'method': 'src.hr_data_manipulation.ManipulateData.average_cost_per_click',
            'description': "What does it do",
            'misc': None
        }

        try:
            cost, _ = self.cost()
            click, _ = self.clicks()

            dataOut = cost.divide(click)

        except Exception as e:
            message_['error'] = "Something went wrong doing the function " + message_['method']+ ": " + str(e)
            dataOut = ''
            #print(message_['error'])
            pass

        return dataOut, message_

    def impressions(self):
        '''
            produces the table holding impressions data for each date provided in dataIn
            TO DO:  something
            '''
        message_ = {
            'error': None,
            'method': 'src.hr_data_manipulation.ManipulateData.impressions',
            'description': "What does it do",
            'misc': None
        }

        try:
            dataOut = self.data[['TrafficDate', 'HourOfDay', 'Impressions']].groupby(
                ['TrafficDate','HourOfDay']).sum().unstack(level=0)
            dataOut.columns = dataOut.columns.get_level_values(1)


        except Exception as e:
            message_['error'] = "Something went wrong doing the function " + message_['method']+ ": " + str(e)
            dataOut = ''
            #print(message_['error'])
            pass

        return dataOut, message_

    def average_position(self):
        '''
            produces the table holding average_position data for each date provided in dataIn
            TO DO:  something
            '''
        message_ = {
            'error': None,
            'method': 'src.hr_data_manipulation.ManipulateData.average_position',
            'description': "What does it do",
            'misc': None
        }

        try:
            dataOut = self.data[['TrafficDate', 'HourOfDay', 'Impressions', 'AvgPosition']]
            dataOut['actualPosition'] = dataOut['AvgPosition'] * dataOut['Impressions']
            dataOut = dataOut[['TrafficDate', 'HourOfDay', 'actualPosition']].groupby(
                ['TrafficDate','HourOfDay']).sum().unstack(level=0)
            dataOut.columns = dataOut.columns.get_level_values(1)
            impression, _ = self.impressions()
            dataOut = (dataOut / impression)

        except Exception as e:
            message_['error'] = "Something went wrong doing the function " + message_['method']+ ": " + str(e)
            dataOut = ''
            #print(message_['error'])
            pass

        return dataOut, message_

    def click_through_rate(self):
        '''
            produces the table holding click_through_rate data for each date provided in dataIn
            TO DO:  something
            '''
        message_ = {
            'error': None,
            'method': 'src.hr_data_manipulation.ManipulateData.click_through_rate',
            'description': "What does it do",
            'misc': None
        }

        try:
            click, _ = self.clicks()
            impression, _ = self.impressions()
            dataOut = click.divide(impression)


        except Exception as e:
            message_['error'] = "Something went wrong doing the function " + message_['method']+ ": " + str(e)
            dataOut = ''
            #print(message_['error'])
            pass

        return dataOut, message_


