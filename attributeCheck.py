import xml.etree.ElementTree as ET
from display import *

def attributeCheck(jmx, element):
    '''
    This function perform additional attribute checks for the few elements.
    '''
    tree = ET.parse(jmx)
    root = tree.getroot()
    #Set flag = 1 for issue found
    flag = 0
    for node in root.iter(element):
        #
        for child in node.getchildren():            
            for i, j in child.attrib.items():
                #print(i, j)
                if str(j) == 'IfController.useExpression':
                    #Set flag = 0 for no issues
                    flag=0
                elif str(j) == 'LoopController.loops':
                    loopCount = child.text
                    if int(loopCount) == -1:
                        #print(f'Loop count {loopCount}')
                        flag=0
                else:
                    flag=1
        #if element == "LoopController":
            #print("Loopppp")
    if flag == 1:
        if element == 'IfController':
            message="For performance, check \"Interpret Condition as Variable Expression\" in If Controller."
            addRecommendation(message)
        elif element == 'LoopController':
            message="Loop Count is set to infinity. Double check the count before you start the test."
            addRecommendation(message)
                        
    return