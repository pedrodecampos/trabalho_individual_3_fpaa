import networkx as nx
import matplotlib.pyplot as plt
from main import Grafo

def visualizar_grafo(grafo, caminho=None):
    G = nx.Graph()
    
    # Adiciona vértices
    for i in range(grafo.vertices):
        G.add_node(i)
    
    # Adiciona arestas
    for i in range(grafo.vertices):
        for j in range(i+1, grafo.vertices):
            if grafo.grafo[i][j] == 1:
                G.add_edge(i, j)
    
    # Configura o layout
    pos = nx.spring_layout(G)
    
    # Desenha o grafo
    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', 
            node_size=500, font_size=16, font_weight='bold')
    
    # Se houver um caminho hamiltoniano, destaca-o
    if caminho:
        edges = [(caminho[i], caminho[i+1]) for i in range(len(caminho)-1)]
        nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='red', width=2)
    
    plt.title("Grafo com Caminho Hamiltoniano")
    plt.savefig('assets/grafo.png')
    plt.close()

if __name__ == "__main__":
    # Cria o mesmo grafo do exemplo
    g = Grafo(5)
    g.adicionar_aresta(0, 1)
    g.adicionar_aresta(0, 3)
    g.adicionar_aresta(1, 2)
    g.adicionar_aresta(1, 3)
    g.adicionar_aresta(1, 4)
    g.adicionar_aresta(2, 4)
    g.adicionar_aresta(3, 4)
    
    # Encontra o caminho hamiltoniano
    caminho = g.encontrar_caminho_hamiltoniano()
    
    # Visualiza o grafo
    visualizar_grafo(g, caminho) 