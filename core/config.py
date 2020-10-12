import yaml
import json
import os
from core.engine import print_message, Colors

config = None
custom_plugin_mappings = None


def load():
    """
    Loads config.yaml configuration into config variable
    """
    global config
    with open('config.yaml') as file:
        try:
            # Reading Config file and parsing JMX (once)
            config = yaml.safe_load(file)
        except yaml.YAMLError as e:
            print_message(message_color=Colors.red, message=e)


def load_plugin_mappings():
    """
    Loads custom Jmeter plugin mappings from a json file
    and sets to a global variable
    """
    global custom_plugin_mappings
    filename = 'plugin-mappings.json'

    if not (isinstance(filename, str) and os.path.exists and os.path.isfile(filename)):
        return None

    with open(filename, 'rb') as mapping_file:
        data = json.loads(mapping_file)

    if not isinstance(data, dict):
        raise MalformedDataError()

    custom_plugin_mappings = data

    return None


class MalformedDataError(Exception):
    pass

