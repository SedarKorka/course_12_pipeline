# import the modules
import urllib.request
import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt

#Load the dataset
# Define the URL of the edge list file for the Facebook-Ego network
url_facebook = input('Enter the facebook url\n')
#facebook_url = "https://raw.githubusercontent.com/wang422003/Complex-Networks_exercise/main/Datasets/Group3/Facebook-Ego/348.edges"
# Download the Facebook-Ego network file
urllib.request.urlretrieve(url_facebook, "facebook.edges")
# Load the Facebook-Ego network (undirect graph)
facebook_network = nx.read_edgelist("facebook.edges", nodetype=int)

# Define the URL of the edge list file for the Twitter-Ego network
url_twitter = input('Enter the twitter url\n')
#twitter_url = "https://raw.githubusercontent.com/wang422003/Complex-Networks_exercise/main/Datasets/Group3/Twitter-Ego/789071.edges"
# Download the Twitter-Ego network file
urllib.request.urlretrieve(url_twitter, "twitter.edges")
# Load the Twitter-Ego network (direct graph)
twitter_network = nx.read_edgelist("twitter.edges", nodetype=int, create_using=nx.DiGraph())


##Question a
# Get the number of nodes and edges in the Facebook-Ego network
facebook_num_nodes = len(facebook_network.nodes())
facebook_num_edges = len(facebook_network.edges())

# Get the number of nodes and edges in the Twitter-Ego network
twitter_num_nodes = len(twitter_network.nodes())
twitter_num_edges = len(twitter_network.edges())

# Print the results for Facebook-Ego network
print("For Facebook-Ego Network:")
print("The number of nodes is : ", facebook_num_nodes)
print("The number of edges is : ", facebook_num_edges)

# Print the results for Twitter-Ego network
print("For Twitter-Ego Network:")
print("The number of nodes is : ", twitter_num_nodes)
print("The number of edges is : ", twitter_num_edges)