import sys
import csv
import pdb
import numpy as np
from sklearn.cluster import KMeans
from sklearn import svm

def main(argv, argc):
    if (argc < 1):
        print("Usage: python main.py <dataset>")
        return 1

    file_a = open(argv[1], "r")
    features  = get_data(file_a)

def get_data(file):
    fileContents = csv.reader(file, delimiter=',')
    
    data = []
    for row in fileContents:
        pdb.set_trace()
        data.append( [float(row[0]), float(row[1])] )
    return data



if __name__ == "__main__":
    main(sys.argv, len(sys.argv))
