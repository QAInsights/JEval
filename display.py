import logging
from colorit import *

def printGreen(message):
    '''
    This function will print if the JMeter test plan passes a check.
    '''
    print(color(f"\u2713 {message}", Colors.green))
    logging.basicConfig(filename='tmp.log',format='%(levelname)s %(asctime)s :: %(message)s',level=logging.DEBUG)
    logging.info(f"{message}")

    return

def printRed(message):
    '''
    This function will print if the JMeter test plan fails a check.
    '''
    print(color(f"\u2718 {message}", Colors.red))
    logging.basicConfig(filename='tmp.log',format='%(levelname)s %(asctime)s :: %(message)s',level=logging.DEBUG)
    logging.info(f"{message}")
    return

def addRecommendation(recommendation):
    '''
    This functions adds the recommendation.
    '''
    print(f"Recommendation: {recommendation}")   
    logging.basicConfig(filename='tmp.log',format='%(levelname)s %(asctime)s :: %(message)s',level=logging.DEBUG)
    logging.info(f"{recommendation}") 
    return