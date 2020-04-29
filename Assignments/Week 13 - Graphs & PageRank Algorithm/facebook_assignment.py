from concurrent.futures import ProcessPoolExecutor
from webget import download
import networkx as nx
import gzip
import numpy as np
import os
import warnings
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout, write_dot
import pygraphviz


filename = "facebook_combined.txt.gz"


def download_facebook_file():
    download_link = "https://snap.stanford.edu/data/facebook_combined.txt.gz"

    shouldDownload = True

    if os.path.isfile(filename):
        print("File exists")
    else:
        download(download_link, filename)


download_facebook_file()

with gzip.open(filename, "r") as f:
    print(f"Reading file")
    graph = nx.read_edgelist(f)

print()
print()



print(nx.info(graph))

deg_vec = np.array([graph.degree(n) for n in graph.nodes()])

max_ind_deg = deg_vec.max()

index_name = list(graph.nodes())[np.argmax(deg_vec)]
print(
    "Node {} has the most connections with {} connections".format(
        index_name, len(list(graph.neighbors(index_name)))
    )
)

print()
print()

nx.draw(
    graph,
    pos=graphviz_layout(graph),
    node_size=1,
    width=0.05,
    cmap=plt.cm.Blues,
    with_labels=False,
    node_color=range(len(graph)),
)
plt.show()

# commented out for performance enhancement.
# bash
# conda install -y networkx
# conda install -c anaconda pygraphviz


# def draw_graph(graph):
#     nx.draw(
#         graph,
#         pos=graphviz_layout(graph),
#         node_size=30,
#         width=0.05,
#         cmap=plt.cm.Blues,
#         with_labels=True,
#         node_color=range(len(graph)),
#     )


# graph = create_graph()
# draw_graph(graph)
# nx.draw(graph)

# nx.write_gml(graph, './social_network.gml')


# in_deg_vec = np.array([graph.in_degree(n) for n in graph.nodes()])
# print(in_deg_vec)
# in_deg_vec.max()  
# print(np.argmax(in_deg_vec))
# idx = np.argmax(in_deg_vec)  
# print(graph.nodes[idx]["name"])
