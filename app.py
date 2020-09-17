import argparse
import sys
import fileinput

def main():
    try:
        jmxFile = str(sys.argv)
        print(str(sys.argv[1]))
        print(f"JMeter file is {jmxFile}")
        # Open file
        with open('C:\\Gits\\jeval\\jmx\\Sample.jmx','r') as f:
            print(f.read())
        f.close()
        #if str(jmxFile.__contains__("jmx")):
        #    print("Yes")

        
    except FileNotFoundError:
        print("File Not Found")

if __name__ == "__main__":
    main()