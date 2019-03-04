import sys
import csv
import pdb
import math
import random
import numpy as np
from sklearn.cluster import KMeans
from sklearn import svm

def main(argv, argc):
    if (argc < 1):
        print("Usage: python main.py <dataset>")
        return 1

    file_a = open(argv[1], "r")
    features  = get_data(file_a)
    k_means_cluster(2, features)
#pdb.set_trace()

def find_centroid(features):
    centroid_1 = random.choice(features)
    while (True):
        centroid_2 = random.choice(features)
        if centroid_2 != centroid_1:
            break
    return (centroid_1, centroid_2)

def k_means_cluster(cluster_amount, features):
    (centroid_1, centroid_2) = find_centroid(features)
    centroid_1_group, centroid_2_group = [], []
    for i in features:
# compute distance formula for both centroids
        v1 = (centroid_1[0]-(i[0]))**2
        v2 = (centroid_1[1]-(i[1]))**2
        c1 = math.sqrt(v1 + v2)
        
        v1 = (centroid_2[0]-(i[0]))**2
        v2 = (centroid_2[1]-(i[1]))**2
        c2 = math.sqrt(v1 + v2)
        
        if c1 > c2:
            centroid_1_group.append(i)
        else:
            centroid_2_group.append(i)

# recompute location of centroids by finding their means by their respective lists


def get_data(file):
    fileContents = csv.reader(file, delimiter=',')
    
    features = []
    for row in fileContents:
        features.append( [float(row[0]), float(row[1])] )
    return features



if __name__ == "__main__":
    main(sys.argv, len(sys.argv))
