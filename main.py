class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * vertices for _ in range(vertices)]
    
    def adicionar_aresta(self, u, v):
        self.grafo[u][v] = 1
        self.grafo[v][u] = 1  # Para grafos não direcionados
    
    def eh_seguro(self, v, pos, caminho):
        # Verifica se o vértice v pode ser adicionado ao caminho
        if self.grafo[caminho[pos-1]][v] == 0:
            return False
        
        # Verifica se o vértice já está no caminho
        for vertice in caminho:
            if vertice == v:
                return False
        
        return True
    
    def caminho_hamiltoniano_util(self, caminho, pos):
        # Caso base: se todos os vértices estão no caminho
        if pos == self.vertices:
            return True
        
        # Tenta adicionar cada vértice ao caminho
        for v in range(self.vertices):
            if self.eh_seguro(v, pos, caminho):
                caminho[pos] = v
                
                if self.caminho_hamiltoniano_util(caminho, pos + 1):
                    return True
                
                caminho[pos] = -1
        
        return False
    
    def encontrar_caminho_hamiltoniano(self):
        caminho = [-1] * self.vertices
        
        # Começa do vértice 0
        caminho[0] = 0
        
        if not self.caminho_hamiltoniano_util(caminho, 1):
            print("Não existe caminho hamiltoniano")
            return None
        
        return caminho

# Exemplo de uso
if __name__ == "__main__":
    # Cria um grafo com 5 vértices
    g = Grafo(5)
    
    # Adiciona arestas
    g.adicionar_aresta(0, 1)
    g.adicionar_aresta(0, 3)
    g.adicionar_aresta(1, 2)
    g.adicionar_aresta(1, 3)
    g.adicionar_aresta(1, 4)
    g.adicionar_aresta(2, 4)
    g.adicionar_aresta(3, 4)
    
    # Encontra o caminho hamiltoniano
    caminho = g.encontrar_caminho_hamiltoniano()
    
    if caminho:
        print("Caminho Hamiltoniano encontrado:")
        for vertice in caminho:
            print(vertice, end=" ")
        print() 