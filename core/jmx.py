import os

from core.engine import *


def parse_jmx(jmx):
    """
    Parses a JMX file
    @param jmx: path to JMX file
    """
    # boilerplate
    cleanup()
    print_art()
    print_file_name(jmx)

    # jmx related computing
    tree = validate_test_plan(jmx)
    validate_jmeter_version(tree)
    find_thread_groups(tree)
    element_check(tree)
    plugins_check(tree)



def print_art():
    """
    Prints the console header of the app
    """
    print("""
\033[94m 
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
JEval helps you to evaluate your JMeter test plan and provides recommendation 
before you start your performance testing.
  """)


def print_file_name(jmx):
    """
    Prints (in yellow) the filename of the JMX being analyzed
    @param jmx: path to JMX file
    """
    print(f"\033[93m \t Analyzing {jmx} \n")


def cleanup():
    """
    Removes previous (or trailing) log files in the execution folder
    """
    try:
        os.remove("tmp.log")
    except OSError:
        pass
