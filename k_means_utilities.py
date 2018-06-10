# -*- coding: utf-8 -*-
"""
Created on Tue May 29 22:54:46 2018

@author: NILESH
"""

# -*- coding: utf-8 -*-
"""
Created on Sun May 27 22:58:21 2018

@author: NILESH
"""
import numpy
from random import randrange

def assign_clusters_to_data_points(current_round, number_of_clusters,cluster_means,data):
    try:
        lenght_of_data = len(data)
        data_assignment_cluster = []
        over_all_error = 0
        for i in range(0,lenght_of_data):
            current_minimum = 999999999999
            nearest_cluster = 0
            for j in range(0,number_of_clusters):
                distance = 0
                distance = numpy.sqrt(numpy.sum(numpy.square(data[i] - cluster_means[j])))
                if(distance < current_minimum):
                    current_minimum = distance
                    nearest_cluster = j
            over_all_error = over_all_error + distance
            data_assignment_cluster.append(nearest_cluster)
        print('Current over all error of round:', current_round, 'is:', over_all_error)
        return numpy.array(data_assignment_cluster)    
    except Exception:
        print('Issue while assigning clusters to data points')
            
 

def calculate_new_mean_for_clusters(number_of_clusters, data, assignment_array):
    try:
        lenght_of_data, features = data.shape
        new_mean_array = numpy.zeros((number_of_clusters,features),dtype=numpy.float64)
        per_cluster_datapoints = numpy.zeros((1,number_of_clusters),dtype=numpy.float64)
        for i in range(0,lenght_of_data):
            cluster_index = int(assignment_array[i])
            per_cluster_datapoints[0][cluster_index] = per_cluster_datapoints[0][cluster_index] + 1
            new_mean_array[cluster_index] = numpy.add(new_mean_array[cluster_index], data[i])
        for i in range(0,number_of_clusters):
            new_mean_array[i] = numpy.divide(new_mean_array[i],per_cluster_datapoints[0][i])
        return new_mean_array
    except Exception:
        print('Issue while calculating mean for the clusters')
    


def k_means_plus_plus_for_cluster_initalization(data, number_of_clusters):
    try:
        number_of_instances, number_of_features = data.shape
        random_index = randrange(0,len(data)-1)
        skip_index_while_calulating_distances = []
        skip_index_while_calulating_distances.append(random_index)
        clusters = []        
        clusters.append(data[random_index])
        for cluster_index in range(1,number_of_clusters):
            probablity_distribution_array = []
            for i in range(0,number_of_instances):
                current_cluster_lenght = len(clusters)
                min_nearest_cluster_distace = 99999999999
                if(numpy.sum(numpy.equal(skip_index_while_calulating_distances,i)) == 0):
                    for j in range(0,current_cluster_lenght):
                        distance = numpy.sqrt(numpy.sum(numpy.square(data[i] - clusters[j])))
                        if(distance < min_nearest_cluster_distace):
                            min_nearest_cluster_distace = distance
                    probablity_distribution_array.append([i,min_nearest_cluster_distace])        
            next_cluster_index = get_next_cluster_index(probablity_distribution_array)
            skip_index_while_calulating_distances.append(next_cluster_index)
            clusters.append(data[next_cluster_index])
        return numpy.array(clusters)   
    except Exception:
        print('Issue while finding seeds for clusters')

#we can use different fintness function. Here we will use max function for simplicity
def get_next_cluster_index(probablity_distribution_array):
    try:
        probablity_array = numpy.array(probablity_distribution_array)
        total_variation_accross_clusters = numpy.sum(probablity_array.T[1])
        distribution_array = numpy.divide(probablity_array.T[1],total_variation_accross_clusters) 
        index_of_instance_with_max_prob = numpy.argmax(distribution_array)
        next_cluster_index = probablity_array.T[0][index_of_instance_with_max_prob]
        return int(next_cluster_index)
    except Exception:
        print('Issue while getting index of the next cluster')
    