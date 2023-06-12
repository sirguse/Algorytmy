import networkx as nx
import matplotlib.pyplot as plt


def ask_for_graph_type():
    print("Podaj typ grafu, który chcesz zbudować:")
    print("1. Nieskierowany")
    print("2. Skierowany")
    print("3. Ważony")
    print("4. Inny")

    return input("Twój wybór: ")


def get_edges_directed(n):
    edges = []
    for i in range(n):
        edge = input(f"Podaj krawędź nr {i+1} w formacie (start, koniec): ")
        edges.append(tuple(map(int, edge.strip('()').split(','))))
    return edges


def get_edges_weighted(n):
    edges = []
    for i in range(n):
        edge = input(f"Podaj krawędź nr {i+1} w formacie (start, koniec, waga): ")
        edges.append(tuple(map(int, edge.strip('()').split(','))))
    return edges


def display_graph_info(G):
    print("Macierz sąsiedztwa:")
    print(nx.adjacency_matrix(G).todense())

    print("Lista sąsiedztwa:")
    print(nx.generate_adjlist(G))

    nx.draw(G, with_labels=True)
    plt.show()


def main():
    graph_type = ask_for_graph_type()
    
    n = int(input("Podaj liczbę wierzchołków: "))
    m = int(input("Podaj liczbę krawędzi: "))

    if graph_type == '1':
        G = nx.Graph()
        G.add_nodes_from(range(1, n+1))
        G.add_edges_from(get_edges_directed(m))
    elif graph_type == '2':
        G = nx.DiGraph()
        G.add_nodes_from(range(1, n+1))
        G.add_edges_from(get_edges_directed(m))
    elif graph_type == '3':
        G = nx.Graph()
        G.add_nodes_from(range(1, n+1))
        G.add_weighted_edges_from(get_edges_weighted(m))
    else:
        print("Nieznany typ grafu.")
        return

    display_graph_info(G)


if __name__ == "__main__":
    main()
