# import the modules
import urllib.request
import networkx as nx
import numpy as np 
import matplotlib.pyplot as plt
import os


#ENV FACEBOOK_URL="https://raw.githubusercontent.com/wang422003/Complex-Networks_exercise/main/Datasets/Group3/Facebook-Ego/348.edges"
#ENV TWITTER_URL="https://raw.githubusercontent.com/wang422003/Complex-Networks_exercise/main/Datasets/Group3/Twitter-Ego/789071.edges"
# Load the dataset
# Define the URL of the edge list file for the Facebook-Ego network
url_facebook = os.getenv('FACEBOOK_URL')  
# Download the Facebook-Ego network file
urllib.request.urlretrieve(url_facebook, "facebook.edges")
# Load the Facebook-Ego network (undirected graph)
facebook_network = nx.read_edgelist("facebook.edges", nodetype=int)

# Define the URL of the edge list file for the Twitter-Ego network
url_twitter = os.getenv('TWITTER_URL')  
# Download the Twitter-Ego network file
urllib.request.urlretrieve(url_twitter, "twitter.edges")
# Load the Twitter-Ego network (directed graph)
twitter_network = nx.read_edgelist("twitter.edges", nodetype=int, create_using=nx.DiGraph())


##Question a

# Get the number of nodes and edges in the Facebook-Ego network
facebook_num_nodes = len(facebook_network.nodes())
facebook_num_edges = len(facebook_network.edges())

# Get the number of nodes and edges in the Twitter-Ego network
twitter_num_nodes = len(twitter_network.nodes())
twitter_num_edges = len(twitter_network.edges())

# Print the results for Facebook-Ego network
 
print("Data save in the output.txt file")
f = open("/home/network/output/output.txt", "w")
f.write("For Facebook-Ego Network: \n")
f.write("The number of nodes is : %d \n" %facebook_num_nodes) 
f.write("The number of edges is : %d \n" %facebook_num_edges)

f.write("For Twitter-Ego Network: \n")
f.write("The number of nodes is : %d \n" %twitter_num_nodes) 
f.write("The number of edges is : %d \n" %twitter_num_edges)
f.close()