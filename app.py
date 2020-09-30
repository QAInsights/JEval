import argparse
import os
import time

from core.engine import print_message, Colors
from core.jmx import parse_jmx


def main():
    """
    The main context of the application
    """
    try:
        parser = argparse.ArgumentParser(
            description='Evaluate JMeter Test Plan'
        )
        required_named = parser.add_argument_group('mandatory arguments')
        required_named.add_argument(
            "-f",
            "--file",
            dest="jmxfile",
            help="Add JMeter Test Plan file path"
        )
        args = parser.parse_args()
        jmx = args.jmxfile
        with open(jmx) as f:
            parse_jmx(jmx)
            f.close()
    except FileNotFoundError as e:
        print_message(message_color=Colors.red, message=f"An error occured during JEval execution: "
                                                        f"{e.strerror} ({e.filename})")


if __name__ == "__main__":
    start_time = time.time()
    main()
    # Print Execution Time
    print("\033[93m \n\t Execution completed in %s seconds." % round(time.time() - start_time, 3))
    # Print Log file location
    print(f"\033[93m \t Log file is located in {os.curdir}/tmp.log")
