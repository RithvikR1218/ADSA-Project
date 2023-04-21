import toyplot

def kmer_set(sequence, k, cyclic):
    
    kmers = set()
    
    if k > len(sequence):
        print("Kmer length exceeds sequence length")
        return kmers
    if k <= 1:
        print("Kmer length cant be equal to 1")
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

def plot_graph(edges, width=500, height=500):    
    
    if len(edges) == 0:
        print("No graph is formed")
        return 
    
    graph = toyplot.graph(
        [i[0] for i in edges],
        [i[1] for i in edges],
        width=width,
        height=height,
        tmarker=">", 
        vsize=25,
        vstyle={"stroke": "white", "stroke-width": 2, "fill": "none"},
        vlstyle={"font-size": "11px", "stroke": "white"},
        estyle={"stroke": "white", "stroke-width": 2},
        layout=toyplot.layout.FruchtermanReingold(edges=toyplot.layout.CurvedEdges()))
    return graph