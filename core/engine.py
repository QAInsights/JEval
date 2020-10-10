from xml.etree import ElementTree
from core.attribute_check import *
from core import config as setup
from utils.display import print_message, Colors
from core.exceptions import Exceptions

def plugins_check(tree):
    """
    Checks for JMeter Plugins in JMeter
    @param tree: Parsed JMX file
    """
    
    for plugin in setup.config['JMeter']['Plugins']:
        if plugin == 'DummySampler':
            plugin_name = 'kg.apc.jmeter.samplers.DummySampler'
        if plugin == 'UDP':
            plugin_name = 'kg.apc.jmeter.samplers.UDPSampler'
        if plugin == 'SeleniumWebDriver':
            plugin_name = 'com.googlecode.jmeter.plugins.webdriver.sampler.WebDriverSampler'
        if plugin == 'Visualizer':
            plugin_name = 'kg.apc.jmeter.vizualizers.CorrectedResultCollector'
        detect_plugins(tree, plugin, plugin_name)

def detect_plugins(tree,plugin,plugin_name):
    """
    Detects each JMeter Plugins present in the test plan
    @param tree: Parsed JMX file
    @param element: Name of the element to check the status for
    """
    root = tree.getroot()
    enabled_count = 0
    flag = 0
    message = f"No plugin found for {plugin_name}."
    
    for node in root.iter(plugin_name):
        if str.__contains__(str(node.attrib), '\'enabled\': \'true\''):
            # Find enabled count
            enabled_count += 1
            # Set flag for success
            flag = 1
            message = f"{enabled_count} {plugin}(s) enabled."

    #print_message(message_color=Colors.green, message=message)
    Exceptions.check(plugin, flag, enabled_count, message)

def element_check(tree):
    """
    Checks for each element in JMeter
    @param tree: Parsed JMX file
    """
    # Looping JMeter > Elements
    for element in setup.config['JMeter']['Elements']:
        # Calling Elements Check
        find_element_status(tree, element)
        if element == "IfController" or element == "LoopController":
            attribute_check(tree, element)


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

    for node in root.iter(element):
        if node.attrib is None:
            print_message(message_color=Colors.red, message=message)
        else:
            if str.__contains__(str(node.attrib), '\'enabled\': \'true\''):
                # Find enabled count
                enabled_count += 1
                # Set flag for success
                flag = 1
                message = f"{enabled_count} {element}(s) enabled."
            else:
                message = f"No {element} enabled."
                # Set flag for fail
                flag = 0

    # print custom logs for exception elements
    Exceptions.check(element, flag, enabled_count, message)


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
    for element in setup.config['JMeter']['ThreadGroups']:
        find_thread_groups_status(tree, element)


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
            print_message(message_color=Colors.red, message=f"No {element} found.")
    if flag == 1:
        print_message(message_color=Colors.green, message=message)
        enabled_count = 0
    if flag == 0:
        print_message(message_color=Colors.red, message=message)
        print_message(message_color=Colors.white, message=f"Consider enabling one or more {element}.")
        enabled_count = 0
    return


def validate_test_plan(jmx):
    """
    validates the JMeter test plan
    @param jmx: The file path to the JMX
    """
    try:
        tree = ElementTree.parse(jmx)
        print_message(message_color=Colors.green, message="Valid JMeter Test Plan")
        return tree
    except:
        print_message(message_color=Colors.red, message="Invalid test plan. Please use the valid JMeter test plan. \n")
        exit(1)


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
        print_message(message_color=Colors.green, message=f"JMeter version is {jmeter_version[2][1]}.")
    else:
        print_message(message_color=Colors.red, message=f"Found outdated JMeter version: {jmeter_version[2][1]}.")
        print_message(message_color=Colors.white, message="Consider updating to the latest version of JMeter.")


def get_jmeter_version():
    """
    Reads the expected JMeter version from the config file.
    @return: the JMeter version as a string
    """
    return str(setup.config['JMeter']['version'])
