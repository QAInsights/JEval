from jmx import *

def main():
    try:
        #jmxFile = str(sys.argv)
        #print(str(sys.argv[1]))
        #print(f"JMeter file is {jmxFile}")
        # Open file
        jmx = "./jmx/Sample.jmx"
        with open(jmx,'r') as f:
            parseJMX(jmx)
        f.close()
       
    except FileNotFoundError:
        print("File Not Found")

if __name__ == "__main__":
    main()