import sys
import csv
import pdb
import math
import random
import numpy as np
from sklearn.cluster import KMeans
from sklearn import svm

def main(argv, argc):
    if (argc < 2):
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
    print("Initial randomly selected centroids:")
    print("- Centroid 1:\t(" + str(centroid_1[0]) + ", " + str(centroid_1[1]) + ")")
    print("- Centroid 2:\t(" + str(centroid_2[0]) + ", " + str(centroid_2[1]) + ")")

    centroid_1_group = []
    centroid_2_group = []

    iterations = 10
    for iteration in range(0, iterations):
        centroid_1_group, centroid_2_group = compute_closeness(centroid_1, centroid_2, features)
        og_centroid_1 = centroid_1
        og_centroid_2 = centroid_2

        centroid_1 = compute_centroid_means(centroid_1_group)
        centroid_2 = compute_centroid_means(centroid_2_group)
        print("\nResults for Iteration " + str(iteration + 1) + ":")
        print("Group 1 (with centroid (" + str(og_centroid_1[0]) + ", " + str(og_centroid_1[1]) + "))" + ":")
        print_cluster(centroid_1_group)
        print("Group 2 (with centroid (" + str(og_centroid_2[0]) + ", " + str(og_centroid_2[1]) + "))" + ":")
        print_cluster(centroid_2_group)
        print("- New Centroid 1: (" + str(centroid_1[0]) + ", " + str(centroid_1[1]) + ")")
        print("- New Centroid 2: (" + str(centroid_2[0]) + ", " + str(centroid_2[1]) + ")")


def print_cluster(cluster):
    for c in cluster:
        print("\t(" + str(c[0]) + ", " + str(c[1]) + ")")


# I had no idea what to call this function
def compute_closeness(centroid_1, centroid_2, features):
    centroid_1_group, centroid_2_group = [], []
    for i in features:
        # compute distance formula for both centroids
        v1 = (centroid_1[0] - (i[0])) ** 2
        v2 = (centroid_1[1] - (i[1])) ** 2
        c1 = math.sqrt(v1 + v2)

        v1 = (centroid_2[0] - (i[0])) ** 2
        v2 = (centroid_2[1] - (i[1])) ** 2
        c2 = math.sqrt(v1 + v2)

        if c1 > c2:
            centroid_1_group.append(i)
        else:
            centroid_2_group.append(i)
    return centroid_1_group, centroid_2_group


def compute_centroid_means(centroid_group):
    # recompute location of centroids by finding their means by their respective lists

    xSum = 0.0
    ySum = 0.0
    count = float(len(centroid_group))
    for cg in centroid_group:
        xSum += cg[0]
        ySum += cg[1]
    return (xSum / count), (ySum / count)



def get_data(file):
    fileContents = csv.reader(file, delimiter=',')
    
    features = []
    for row in fileContents:
        features.append( [float(row[0]), float(row[1])] )
    return features



if __name__ == "__main__":
    main(sys.argv, len(sys.argv))
