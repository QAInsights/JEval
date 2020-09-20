import xml.etree.ElementTree as ET
import xml.dom.minidom as XD
import argparse
import sys
import fileinput
import pdb
import yaml
import logging
from attributeCheck import *
from colorit import *
from display import *

def elementCheck(jmx):
    '''
    This function will check for each element in JMeter.
    Returns: Each Elements status
    '''
    with open('./config.yaml','r') as file:
        try:
            #Reading Config file
            elements=yaml.safe_load(file)
            #Looping JMeter > Elements
            for element in elements['JMeter']['Elements']:
                #Calling Elements Check
                findElementStatus(jmx,element)
                if element == "IfController" or element == "LoopController":
                    attributeCheck(jmx,element)
        except yaml.YAMLError as e:
            #print(e)
            printRed(e)
    return

def findElementStatus(jmx, element):
    '''
    This function will get called from elementCheck().
    Returns each element status.
    '''    
    tree = ET.parse(jmx)
    root = tree.getroot()
    enabledCount = 0
    flag = 0
    message=f"No element found for {element}"
    for node in root.iter(element):
        if node.attrib is None:
            printRed(message)
        else:
            if str.__contains__(str(node.attrib),'\'enabled\': \'true\''):            
                #Find enabled count
                enabledCount += 1
                #Set flag for success
                flag=1
                message=f"{enabledCount} {element}(s) enabled."
            else:
                message=f"No {element} enabled."
                #Set flag for fail
                flag=0
    
    if flag == 1:
        # Exceptions 
        if element == 'ResultCollector':
            message = f"{enabledCount} Listener(s) enabled."
            printRed(message)
            recommendation = "Consider disabling Listeners."
            addRecommendation(recommendation)
        elif element == 'ResponseAssertion':
            message = f"{enabledCount} Response Assertion(s) are enabled."
            printRed(message)
            recommendation = "Consider disabling Response Assertions."
            addRecommendation(recommendation)
        elif element == 'DebugSampler':
            message = f"{enabledCount} Debug Sampler(s) are enabled."
            printRed(message)
            recommendation = "Consider disabling Debug Samplers."
            addRecommendation(recommendation)
        elif element == 'ProxyControl':
            message = f"{enabledCount} HTTP(S) Script Recorder(s) are enabled."
            printRed(message)
            recommendation = "Consider disabling HTTP(S) Script Recorder(s)."
            addRecommendation(recommendation)
        elif element == 'BeanShellSampler':
            message = f"{enabledCount} Bean Shell Sampler(s) are enabled."
            printRed(message)
            recommendation = "Consider using JSR223 Sampler."
            addRecommendation(recommendation)
        else:
            printGreen(message)
    if flag == 0:
        # Exception 
        if element == 'ResultCollector':
            message = f"{enabledCount} Listener(s) are enabled."
            printGreen(message)            
        elif element == 'ResponseAssertion':
            message = f"{enabledCount} Response Assertion(s) are enabled."
            printGreen(message)
        elif element == 'DebugSampler':
            message = f"{enabledCount} Debug Sampler(s) are enabled."
            printGreen(message)
        elif element == 'ProxyControl':
            message = f"{enabledCount} HTTP(S) Script Recorder(s) are enabled."
            printGreen(message)
        elif element == 'BeanShellSampler':
            message = f"{enabledCount} Bean Shell Sampler(s) are enabled."
            printGreen(message)
        else:
            printRed(message)
    return

def countNode(root,element):
    '''
    This function returns the count of the node.
    '''
    count = 0
    for node in root.iter(element):
        count += 1
    return count

def findThreadGroups(jmx):
    '''
    This function find the number of thread groups.
    '''
    tree = ET.parse(jmx)
    root = tree.getroot()
    element = 'ThreadGroup'
    enabledCount = 0

    for node in root.iter(element):
        #Find Enabled Thread Group
        if str.__contains__(str(node.attrib),'\'enabled\': \'true\''):            
            #Find enabled count
            enabledCount += 1
            #Set flag for success
            flag=1
            message=f"Total number of Thread Groups enabled {enabledCount}"
        else:
            message="No thread groups enabled."
            #Set flag for fail
            flag=0
    if flag == 1:
        printGreen(message)
    if flag == 0:
        printRed(message)    
        recommendation = "Consider enabling one or more Thread Groups."
        addRecommendation(recommendation)
    return

def findJMeterVersion(jmx):
    '''
    This function find the JMeter version.
    '''
    tree = ET.parse(jmx)
    # Get JMeter version
    root = tree.getroot()    
    jmeterversion = root.items()
    #Call JMeter Version
    expectedJMeterVersion = getJMeterVersion()
    #Check JMeter Version
    if expectedJMeterVersion == jmeterversion[2][1]:
        message=f"JMeter version is {jmeterversion[2][1]}."
        printGreen(message)
    else:
        message=f"Found outdated JMeter version: {jmeterversion[2][1]}."
        printRed(message)
        recommendation = "Consider updating to the latest version of JMeter."
        addRecommendation(recommendation)
    return

def getJMeterVersion():
    '''
    This function reads the expected JMeter version from the config file.
    '''
    #Read Config yaml
    with open('./config.yaml','r') as file:
        try:
            elements=yaml.safe_load(file)            
        except yaml.YAMLError as e:
            print(e)
    #Return JMeter Version
    return str(elements['JMeter']['version'])



def validateTestPlan(jmx):
    '''
    This function validates the JMeter test plan.
    '''
    try:
        element=XD.parse(jmx)
        message="Valid JMeter Test Plan"
        printGreen(message)

    except:
        message="Invalid test plan. Please use the valid JMeter test plan. \n"
        printRed(message)
        exit(1)    
    return