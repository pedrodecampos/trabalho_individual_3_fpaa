# Implementação do Algoritmo para Caminho Hamiltoniano

## Descrição do Projeto

Este projeto implementa um algoritmo para encontrar um Caminho Hamiltoniano em um grafo orientado ou não orientado. Um Caminho Hamiltoniano é um caminho que visita cada vértice do grafo exatamente uma vez.

### Lógica do Algoritmo

O algoritmo implementado utiliza uma abordagem de backtracking para encontrar o Caminho Hamiltoniano. Aqui está a explicação linha a linha:

1. A classe `Grafo` é definida para representar o grafo usando uma matriz de adjacência.
2. O método `adicionar_aresta` adiciona uma aresta entre dois vértices.
3. O método `eh_seguro` verifica se um vértice pode ser adicionado ao caminho atual:
   - Verifica se existe uma aresta entre o último vértice do caminho e o vértice candidato
   - Verifica se o vértice já está no caminho
4. O método `caminho_hamiltoniano_util` implementa o backtracking:
   - Caso base: quando todos os vértices estão no caminho
   - Para cada vértice, tenta adicioná-lo ao caminho se for seguro
   - Se não encontrar solução, volta atrás (backtrack)
5. O método `encontrar_caminho_hamiltoniano` inicia o processo a partir do vértice 0

## Como Executar o Projeto

### Pré-requisitos

- Python 3.x
- Bibliotecas necessárias:
  ```
  pip install networkx matplotlib
  ```

### Executando o Projeto

1. Clone o repositório:

   ```
   git clone [URL_DO_REPOSITÓRIO]
   ```

2. Navegue até o diretório do projeto:

   ```
   cd [NOME_DO_DIRETÓRIO]
   ```

3. Execute o programa principal:

   ```
   python main.py
   ```

4. Para visualizar o grafo:
   ```
   python view.py
   ```

## Relatório Técnico

### Análise da Complexidade Computacional

#### Classes P, NP, NP-Completo e NP-Difícil

O problema do Caminho Hamiltoniano é NP-Completo. Isso significa que:

1. Pertence à classe NP: Uma solução pode ser verificada em tempo polinomial
2. É NP-Difícil: Qualquer problema em NP pode ser reduzido a ele em tempo polinomial
3. Não pertence à classe P: Não existe algoritmo conhecido que o resolva em tempo polinomial

A relação com o Problema do Caixeiro Viajante (TSP) é direta, pois o TSP é uma extensão do Caminho Hamiltoniano onde se busca minimizar o custo total do caminho.

### Análise da Complexidade Assintótica de Tempo

A complexidade temporal do algoritmo é O(n!), onde n é o número de vértices do grafo. Isso ocorre porque:

1. Para cada posição no caminho, tentamos todos os vértices não visitados
2. No pior caso, precisamos explorar todas as permutações possíveis dos vértices
3. O método de contagem de operações mostra que cada chamada recursiva pode gerar até n-1 novas chamadas

### Aplicação do Teorema Mestre

O Teorema Mestre não pode ser aplicado diretamente ao algoritmo de Caminho Hamiltoniano porque:

1. O algoritmo não segue a forma de recorrência T(n) = aT(n/b) + f(n)
2. A estrutura do problema é diferente daquela que o Teorema Mestre foi projetado para analisar
3. O número de subproblemas não é constante e não divide o problema em partes iguais

### Análise dos Casos de Complexidade

1. **Pior Caso**: O(n!)

   - Ocorre quando precisamos explorar todas as permutações possíveis
   - Impacto: O tempo de execução cresce exponencialmente com o número de vértices

2. **Caso Médio**: O(n!)

   - Embora alguns caminhos possam ser encontrados mais rapidamente, a média ainda é fatorial
   - Impacto: O algoritmo continua impraticável para grafos grandes

3. **Melhor Caso**: O(n)
   - Ocorre quando o primeiro caminho tentado é hamiltoniano
   - Impacto: Mesmo no melhor caso, o algoritmo ainda é ineficiente para grafos grandes

## Visualização do Grafo

O projeto inclui uma funcionalidade de visualização usando NetworkX e Matplotlib. O grafo é exibido com:

- Vértices numerados
- Arestas em azul
- Caminho Hamiltoniano destacado em vermelho (quando encontrado)

