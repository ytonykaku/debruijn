import itertools as it
import networkx as nx
import matplotlib.pyplot as plt


def main():
    graph = open("graph.txt")
    G = nx.DiGraph()
    x = 0

    for line in graph.readlines():
        if x == 0:
            symbolSize, alphabetSize = line.split()
        else:
            alphabet = list(line.split(' '))
        x += 1

    permutationList = list(it.product((alphabet), repeat = int(symbolSize)-1))
    debruijngraph = makeGraph(permutationList)

    options = {
        "font_size": 36,
        "node_size": 3000,
        "node_color": "white",
        "edgecolors": "black",
        "linewidths": 5,
        "width": 5,
    }
    nx.draw_networkx(debruijngraph, **options)
#    plt.show()

    debruijnPath = list(nx.eulerian_circuit(debruijngraph))
    sequency = ''
    for permutation in debruijnPath:
        firstPos = permutation[0]
        firstPos = firstPos[:1]
        sequency += firstPos
    print (sequency)
#    print(debruijnPath)

def makeGraph(permutationList):
    G = nx.DiGraph()
    for permutation1 in permutationList:
        aux = permutation1
        aux = aux[1:]
        for permutation2 in permutationList:
            aux2 = permutation2
            aux2 = aux2[:-1]
            if aux == aux2:
                node_a = ''
                node_b = ''
                for symbols in permutation1:
                    node_a += symbols
                for symbols in permutation2:
                    node_b += symbols
                G.add_node(node_a)
                G.add_node(node_b)
                G.add_edge(node_a, node_b)
    return G

main()