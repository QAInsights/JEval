import logging
from colorit import *
from utils.ascii_icons import Icon


def print_message(message_color, message):
    """
    Prints message in a specific color
    """
    if message_color is Colors.green:
        icon = Icon.CHECK_MARK.value
    elif message_color is Colors.red:
        icon = Icon.RED_X.value
    elif message_color is Colors.white:
        icon = f" {Icon.INFO.value}"
    else:
        icon = Icon.EMPTY.value

    print(color(f"{icon} {message}", message_color))
    logging.basicConfig(filename='tmp.log', format='%(levelname)s %(asctime)s :: %(message)s', level=logging.DEBUG)
    logging.info(f"{message}")