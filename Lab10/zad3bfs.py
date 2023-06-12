from collections import deque

def bfs(graph, root):
    visited = set([root])
    queue = deque([root])

    while queue:
        vertex = queue.popleft()
        print(vertex)

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

# Przykładowy graf do przetestowania
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}

bfs(graph, 'A')
