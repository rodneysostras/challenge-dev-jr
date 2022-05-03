# Copyright 2022 the author Rodney Sostras. All rights reserved.

from collections import deque, defaultdict

class Graph():
    def __init__(self) -> None:
        self.edges = defaultdict(lambda: {})

    def add_edge(self, source: str, target: str, weight: int):
        """ Adiciona as bordas """
        if target not in self.edges:
            self.edges[target] = defaultdict(lambda: {})
        
        # Cria uma matriz conténdo o peso para chegar na determinada bordas
        self.edges[target][source] = int(weight)

    def dijkstra(self, source: str):
        """
        Utilizando o algoritmo Dijkstra para monta um vetor
        com o custo da trajetória de cada nó em uma vértice
        """
        # Uma lista para verificar as adjacência do nó
        queue = deque()
        # Uma lista de nós visitados/verificados
        visited = set()
        # Vetor dos caminhos
        vector = defaultdict(lambda: {})

        # Adiciona valor inicial que e a origem
        vector[source] = 0

        # Aciona a origem para ser verificada
        queue.append( ( source, 0 ) )

        while queue:
            # Retira as informações do ultimo nó da fila
            current_node, current_node_weigth = queue.popleft()
            
            if current_node in visited: continue
            
            visited.add(current_node)
            
            adjacency = self.edges[current_node] or {}
            
            # Loop para verificar os nós adjacentes/próximos
            for next_node, next_node_weight in adjacency.items():
                if next_node == source: continue
                
                if next_node not in vector:
                    vector[next_node] = {}

                weight = current_node_weigth + next_node_weight
                
                # Adiciona o peso do próximo nó para o atual
                vector[next_node][current_node] = weight
                # Adiciona o próximo no na fila para ser verificado
                queue.append( (next_node, weight) )
                    
        return vector


    def shortest_path(self, source: str, target: str):
        """
        Utilizando o algoritmo Dijkstra para encontrar
        o melhor caminho de custo mínimo entre 
        dois nós de uma única direção em um grafo

        """
        # Segmentos com os custos com direção a origem
        vector = self.dijkstra(source)
        # melhor direção inicial e o alvo
        best_direction = target
        # matriz com a melhor rota
        route = []

        while best_direction:
            route.insert(0, best_direction)
            
            # menor que todos os pesos inicia com valor maximo
            min_weight = 1e7

            # retorna nós visinhos ou nenhum
            adjacency = vector[best_direction] or {}

            best_direction = None

            for next_node, next_node_weight in adjacency.items():
                if next_node in route: continue
                
                if min_weight > next_node_weight:
                    min_weight = next_node_weight
                    best_direction = next_node
        
        # Caso o caminho não exista
        if not vector[target]:
            return None

        # Peso do melhor trajeto até o alvo 
        distance = vector[target][ route[-2] ]
        
        return { 'distance': distance, 'path': route }

    def all_paths(self, source: str, target: str, max_stops = 1e7):
        """ 
        Utiliza o algoritmo 'busca em largura' (BFS) 
        para encontrar todas as trajetórias possíveis entre
        dois nós em um grafo, possuíndo a extenção de limite de paradas.
        """
        # Fila para verificar as direções
        queue = deque()
        # Lista contendo a trajetória
        routes = []

        # Inicia a fila a parti do alvo
        queue.append([target])

        while queue:
            # retira o primeiro caminho da fila
            path = queue.popleft()
            # pega o ultima direção adcionado no caminho
            last = path[ 0 ]

            # Caso o ultima direção e a origem
            # termina esse trajeto e segue para próximo
            if last == source:
                routes.append(path)
                continue
            
            # pega os nós visinhos
            adjacency = self.edges[last]
            
            for direction in adjacency.keys():
                if direction in path: continue
                if len(path) > max_stops: break
                
                # Copia a trajetória atual para
                # verificar uma nova direção
                new_path = path.copy()
                # insere uma nova direção no novo caminho
                new_path.insert(0, direction)
                # acrecenta novo caminho na fila para verificar
                queue.append(new_path)

        return routes