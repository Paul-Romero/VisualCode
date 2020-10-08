import networkx as nx
import matplotlib.pyplot as plt

def bfs_shortes_path(grafo, inicio, meta):
    explorado = []
    cola = [[inicio]]
    if inicio == meta:
        return "Inicio = meta"
    while cola:
        ruta = cola.pop(0)
        nodo = ruta[-1]
        if nodo not in explorado:
            #explorado.append(nodo)
            vecinos = grafo[nodo]
            for vecino in vecinos:
                new_ruta = list(ruta)
                new_ruta.append(vecino)
                cola.append(new_ruta)
                if vecino == meta:
                    return new_ruta
            explorado.append(nodo)
    return "Esa conexión no existe!"

grafo = nx.DiGraph()
grafo.add_nodes_from(['A','B','C','D','E','F','G','H','I'])
grafo.add_edges_from([('A','B'),('A','E'),('B','D'),('E','C'),('D','G'),('C','G'),('C','I'),('I','F'),('I','H')])
nx.draw(grafo, with_labels=True, font_weight='bold')
print(bfs_shortes_path(grafo,'A','H'))
plt.show()