"""the db_sql class is part of the general database interaction module


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
__version__ = 'pkg 1.0.0'
__date__    = "23 August 2017"
__author__  = 'Bilgin Sherifov <bilgin.sherifov@onthebeach.co.uk>'
__copyright__ = "Copyright 2017, On The Beach Ltd"
__credits__ = ["Bilgin Sherifov"]
__license__ = "???????"
__created__ =  "22/08/2017"
__maintainer__ = "data Science Team"
__email__ = ["bilgin.sherifov@onthebeach.co.uk"]



hardDependencies = {'numpy':'np', 'pandas':'pd', 'time':'tm', 'pymssql':'pymssql'}

missingDependencies = []

for module_, newName in hardDependencies.items():
    try:
        # load 'module_' and alias it as 'newName'
        globals()[newName] =  __import__(module_)
    except ImportError as e:
        missingDependencies.append(module_)

if missingDependencies:
    raise ImportError("Missing required dependencies {0}".format(missingDependencies))