from engine import *

def parseJMX(jmx):
    printArt()
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
