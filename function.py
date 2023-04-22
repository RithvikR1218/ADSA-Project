import matplotlib.pyplot as plt
import networkx as nx

def kmer_set(sequence, k, cyclic):
    
    kmers = set()
    
    if k > len(sequence):
        print("K-mer length exceeds sequence length")
        return kmers
    if k <= 1:
        print("K-mer length cant be equal to 1")
        return kmers
    
    for i in range(0, len(sequence)):
        kmer = sequence[i:i + k]
        length = len(kmer)
        if cyclic:
            if len(kmer) != k:
                kmer += sequence[:(k - length)]
        else:
            if len(kmer) != k:
                continue
        kmers.add(kmer)
    return kmers

def edge_set(kmers):
    edges = set()
    for k1 in kmers:
        for k2 in kmers:
            if k1 != k2:            
                if k1[1:] == k2[:-1]:
                    edges.add((k1[:-1], k2[:-1]))
                if k1[:-1] == k2[1:]:
                    edges.add((k2[:-1], k1[:-1]))
    return edges

def plot_debruijn_graph(edges, width=500, height=500):
    # Error handling
    if len(edges) == 0:
        print("No graph is formed")
        return

    G = nx.DiGraph()

    for edge in edges:
        G.add_edge(edge[0], edge[1])

    fig, ax = plt.subplots(figsize=(width/80, height/80))
    pos = nx.spring_layout(G, seed=42)

    nx.draw_networkx_nodes(G, pos, node_size=25, node_color="none", edgecolors="none", linewidths=2, ax=ax)

    nx.draw_networkx_edges(G, pos, edge_color="black", width=3, ax=ax, connectionstyle="arc3,rad=0.3")

    nx.draw_networkx_labels(G, pos, font_color="red",labels={node: node for node in G.nodes()}, font_size=15, ax=ax)

    ax.set_xlim([-1.2, 1.2])
    ax.set_ylim([-1.2, 1.2])

    ax.set_xticks([])
    ax.set_yticks([])

    plt.show()
