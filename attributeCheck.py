import xml.etree.ElementTree as ET
from display import *

def attributeCheck(jmx, element):
    '''
    This function perform additional attribute checks for the few elements.
    '''
    tree = ET.parse(jmx)
    root = tree.getroot()
    #Set flag = 1 for issue found
    flag = 1
    for node in root.iter(element):
        if element == 'IfController':
            for child in node.getchildren():
                #print(child.attrib)
                for i, j in child.attrib.items():
                    #print(i, j)                    
                    if str(j) == 'IfController.useExpression':
                        #Set flag = 0 for no issues
                        flag=0
                    else:
                        flag=1
    if flag == 1:
        message="For performance, check \"Interpret Condition as Variable Expression\" in If Controller."
        addRecommendation(message)       
                        
    return