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
__date__ = "26 August 2017"
__author__ = 'Bilgin Sherifov <my.email@onthebeach.co.uk>'
             

import matplotlib
matplotlib.use("TkAgg")
import numpy as np
import sys
import os.path
from datetime import datetime
import logging

import config
import data_manipulation
import report

def __main__():

    '''The hourlyReport program is split into the following stages
        1.  houesekeeping
        2.  create a new general database interaction object (package dbutility)
            a.  prepare the bid upload script
            b.  fetch SQL data for last bit upload
            c.  prepare the cost, click SQL script
            d.  update the hourly report table and fetch latest cost, click data
        3.  process the data and perform the multiplications to obtain cost, clicks, impressions, CPC, avg position and CTR
        4.  create a figure holding this data
        5.  email the figure to everyone in the address book'''

    #############################################
    # 1.    housekeeping

    # obtain the root path from the config file and add the Utility packages to the system path
    rootPath = config.rootPath
    sys.path.append(os.path.join(rootPath))
    sys.path.append(os.path.join(rootPath, 'UtilityPackages'))


    logging.basicConfig(filename= config.hrLogFile, level=logging.DEBUG, format=config.format, datefmt='%d-%m-%Y %H:%M')

    logging.info('-------Program Started-------', extra = config.dctLog['OK'])

    # import new marketting tool packages for use in the hourly report generator
    from dbutility import gnrl_database_interaction as gdbi
    from mt_email import email_
    logging.info(' imported required internal modules ', extra = config.dctLog['OK'])

    #############################################
    # 2.    prepare SQL scripts and fetch data from the database

    # create a new general_database_interaction object (package dbutility)
    dataIn = {'credentials': config.credentials['MI'],
              'permissions': config.permissions['MI'],
              'scriptViolations': config.scriptViolations['SQL']
              }

    dbSqlObj = gdbi.DbSql(dataIn)

    # a,b. Get latest bid upload date for the hourly report figure
    _, message = dbSqlObj.prepare_script(config.bidUploadPathName)
    config.abort_pass_programme(message, ' sql script for bidUploadPathName prepared ')

    bidUploadData, message = dbSqlObj.fetch()
    config.abort_pass_programme(message, ' fetched last bid upload date ')

    # c,d. Update the table for the hourly report and pull latest data for specified dates (see config file)

    # populate the MI table with data for the last few hours
    '''_, message = dbSqlObj.run_stored_procedure('msdb.dbo.spGetGoogleAdwordsStdReportData', ['CampaignByHour', 'UK'])
    config.abort_pass_programme(message , ' finished running the stored procedure ')'''

    # prepare the script to fetch from the updated MI table
    _, message = dbSqlObj.prepare_script(config.sqlPathName, vars=config.hrSqlVarReplacements)
    config.abort_pass_programme(message, ' sql script for fetching MI data prepared ')

    # fetch from the updated MI table
    sqlData, message = dbSqlObj.fetch()
    config.abort_pass_programme(message, ' fetched report data ')

    #############################################
    # 3.  process the data and perform the multiplications to obtain cost, clicks, impressions, CPC, avg position and CTR

    # create a new daily report data manipulation object (package src)

    devices = ['All Devices']
    attachmentsPath = []

    for index, key in enumerate(devices):

        giveMe = data_manipulation.ManipulateData(sqlData, key)

        clicks, message = giveMe.clicks()
        cost, message = giveMe.cost()
        averageCostPerClick, message = giveMe.average_cost_per_click()
        impressions, message = giveMe.impressions()
        averagePosition, message = giveMe.average_position()
        clickThroughRate, message = giveMe.click_through_rate()

        #currentHour = int(datetime.now().hour -1)
        currentHour = int(datetime.now().hour)


        # remove any data from the previous hour as it is incomplete (we are part way through this current hour)
        if True:
            clicks.loc[currentHour][4] = np.nan
            cost.loc[currentHour][4] = np.nan
            averageCostPerClick.loc[currentHour][4] = np.nan
            averagePosition.loc[currentHour][4] = np.nan
            impressions.loc[currentHour][4] = np.nan
            clickThroughRate.loc[currentHour][4] = np.nan

        config.abort_pass_programme(message, ' processed data for daily report ')

        #############################################
        # 4.  create a figure holding this data
        # the dataIn dictionary contains all input data for the report generator
        dataIn = {
            'data': {
                'Impressions': impressions,
                'Clicks' : clicks,
                'Click through rate': clickThroughRate,
                'Cost (£)' : cost,
                'Average CPC (£)' : averageCostPerClick,
                'Average position' : averagePosition
            },
            'plot position' : ['Impressions',
                               'Clicks',
                               'Click through rate',
                               'Cost (£)',
                               'Average CPC (£)',
                               'Average position'],
            'device' : key,
            'file name': 'HourlyReport',
            'bid upload date' : bidUploadData,
            'root path': rootPath,
        }

        # create new hourly report generator object (package src)
        generate = report.GenerateReport(dataIn)

        # create the report
        strToday = config.hrSqlVarReplacements['dayPlaceHolder'].strip('\'')
        message = generate.report_aggregated_kw_curve(strToday)
        config.abort_pass_programme(message, ' reports generated ')

        # save the figures
        reportPath, message = generate.save_file()
        config.abort_pass_programme(message, ' reports saved ')
        attachmentsPath.append(reportPath)

    #############################################
    # 5.  email the figure to everyone in the address book (see config file)

    # the dataIn dictionary contains all input data for the emailer
    #print(message['error'])


    dataIn = {
        'username': config.credentials['Email']['Bilgin']['username'],
        'password': config.credentials['Email']['Bilgin']['password'],
        'my address': config.credentials['Email']['Bilgin']['my address'],
        'address book': config.addressBook,
        'subject': 'Hourly Report',
        'html': '<html><body><p> Please find attached the hourly report for Google non-brand PPC </p></body></html>',
        'attachment path': attachmentsPath
    }

    # create a new email object (package mt_email)
    emailer = email_.Email(dataIn)

    #send the report to everyone in the address book (see config file)
    message = emailer.send_mail()
    config.abort_pass_programme(message, ' emails sent ')

    logging.info(' -------Program Complete------- \n\n', extra=config.dctLog['OK'])


__main__()
