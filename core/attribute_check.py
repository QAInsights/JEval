from utils.display import print_message, Colors
import logging

def attribute_check(tree, element):
    """
    Performs additional attribute checks on IfController or LoopController
    @param tree: The parsed JMX
    @param element: The element to check
    """
    root = tree.getroot()
    # Set flag = 1 for issue found
    flag = 0
    
    for node in root.iter(element):
        try:
            for child in node.getchildren():    
                for i, j in child.attrib.items():
                    print(i, j)
                    if str(j) == 'IfController.useExpression':
                        # Set flag = 0 for no issues
                        flag = 0
                    elif str(j) == 'LoopController.loops':
                        loop_count = child.text
                        if int(loop_count) == -1:
                            flag = 0
                    else:
                        flag = 1
        except AttributeError:
            if element == 'LoopController':
                print_message(message_color=Colors.red, message="Loop Controller is empty.")
                logging.basicConfig(filename='tmp.log', format='%(levelname)s %(asctime)s :: %(message)s', level=logging.DEBUG)
                
    if flag == 1:
        if element == 'IfController':
            print_message(message_color=Colors.white, message="For performance, check \"Interpret Condition as Variable"
                                                            " Expression\" in If Controller.")
        elif element == 'LoopController':
            print_message(message_color=Colors.white, message="Loop Count is set to infinity. Double check "
                                                            "the count before you start the test.")
