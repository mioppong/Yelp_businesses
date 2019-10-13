import csv
import sys
import pandas as pd
import numpy as np
from collections import defaultdict
import argparse







def command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="csv file")
    parser.add_argument("city", help="city of choice")
    args = parser.parse_args()
    filename = args.filename
    city = args.city
    
    print(city,filename)

def main():
        #count_business()
        #dealing_with_args()
        command_line_args()


if __name__ == "__main__":
    main()