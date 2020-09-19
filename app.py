from jmx import *
from engine import printRed
from engine import printGreen
def main():
    try:
        #jmxFile = str(sys.argv)
        #print(str(sys.argv[1]))
        #print(f"JMeter file is {jmxFile}")
        
        # Open file        
        jmx = "./jmx/Sample.jmx"
        #Print file name
        with open(jmx,'r') as f:
            parseJMX(jmx)
        f.close()       
    except FileNotFoundError:
        printRed("Trouble in accessing JMeter file. Check for missing file and/or its permissions.")

if __name__ == "__main__":
    main()