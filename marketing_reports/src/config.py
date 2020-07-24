from datetime import datetime, timedelta
import os
import logging
import sys

dateEndTemp = datetime.now()


rootPath = os.path.join(os.path.expanduser('G:'),os.path.sep, 'MARKETING_TOOLS', 'Projects', 'Python')
sqlPathName = os.path.join(rootPath,'MarketingReports','materials','SQL', 'hourlyReportDataTEMP.txt')
bidUploadPathName = os.path.join(rootPath,'MarketingReports','materials','SQL', 'bidToolUploadTime.txt')

##########Logging##########

hrLogFile = os.path.join(rootPath, 'MarketingReports', 'logs', 'Hourly_Report.log')
drLogFile = os.path.join(rootPath, 'MarketingReports', 'logs', 'Daily_Report.log')
statusLog = {
        'OK ': '[__OK__]',
        'FAIL': '[_FAIL_]'
    }
format = '%(asctime)s %(status)-8s %(separator)-3s %(message)s'

dctLog = {
    'FAIL': {
        'status': '[ FAIL ]',
        'separator': ' - '
    },
    'OK': {
        'status': '[      ]',
        'separator': ' - '
    }
}

####################

addressBook = ', '.join([    
    'my.email@onthebeach.co.uk',
    'name_1.surname_1@onthebeach.co.uk',
	'name_2.surname_2@onthebeach.co.uk',
	'name_3.surname_3@onthebeach.co.uk',
])

credentials = {
    'MI': {
        'server':   'server', 
        'database': 'database',
        'username': 'username',
        'password': 'password',
    },
    'Email': {
        'Bilgin': {
            'username': 'username',
            'password': 'password',
            'my address': 'my.email@onthebeach.co.uk'
        },
        'Datascience': {
            'username': 'username',
            'password': 'password',
            'my address': 'datascience.email@onthebeach.co.uk'
        },
    },
    'Mongo': {

    }
}


hrSqlVarReplacements = {
    'dayPlaceHolder': "'" + (dateEndTemp - timedelta(days=0)).date().strftime('%Y-%m-%d') + "'",
    'yestPlaceHolder': "'" + (dateEndTemp - timedelta(days=1)).date().strftime('%Y-%m-%d')+ "'",
    'weekPlaceHolder': "'" + (dateEndTemp - timedelta(days=7)).date().strftime('%Y-%m-%d')+ "'",
    'monthPlaceHolder': "'" + (dateEndTemp - timedelta(days=28)).date().strftime('%Y-%m-%d')+ "'",
    'yearPlaceHolder': "'" + (dateEndTemp - timedelta(days=364)).date().strftime('%Y-%m-%d')+ "'"
}

drSqlVarReplacements = {
    'dayPlaceHolder': "'" + (dateEndTemp - timedelta(days=1)).date().strftime('%Y-%m-%d') + "'",
    'yestPlaceHolder': "'" + (dateEndTemp - timedelta(days=2)).date().strftime('%Y-%m-%d')+ "'",
    'weekPlaceHolder': "'" + (dateEndTemp - timedelta(days=8)).date().strftime('%Y-%m-%d')+ "'",
    'monthPlaceHolder': "'" + (dateEndTemp - timedelta(days=29)).date().strftime('%Y-%m-%d')+ "'",
    'yearPlaceHolder': "'" + (dateEndTemp - timedelta(days=365)).date().strftime('%Y-%m-%d')+ "'"
}

permissions = {
    'MI':{
        'name_1.surname_1': {
            'fetch': True,
            'push': True,
            'update': False,
            'design': False
        },
        'name_2.surname_2': {
            'fetch': True,
            'push': True,
            'update': False,
            'design': False
        },
        'name_3.surname_3': {
            'fetch': True,
            'push': True,
            'update': False,
            'design': False
        },
    },
    'Mongo': {}

}

scriptViolations = {
    'SQL': {
        'fetch' : ['INSERT', 'CREATE TABLE', 'DROP DATABASE', 'ALTER TABLE', 'UPDATE', 'DELETE'],
        'push:' : ['CREATE TABLE', 'DROP DATABASE', 'ALTER TABLE', 'UPDATE', 'DELETE'],
        'update' : [],
        'design' : []
    },
    'Mongo' : {}
}

def abort_pass_programme(objMessage,logString):
    if objMessage['error'] != None:
        logging.info(objMessage['error'], extra=dctLog['FAIL'])
        sys.exit()
    else:
        logging.info(logString, extra=dctLog['OK'])
