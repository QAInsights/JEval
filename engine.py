JMETER_VERSION="5.3"
import xml.etree.ElementTree as ET
import argparse
import sys
import fileinput
import pdb
import yaml

from colorit import *

def elementCheck(jmx):
    with open('./elementCheck.yaml','r') as file:
        try:
            elements=yaml.safe_load(file)
            for i, k in elements.items():
                #print(i, k)
                for element in k:
                    #print(element)
                    findElementStatus(jmx,element)

        except yaml.YAMLError as e:
            print(e)
    return

def findElementStatus(jmx, element):
    tree = ET.parse(jmx)
    root = tree.getroot()
    #print(str(countNode(root,element)))
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
        # Exception for ResultCollector
        if element == 'ResultCollector':
            message = f"{enabledCount} Listener(s) enabled."
            printRed(message)
        elif element == 'ResponseAssertion':
            message = f"{enabledCount} Response Assertion(s) are enabled."
            printRed(message)
        elif element == 'DebugSampler':
            message = f"{enabledCount} Debug Sampler(s) are enabled."
            printRed(message)
        else:
            printGreen(message)
    if flag == 0:
        # Exception for ResultCollector
        if element == 'ResultCollector':
            message = f"{enabledCount} Listener(s) are enabled."
            printGreen(message)
        elif element == 'ResponseAssertion':
            message = f"{enabledCount} Response Assertion(s) are enabled."
            printGreen(message)
        elif element == 'DebugSampler':
            message = f"{enabledCount} Debug Sampler(s) are enabled."
            printGreen(message)
        else:
            printRed(message)

    return

def countNode(root,element):
    count = 0
    for node in root.iter(element):
        count += 1

    return count

def findThreadGroups(jmx):
    tree = ET.parse(jmx)
    root = tree.getroot()
    element = 'ThreadGroup'
    #print(str(countNode(root,element)))
    enabledCount = 0

    for node in root.iter(element):
        #Find Enabled Thread Group
        if str.__contains__(str(node.attrib),'\'enabled\': \'true\''):            
            #print(node.attrib)
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
    
    return

def findJMeterVersion(jmx):
    tree = ET.parse(jmx)
    # Get JMeter version
    root = tree.getroot()
    jmeterversion = root.items()
    #Check 00 - JMeter Version
    if JMETER_VERSION == jmeterversion[2][1]:
        message=f"JMeter version is {jmeterversion[2][1]}."
        printGreen(message)
    else:
        message=f"Found outdated JMeter version: {jmeterversion[2][1]}."
        printRed(message)
        recommendation = "Consider updating to the latest version of JMeter."
        addRecommendation(recommendation)
    return

def printGreen(message):
    '''
    This function will print if the JMeter test plan passes a check.
    '''
    print(color(f"\u2713 {message}", Colors.green))
    return

def printRed(message):
    '''
    This function will print if the JMeter test plan fails a check.
    '''
    print(color(f"\u2718 {message}", Colors.red))
    return

def addRecommendation(recommendation):
    print(f"Recommendation: {recommendation}\n")    
    return

'''
def validateListeners(jmx):
    tree = ET.parse(jmx)
    root = tree.getroot()
    #Check 10 - Listeners Enable or Disable
    #Find ResultCollector node(s) in the XML
    for tnode in root.iter('ThreadGroup'):
        for node in root.iter('ResultCollector'):
            if str.__contains__(str(node.attrib),'true'):
                print(node.attrib)

    return 
'''