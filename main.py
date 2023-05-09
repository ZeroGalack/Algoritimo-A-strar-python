import numpy as np
import matplotlib.pyplot as plt


def find_path(matrix, start, end):
    # Define as ações possíveis: cima, baixo, esquerda, direita
    actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Obtém as dimensões da matriz
    rows, cols = matrix.shape

    # Inicializa as listas de nós abertos e fechados
    open_list = [start]
    closed_list = []

    # Cria um dicionário para armazenar os custos g e h de cada nó
    g_scores = {start: 0}
    h_scores = {start: heuristic(start, end)}

    # Cria um dicionário para armazenar os pais de cada nó
    parents = {}

    while open_list:
        # Encontra o nó com o menor valor de f = g + h
        current = min(open_list, key=lambda node: g_scores[node] + h_scores[node])

        # Verifica se chegamos ao destino
        if current == end:
            path = construct_path(parents, end)
            return path

        # Remove o nó atual da lista aberta e adiciona na lista fechada
        open_list.remove(current)
        closed_list.append(current)

        # Explora os vizinhos do nó atual
        for action in actions:
            row, col = current
            new_row = row + action[0]
            new_col = col + action[1]

            # Verifica se a posição é válida dentro da matriz
            if (new_row >= 0 and new_row < rows and new_col >= 0 and new_col < cols):
                neighbor = (new_row, new_col)

                # Verifica se o vizinho é uma parede (2) ou já foi visitado
                if (matrix[new_row, new_col] == 2) or (neighbor in closed_list):
                    continue

                # Calcula o custo g do vizinho
                new_g_score = g_scores[current] + 1

                if neighbor not in open_list:
                    # Adiciona o vizinho na lista aberta
                    open_list.append(neighbor)
                elif new_g_score >= g_scores[neighbor]:
                    # O custo atual é maior ou igual ao custo anterior, não faz nada
                    continue

                # Atualiza os custos g e h e define o pai do vizinho
                g_scores[neighbor] = new_g_score
                h_scores[neighbor] = heuristic(neighbor, end)
                parents[neighbor] = current

    # Não foi possível encontrar um caminho
    return None


def heuristic(node, goal):
    # Distância de Manhattan como heurística
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])


def construct_path(parents, end):
    # Reconstrói o caminho a partir dos pais
    path = [end]
    while end in parents:
        end = parents[end]
        path.append(end)
    path.reverse()
    return path


# Matriz de exemplo
matriz = np.array([
    [2, 1, 0, 1, 1, 1],
    [2, 2, 1, 2, 1, 1],
    [2, 1, 1, 1, 1, 2],
    [1, 3, 1, 2, 2, 1]
])

MatizOld = np.array([
    [2, 1, 0, 1, 1, 1],
    [2, 2, 1, 2, 1, 1],
    [2, 1, 1, 1, 1, 2],
    [1, 3, 1, 2, 2, 1]
])

# Encontra as posições inicial (3) e final (0) na matriz
start = tuple(np.argwhere(matriz == 3)[0])
end = tuple(np.argwhere(matriz == 0)[0])

# Encontra o melhor caminho
caminho = find_path(matriz, start, end)

if caminho:
    # Exibe o caminho encontrado
    for pos in caminho:
        matriz[pos] = 9  # Marca o caminho com o valor 9
    print("Melhor caminho encontrado:")
    caminho_final = matriz
    print(caminho_final)
else:
    print("Não foi possível encontrar um caminho.")

print(MatizOld)
# Criar duas matrizes de exemplo
matrix1 = MatizOld
matrix2 = matriz

# Plotar a primeira matriz
plt.subplot(1, 2, 1)
plt.imshow(matrix1, cmap='tab10')
plt.title('Old')
plt.axis('off')


# Plotar a segunda matriz
plt.subplot(1, 2, 2)
plt.imshow(matrix2, cmap='tab20')
plt.title('New')
plt.axis('off')

# Mostrar o plot
plt.tight_layout()
plt.show()