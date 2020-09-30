import logging
from colorit import *
from utils.ascii_icons import Icons


def print_message(message_color, message):
    """
    Prints message in a specific color
    """
    if message_color is Colors.green:
        icon = Icons.CHECK_MARK.value
    elif message_color is Colors.red:
        icon = Icons.RED_X.value
    elif message_color is Colors.white:
        icon = f" {Icons.INFO.value}"
    else:
        icon = Icons.NONE.value

    print(color(f"{icon} {message}", message_color))
    logging.basicConfig(filename='tmp.log', format='%(levelname)s %(asctime)s :: %(message)s', level=logging.DEBUG)
    logging.info(f"{message}")
