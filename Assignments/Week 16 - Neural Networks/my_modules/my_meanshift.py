from sklearn.cluster import MeanShift, estimate_bandwidth
import argparse
import numpy as np 
# The bandwidth is the distance/size scale of the kernel function, i.e. 
# sklearn.cluster module offers an estimate_bandwith() function based on a nearest-neighbor analysis.
# quantile should be between [0, 1] 0.5 means that the median of all pairwise distances is used. 
# quantile 0.2 seems to give the best result here

def my_mean_shift(data, n_samples=1000, quantile=0.2):
    """takes data and fit it to meanshift model returns (labels, cluster centers, number of clusters"""
    bandwidth = estimate_bandwidth(data, quantile=quantile, n_samples=n_samples)

    ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
    ms.fit(data)
    labels = ms.labels_
    cluster_centers = ms.cluster_centers_

    labels_unique = np.unique(labels)
    n_clusters = len(labels_unique)

    print('Number of estimated clusters : {}'.format(n_clusters))
    
    return labels, cluster_centers, n_clusters

if __name__ == '__main__':
    print('this is a module to expose the meanshift function for use in other python code')