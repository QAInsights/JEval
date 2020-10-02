import yaml
from core.engine import print_message, Colors

config = None


def load():
    global config
    with open('config.yaml') as file:
        try:
            # Reading Config file and parsing JMX (once)
            config = yaml.safe_load(file)
        except yaml.YAMLError as e:
            print_message(message_color=Colors.red, message=e)
