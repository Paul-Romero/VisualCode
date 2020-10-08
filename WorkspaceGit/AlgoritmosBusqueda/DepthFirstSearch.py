import networkx as nx
import matplotlib.pyplot as plt

grafo = nx.DiGraph()
grafo.add_nodes_from(['A','B','C','D','E','F','G','H','I'])
grafo.add_edges_from([('A','B'),('A','E'),('B','D'),('E','C'),('D','G'),('C','G'),('C','I'),('I','F'),('I','H')])

def dfs(grafo, start, visited, stack):
    if start in visited:
        return stack, visited
    if grafo.out_degree(start) == 0:
        stack.append(start)
        visited.append(start)
        return stack, visited
    for node in grafo.neighbors(start):
        if node in visited:
            continue
        stack, visited = dfs(grafo, node, visited, stack)
    if start not in visited:
        stack.append(start)
        visited.append(start)
    return stack, visited

nx.draw(grafo, with_labels=True, font_weight='bold')
topo_sort = nx.topological_sort(grafo)
print("Recorrido:")
for g in topo_sort: print(g, end=" -> ")
plt.show()