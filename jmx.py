import os
from engine import *
from colorit import *

def parseJMX(jmx):
    cleanup()
    printArt()
    printFileName(jmx)
    validateTestPlan(jmx)
    findJMeterVersion(jmx)
    findThreadGroups(jmx)
    elementCheck(jmx)
    return

def printArt():
    print("""

***************************************************************
*                _   ______                   _               *
*               | | |  ____|                 | |              * 
*               | | | |__    __   __   __ _  | |              *
*           _   | | |  __|   \ \ / /  / _` | | |              *
*          | |__| | | |____   \ V /  | (_| | | |              *
*           \____/  |______|   \_/    \__,_| |_|              *   
*                                                             *   
*       v0.0.1 - (c) NaveenKumar Namachivayam 2020            *  
*                    QAInsights.com                           *
*                                                             *  
***************************************************************
  """)

def printFileName(jmx):
    print(f"\033[93m \nAnalyzing {jmx} \n")    
    return

def cleanup():
    try:
        os.remove("tmp.log")
    except:
        pass
    return