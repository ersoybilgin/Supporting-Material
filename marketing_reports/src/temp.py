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

import pymssql

with pymssql.connect(server=config.credentials['MI']['server'],
                     user=config.credentials['MI']['username'],
                     password=config.credentials['MI']['password'],
                     database=config.credentials['MI']['database'])  as conn:
    with conn.cursor(as_dict=True) as cursor:
        cursor.callproc('msdb.dbo.spGetGoogleAdwordsStdReportData', ('CampaignByHour','UK',))
    print('FINISHED')