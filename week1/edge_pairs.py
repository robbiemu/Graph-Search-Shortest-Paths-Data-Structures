from collections import defaultdict

def preprocess_adjacency_directed_edge_pairs(data):
    res = defaultdict(list)
    for x,y in [tuple(map(int, edge.split())) for edge in data.split(b'\n')]:
        res[x].append(y)
    return dict(res)

def preprocess_directed_edge_pairs(data):
    return [tuple(map(int, edge.split())) for edge in data.split(b'\n')]
