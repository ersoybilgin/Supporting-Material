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


__status__  = "development"
__version__ = 'mdl 1.0.0'
__date__    = "23 August 2017"
__author__  = 'Bilgin Sherifov <bilgin.sherifov@onthebeach.co.uk>'

import numpy as np
import pandas as pd
import pymssql
import time as tm
from ldap3 import Server, Connection, ALL




class DbSql(object):

    def __init__(self, dataIn):
        self.queryScript = ''
        self.credentials = dataIn['credentials']
        self.permissions = dataIn['permissions']
        self.scriptViolations = dataIn['scriptViolations']


    def prepare_script(self, scriptPathName, vars = None):
        '''
            Accepts the path to a script file, then checks / produces a viable SQL script
            TO DO:  write the security check function
            '''

        message_ = {
            'error': None,
            'method': 'dbutility.gnrldatabase_interaction.DbSql.prepare_script',
            'description': "converts script into viable sql script",
            'misc': None
        }

        try:
            # Load SQL template from file
            with open(scriptPathName, 'r') as scriptFile:
                queryScript = scriptFile.read()

            # Replace placeholders with actual values
            if vars != None:
                for key, value in vars.items():
                    queryScript = queryScript.replace(key, value)
            self.queryScript = queryScript

        except Exception as e:
            message_['error'] = "Something went wrong reading the SQL script: " + str(e)
            self.queryScript = ''
            #print(message_['error'])
            pass
        return self.queryScript, message_


    def push(self):
        '''
            Pushes data to the SQL database
            TO DO:  write main code
            '''
        data = ''
        message_ = {
            'error': None,
            'method': 'packagename.module_name.ClassTemplate.push',
            'description': "What does it do",
            'misc': None
        }

        try:
            # Check that the user has the right credentials to execute the method
            clearance = self.permissions_check()
            if clearance['error'] != None:
                message_['error'] = clearance['error']
                return self.queryScript, message_

            # Check that the script doesnt violate function purpose
            clearance = self.script_check('push')
            if clearance['error'] != None:
                message_['error'] = clearance['error']
                return self.queryScript, message_
            '''

            The main code goes here 

            '''
            pass

        except Exception as e:
            message_['error'] = "Something went wrong doing the function push: " + str(e)
            data = ''
            #print(message_['error'])
            pass

        return message_, data


    def fetch(self):
        '''
            Pushes data to the SQL database
            TO DO:
            '''
        data = ''
        message_ = {
            'error': None,
            'method': 'packagename.module_name.ClassTemplate.fetch',
            'description': "Collects data from the SQL database on the " + self.credentials['server'] + ' server',
            'misc': None
        }

        try:
            # Check that the user has the right credentials to execute the method
            clearance = self.permissions_check('fetch')
            if clearance['error'] != None:
                message_['error'] = clearance['error']
                return self.queryScript, message_

            # Check that the script doesnt violate function purpose
            clearance = self.script_check('fetch')
            if clearance['error'] != None:
                message_['error'] = clearance['error']
                return self.queryScript, message_

            timeStart = tm.time()
            with pymssql.connect(server=self.credentials['server'],
                                 user=self.credentials['username'],
                                 password=self.credentials['password'],
                                 database=self.credentials['database']) as dbConnection:
                try:
                    data = pd.read_sql(self.queryScript, dbConnection)


                    # add an index column with unique values
                    data['index'] = np.arange(len(data))
                    data.set_index('index', inplace=True)
                except pymssql.OperationalError as e:
                    data = None
                    message_['error'] = 'Data was not fetched  (' + str(e) + ')'
                    return data, message_

            runTime = np.round((tm.time() - timeStart) / 60, 1)
            message_['misc'] = 'Time elapsed for retrieving data from DB into a table: ' + str(runTime) + 'min'

        except Exception as e:
            message_['error'] = "Something went wrong doing the function fetch: " + str(e)
            data = ''
            return data, message_

        return data, message_


    def update(self):
        '''
            Pushes data to the SQL database
            TO DO:  write main code
            '''
        data = ''
        message_ = {
            'error': None,
            'method': 'packagename.module_name.ClassTemplate.update',
            'description': "What does it do",
            'misc': None
        }

        try:
            # Check that the user has the right credentials to execute the method
            clearance = self.permissions_check()
            if clearance['error'] != None:
                message_['error'] = clearance['error']
                return self.queryScript, message_

            # Check that the script doesnt violate function purpose
            clearance = self.script_check('update')
            if clearance['error'] != None:
                message_['error'] = clearance['error']
                return self.queryScript, message_
            '''

            The main code goes here 

            '''
            pass

        except Exception as e:
            message_['error'] = "Something went wrong doing the function update: " + str(e)
            data = ''
            #print(message_['error'])
            pass

        return message_, data


    def design(self):
        '''
            Pushes data to the SQL database
            TO DO:  write main code
            '''
        data = ''
        message_ = {
            'error': None,
            'method': 'packagename.module_name.ClassTemplate.design',
            'description': "What does it do",
            'misc': None
        }

        try:
            # Check that the user has the right credentials to execute the method
            clearance = self.permissions_check()
            if clearance['error'] != None:
                message_['error'] = clearance['error']
                return self.queryScript, message_

            # Check that the script doesnt violate function purpose
            clearance = self.script_check('design')
            if clearance['error'] != None:
                message_['error'] = clearance['error']
                return self.queryScript, message_
            '''

            The main code goes here 

            '''
            pass

        except Exception as e:
            message_['error'] = "Something went wrong doing the function design: " + str(e)
            data = ''
            #print(message_['error'])
            pass

        return message_, data


    def run_stored_procedure(self, nameTable, listArguments):
        '''
                    Pushes data to the SQL database
                    TO DO:  write main code
                    '''

        # run_stored_procedure(self, nameTable(string), listVars(list of strings))

        message_ = {
            'error': None,
            'method': 'packagename.module_name.ClassTemplate.design',
            'description': "What does it do",
            'misc': None
        }
        try:
            with pymssql.connect(server=self.credentials['server'],
                                 user=self.credentials['username'],
                                 password=self.credentials['password'],
                                 database=self.credentials['database']) as dbConnection:
                with dbConnection.cursor(as_dict=True) as cursor:
                    cursor.callproc(nameTable, tuple(listArguments))
                    #cursor.callproc('msdb.dbo.spGetGoogleAdwordsStdReportData', ('CampaignByHour', 'UK',))
        except Exception as e:
            message_['error'] = 'Data was not fetched  (' + str(e) + ')'
            return message_

        return message_


    def permissions_check(self, sourceMethod):
        '''
            Does something
            TO DO:  something
            '''
        message_ = {
            'error': None,
            'method': 'dbutility.gnrldatabase_interaction.DbSql.permissions_check',
            'description': "What does it do",
            'misc': None
        }
        try:
            if self.permissions[self.credentials['username']][sourceMethod]:
                pass
            else:
                message_['error'] = "User doesn't have permission to use the function " + sourceMethod

            '''

            The main code goes here 

            '''
            pass

        except Exception as e:
            message_['error'] = "Something went wrong doing the function permissions_check: " + str(e)
            #print(message_['error'])
            pass

        return message_


    def script_check(self,sourceMethod):
        '''
            Does something
            TO DO:  something
            '''
        message_ = {
            'error': None,
            'method': 'dbutility.gnrldatabase_interaction.DbSql.script_check',
            'description': "What does it do",
            'misc': None
        }

        #print(self.queryScript)
        try:

            violations = self.scriptViolations[sourceMethod]
            for word in violations:
                if self.queryScript.lower().find(word.lower()) > -1:
                    message_['error'] = 'Script contains: ' + str(word) + ' - permission violation for the function ' + sourceMethod
                    return message_


        except Exception as e:
            message_['error'] = "Something went wrong doing the script_check function: " + str(e)
            #print(message_['error'])
            pass

        return message_