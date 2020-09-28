from xml.dom.minidom import parse

import yaml

from core.attribute_check import *
from core.display import *


def element_check(tree):
    """
    Checks for each element in JMeter
    @param tree: Parsed JMX file
    """
    with open('config.yaml') as file:
        try:
            # Reading Config file and parsing JMX (once)
            elements = yaml.safe_load(file)
            # Looping JMeter > Elements
            for element in elements['JMeter']['Elements']:
                # Calling Elements Check
                find_element_status(tree, element)
                if element == "IfController" or element == "LoopController":
                    attribute_check(tree, element)
        except yaml.YAMLError as e:
            print_red(message=e)


def find_element_status(tree, element):
    """
    Finds the element status for a specified element
    @param tree: Parsed JMX file
    @param element: Name of the element to check the status for
    """
    root = tree.getroot()
    enabled_count = 0
    flag = 0
    message = f"No element found for {element}."
    """
    #Elements to ignore if not found in the JMX Test Plan
    if element == 'XPath2Assertion' or element == 'JSONPathAssertion':
        message=f"Check ignored for {element}."
        printGreen(message)
    """
    for node in root.iter(element):
        if node.attrib is None:
            print_red(message=message)
        else:
            if str.__contains__(str(node.attrib), '\'enabled\': \'true\''):
                # Find enabled count
                enabled_count += 1
                # Set flag for success
                flag = 1
                message = "{enabled_count} {element}(s) enabled."
            else:
                message = f"No {element} enabled."
                # Set flag for fail
                flag = 0

    if flag == 1:
        # Exceptions
        if element == 'ResultCollector':
            print_red(message=f"{enabled_count} Listener(s) enabled.")
            add_recommendation(recommendation="Consider disabling Listeners.")

        elif element == 'ResponseAssertion':
            print_red(message=f"{enabled_count} Response Assertion(s) are enabled.")
            add_recommendation(recommendation="Consider disabling Response Assertions.")

        elif element == 'JSONPathAssertion':
            print_red(message=f"{enabled_count} JSON Path Assertion(s) are enabled.")
            add_recommendation(recommendation="Consider disabling JSON Path Assertions.")

        elif element == 'DebugSampler':
            print_red(message=f"{enabled_count} Debug Sampler(s) are enabled.")
            add_recommendation(recommendation="Consider disabling Debug Samplers.")

        elif element == 'ProxyControl':
            print_red(message=f"{enabled_count} HTTP(S) Script Recorder(s) are enabled.")
            add_recommendation(recommendation="Consider disabling HTTP(S) Script Recorder(s).")

        elif element == 'BeanShellSampler':
            print_red(message=f"{enabled_count} Bean Shell Sampler(s) are enabled.")
            add_recommendation(recommendation="Consider using JSR223 Sampler.")

        else:
            print_green(message=message)

    if flag == 0:
        # Exception
        if element == 'ResultCollector':
            print_green(message=f"{enabled_count} Listener(s) are enabled.")

        elif element == 'ResponseAssertion':
            print_green(message=f"{enabled_count} Response Assertion(s) are enabled.")

        elif element == 'JSONPathAssertion':
            print_green(message=f"{enabled_count} JSON Path Assertion(s) are enabled.")

        elif element == 'DebugSampler':
            print_green(message=f"{enabled_count} Debug Sampler(s) are enabled.")

        elif element == 'ProxyControl':
            print_green(message=f"{enabled_count} HTTP(S) Script Recorder(s) are enabled.")

        elif element == 'CookieManager':
            print_red(message=f"{enabled_count} CookieManager added.")
            add_recommendation(recommendation="Consider adding CookieManager.")

        elif element == 'CacheManager':
            print_red(message=f"{enabled_count} Cache Manager added.")
            add_recommendation(recommendation="Consider adding Cache Manager.")

        elif element == 'ConfigTestElement':
            print_red(message=f"{enabled_count} HTTP Request Defaults added.")
            add_recommendation(recommendation="Consider adding HTTP Request Defaults.")

        elif element == 'CSVDataSet':
            print_green(message=f"{enabled_count} CSV Data Set are added.")
            add_recommendation(recommendation="Consider adding CSV Data Set.")

        elif element == 'ConstantTimer':
            print_red(message=f"{enabled_count} Timers added.")
            add_recommendation(recommendation="Consider adding Timers.")

        elif element == 'BeanShellSampler':
            print_green(message=f"{enabled_count} Bean Shell Sampler(s) are enabled.")
            add_recommendation(recommendation="Consider using JSR223 Sampler.")

        elif element == 'HeaderManager':
            print_red(message=f"{enabled_count} Header Manager are enabled.")
            add_recommendation(recommendation="Consider adding Header Manager.")

        elif element == 'TestAction':
            print_red(message=f"{enabled_count} Test Action are enabled.")
            add_recommendation(recommendation="Consider adding Test Action.")

        else:
            # printRed(message)
            pass


def count_node(root, element):
    """
    Returns the count of the node
    @param root: the root element to count from
    @param element: the element to count to
    @return: the number of nodes as integer
    """
    count = 0
    for node in root.iter(element):
        count += 1
    return count


def find_thread_groups(tree):
    """
    Finds the number of thread groups
    @param tree: Parsed JMX file
    """
    with open('config.yaml') as file:
        try:
            # Reading Config file
            elements = yaml.safe_load(file)
            # Looping JMeter > Thread Group
            for element in elements['JMeter']['ThreadGroups']:
                find_thread_groups_status(tree, element)
        except yaml.YAMLError as e:
            print_red(message=e)


def find_thread_groups_status(tree, element):
    """
    Detects Thread Group and types. It reads from the config.yaml for the list of Thread Groups.
    @param tree: Parsed JMX file
    @param element: The name of the thread group to find
    @return:
    """
    root = tree.getroot()
    enabled_count = 0
    flag = 0
    message = f"No element found for {element}."
    for node in root.iter(element):
        if node.attrib:
            # Find Enabled Thread Groups
            if str.__contains__(str(node.attrib), '\'enabled\': \'true\''):
                # Find enabled count
                enabled_count += 1
                # Set flag for success
                flag = 1
                message = f"Total number of {element} enabled {enabled_count}"
            elif str.__contains__(str(node.attrib), '\'enabled\': \'false\''):
                message = f"No {element} enabled."
                # Set flag for fail
                flag = 0
        else:
            print_red(f"No {element} found.")
    if flag == 1:
        print_green(message=message)
        enabled_count = 0
    if flag == 0:
        print_red(message=message)
        add_recommendation(recommendation=f"Consider enabling one or more {element}.")
        enabled_count = 0
    return


def validate_jmeter_version(tree):
    """
    Finds the JMeter version
    @param tree: Parsed JMX file
    """
    # Get JMeter version
    root = tree.getroot()
    jmeter_version = root.items()
    expected_jmeter_version = get_jmeter_version()

    # Check JMeter Version
    if expected_jmeter_version == jmeter_version[2][1]:
        print_green(message=f"JMeter version is {jmeter_version[2][1]}.")
    else:
        print_red(message=f"Found outdated JMeter version: {jmeter_version[2][1]}.")
        add_recommendation(recommendation="Consider updating to the latest version of JMeter.")


def get_jmeter_version():
    """
    Reads the expected JMeter version from the config file.
    @return: the JMeter version as a string
    """
    # Read Config yaml
    with open('config.yaml') as file:
        try:
            elements = yaml.safe_load(file)
        except yaml.YAMLError as e:
            print(e)
    # Return JMeter Version
    return str(elements['JMeter']['version'])


def validate_test_plan(jmx):
    """
    validates the JMeter test plan
    @param jmx: The file path to the JMX
    """
    try:
        tree = parse(jmx)
        print_green(message="Valid JMeter Test Plan")
        return tree
    except:
        print_red(message="Invalid test plan. Please use the valid JMeter test plan. \n")
        exit(1)
