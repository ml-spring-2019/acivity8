import sys
import csv
import pdb
import numpy as np
from sklearn.cluster.KMeans
from sklearn import svm

def main(argv, argc):
    if (argc < 1):
        print("Usage: python main.py <dataset>")
        return 1

    file_a = open(argv[1], "r")
    features, result = get_data(file_a)

def get_data(file):
    fileContents = csv.reader(file)
    
    features = []
    result = []
    for row in fileContents:
        features.append( [float(row[0]), float(row[1])] )
        result.append(int(row[2]))
    
    return features, result



if __name__ == "__main__":
    main(sys.argv, len(sys.argv))
