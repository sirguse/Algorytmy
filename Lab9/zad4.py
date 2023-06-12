import heapq

def dijkstra(graph, start):
    # Inicjalizacja
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        # Wybieramy wierzchołek o najniższym koszcie
        current_distance, current_node = heapq.heappop(priority_queue)

        # Sprawdzamy, czy aktualny dystans do wierzchołka jest mniejszy niż zapisany
        if current_distance > distances[current_node]:
            continue

        # Przeglądamy sąsiadów obecnego wierzchołka
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Jeśli znaleźliśmy krótszą drogę do sąsiada, aktualizujemy jego dystans i dodajemy do kolejki
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Test algorytmu Dijkstry na przykładowym grafie
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

print(dijkstra(graph, 'A'))  # Wyświetli: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
