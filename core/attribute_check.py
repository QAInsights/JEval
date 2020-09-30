from xml.etree.ElementTree import parse
from core.display import *


def attribute_check(tree, element):
    """
    Performs additional attribute checks on a few elements
    @param tree: The parsed JMX
    @param element: The element to check
    """
    root = tree.getroot()
    # Set flag = 1 for issue found
    flag = 0
    for node in root.iter(element):
        #
        for child in node.getchildren():
            for i, j in child.attrib.items():
                # print(i, j)
                if str(j) == 'IfController.useExpression':
                    # Set flag = 0 for no issues
                    flag = 0
                elif str(j) == 'LoopController.loops':
                    loop_count = child.text
                    if int(loop_count) == -1:
                        # print(f'Loop count {loop_count}')
                        flag = 0
                else:
                    flag = 1
        # if element == "LoopController":
        # print("Loop")
    if flag == 1:
        if element == 'IfController':
            message = "For performance, check \"Interpret Condition as Variable Expression\" in If Controller."
            add_recommendation(message)
        elif element == 'LoopController':
            message = "Loop Count is set to infinity. Double check the count before you start the test."
            add_recommendation(message)
