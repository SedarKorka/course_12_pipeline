# import the modules
import urllib.request
import networkx as nx
import numpy as np 
import matplotlib.pyplot as plt
import os
import sys


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

# Specify the output file name
output_file_name = "output.txt"

# Open the file in write mode
with open(output_file_name, "w") as output_file:
    # Redirect the standard output to the file
    sys.stdout = output_file

    # Get the number of nodes and edges in the Facebook-Ego network
    facebook_num_nodes = len(facebook_network.nodes())
    facebook_num_edges = len(facebook_network.edges())

    # Get the number of nodes and edges in the Twitter-Ego network
    twitter_num_nodes = len(twitter_network.nodes())
    twitter_num_edges = len(twitter_network.edges())

    # Print the results for Facebook-Ego network
    print("For Facebook-Ego Network:")
    print("The number of nodes is: ", facebook_num_nodes)
    print("The number of edges is: ", facebook_num_edges)

    # Print the results for Twitter-Ego network
    print("\nFor Twitter-Ego Network:")
    print("The number of nodes is: ", twitter_num_nodes)
    print("The number of edges is: ", twitter_num_edges)

# Reset the standard output
sys.stdout = sys.__stdout__

print(f"Results saved to {output_file_name}")
