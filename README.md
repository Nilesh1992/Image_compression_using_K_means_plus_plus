# Image_compression_using_K_means_plus_plus
A approach to save space for storing image at the same time minmizing the overall run time for K-means using proper cluster initalization.

Problem in hand:
Given a color image with color space as RGB of size m×n, we have to minimize the space required as much as possible keeping the image visually similar to the original one. 

Approach:
1) One possible approcah is K-means, where K is the number of cluster centers. Which in our case can represent the colours for the pixels grouped in that clusters.
2) To make this method work effectively we have to make sure that the K-means algorithm converges as quickly as possible and at the same time scalable for lager images.
3) We all know that we have no way to know beforehand the value of K, and we also know the initial selection of the K centers gives different solutions and stuck in local minima.
4) For our approcah we can set K = 2,4,8,16,32...2^n, to tackle the problem of initail cluster selection we will use K-means++ algorithm which basically based on the assumption the it better to have the inintal cluster as much seperated as possible. The K-means++ algorithm first initial at random, then all the cluster henceforth is selected based on the probablity distribution of the points. Each point of selection as next cluster center depends on it probablity D(i) is the distance of the point to it's nearest cluster followed by normalization. Once the K cluster are selected then we can use our normal K-means.


