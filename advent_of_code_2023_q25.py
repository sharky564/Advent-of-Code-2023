from math import prod
import networkx as nx


def part1():
    f = open("input.txt", 'r')
    out = f.read().split('\n')

    G = nx.Graph()
    for row in out:
        u, vs = row.split(':')
        for v in vs.split():
            G.add_edge(u, v)
    cuts = nx.minimum_edge_cut(G)
    G.remove_edges_from(cuts)
    print(prod(map(len, nx.connected_components(G))))
    

def part2():
    f = open("input.txt", 'r')
    out = f.read().split('\n')
    
    print("PUSH THAT BUTTON!")
                    

part1()
part2()