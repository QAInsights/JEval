import logging
from colorit import *


def print_green(message):
    """
    Prints if the JMeter test plan passes a check.
    """
    print(color(f"\u2713 {message}", Colors.green))
    logging.basicConfig(filename='tmp.log', format='%(levelname)s %(asctime)s :: %(message)s', level=logging.DEBUG)
    logging.info(f"{message}")


def print_red(message):
    """
    Prints if the JMeter test plan fails a check.
    """
    print(color(f"\u2718 {message}", Colors.red))
    logging.basicConfig(filename='tmp.log', format='%(levelname)s %(asctime)s :: %(message)s', level=logging.DEBUG)
    logging.info(f"{message}")


def add_recommendation(recommendation):
    """
    Adds the recommendation.
    """
    print(f"Recommendation: {recommendation}")
    logging.basicConfig(filename='tmp.log', format='%(levelname)s %(asctime)s :: %(message)s', level=logging.DEBUG)
    logging.info(f"{recommendation}")
