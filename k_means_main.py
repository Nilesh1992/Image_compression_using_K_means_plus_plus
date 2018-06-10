# -*- coding: utf-8 -*-
"""
Created on Sun May 27 22:57:38 2018

@author: NILESH
"""
import scipy.misc
import os
from PIL import Image
import numpy
import k_means_utilities
image_path = os.getcwd() + '\\my_pic.jpg'
image = Image.open(image_path)
image_pixels_raw = numpy.array(image,dtype=numpy.float64)
image_pixels = numpy.array(image.getdata(),dtype=numpy.float64)
number_of_clusters = 32
total_rounds = 1

#clusters_mean = numpy.array([[20,22,22], [255,255,251],
#[252,130,29],
#[98,115,198],
#[119,115,61],
#[203,188,144],
#[145,217,249],
#[49,61,121],
#[237,208,66],
#[197,115,103],
#[252,248,170],
#[96,41,35],
#[127,162,141],
#[173,108,6],
#[214,205,215],
#[254,147,117]])


all_instances, features = image_pixels.shape
for i in range(0,total_rounds):
    current_iteration = 0
    clusters_mean = k_means_utilities.k_means_plus_plus_for_cluster_initalization(image_pixels,number_of_clusters)
    print('Current K-means iteration is:',i)
    while True:
        current_iteration = current_iteration + 1
        assigned_clusters = k_means_utilities.assign_clusters_to_data_points(current_iteration, number_of_clusters,clusters_mean,image_pixels)
        new_means = k_means_utilities.calculate_new_mean_for_clusters(number_of_clusters,image_pixels,assigned_clusters)
        check_if_converged = numpy.sum(((numpy.equal(new_means,clusters_mean)))*1)
        if(check_if_converged == features):
            break
        clusters_mean = new_means

new_image_array = numpy.zeros(image_pixels_raw.shape,dtype=numpy.int)
length, width, channels = new_image_array.shape
for i in range(0,length):
    for j in range(0,width):
        mapped_index = int((length*i) + j)
        index_of_assigned_cluster = assigned_clusters[mapped_index]
        new_image_array[i][j] = numpy.array(clusters_mean[index_of_assigned_cluster],dtype=numpy.int)
        
 
scipy.misc.imsave('outfile_my_pic.jpg', new_image_array)