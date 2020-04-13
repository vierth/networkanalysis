import networkx as nx
import matplotlib.pyplot as plt

# helper function to load data in from file
def get_data(filename):
    # use a context manager to load in the data
    with open(filename, 'r', encoding='utf8') as rf:
        # transform file into string and split along new line
        lines = rf.read().split("\n")

        # separate each line along the tab characters
        data = [line.split("\t") for line in lines]

        # grab the header
        header = data[0]

        # delete header from data
        data = data[1:]
    
    # return header and data
    return header, data

# load data in from file
node_header, node_data = get_data('nodes.tsv')
edge_header, edge_data = get_data('edges.tsv')

# create graph object
G = nx.Graph()

# add node information to the graph
for node in node_data:
    # add nodes one by one, with id, name, chinese name, and index year
    G.add_node(int(node[0]), name=node[1], cname=node[2], indexyear=int(node[3]))

# add edge information to the graph
for edge in edge_data:
    # add edge one by one, node 1, node 2, kin, and label
    G.add_edge(int(edge[0]), int(edge[1]), kin=edge[2], label=edge[3])

# metrics
degree_centrality = nx.degree_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)

# visualize this
nx.draw_spring(G)
plt.show()