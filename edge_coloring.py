# https://networkx.org/documentation/latest/tutorial.html
# https://www.tutorialspoint.com/colouring-the-edges-by-weight-in-networkx-matplotlib#:~:text=To%20color%20the%20edges%20by%20weight%20in%20networkx%2C,graph%27s%20edges%20and%20set%20some%20weight%20to%20them.
# https://www.tutorialspoint.com/how-to-use-an-update-function-to-animate-a-networkx-graph-in-matplotlib
import matplotlib.pyplot as plt
import networkx as nx
import random as rd


plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

G = nx.DiGraph()
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)])
for u, v, d in G.edges(data=True):
   d['weight'] = rd.random()
edges, weights = zip(*nx.get_edge_attributes(G, 'weight').items())
nx.draw(G, node_color='b', edge_color=weights, width=2, with_labels=True)

plt.show()
