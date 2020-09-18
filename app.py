import argparse
import sys
import fileinput
import xml.etree.ElementTree as ET
from colorit import *

JMETER_VERSION="5.3"
def main():
    try:
        #jmxFile = str(sys.argv)
        #print(str(sys.argv[1]))
        #print(f"JMeter file is {jmxFile}")
        # Open file
        jmx = "C:\\Gits\\jeval\\jmx\\Sample.jmx"
        with open(jmx,'r') as f:
            parseJMX(jmx)
        f.close()
       
    except FileNotFoundError:
        print("File Not Found")

def parseJMX(jmx):
    findJMeterVersion(jmx)
    validateListeners(jmx)
    return

def validateListeners(jmx):
    tree = ET.parse(jmx)
    root = tree.getroot()
    #Check 10 - Listeners Enable or Disable
    #Find ResultCollector node(s) in the XML
    for node in root.iter('ResultCollector'):
        if str.__contains__(str(node.attrib),'true'):
            print('Tes')

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

if __name__ == "__main__":
    main()