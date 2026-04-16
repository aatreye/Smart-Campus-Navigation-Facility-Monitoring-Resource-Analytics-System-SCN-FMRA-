# Week 7 - Data Structures (Graph Representation)

def create_graph():
    """
    Default graph (used if file not loaded)
    """
    return {
        "Gate": {"Library": 5, "Canteen": 7},
        "Library": {"Lab": 3, "Auditorium": 6},
        "Canteen": {"Lab": 4},
        "Lab": {"Auditorium": 2},
        "Auditorium": {}
    }


def display_graph(graph):
    """
    Display full campus map
    """
    print("\n--- Campus Map ---")
    for node, neighbors in graph.items():
        print(f"{node} -> {neighbors}")


def add_edge(graph, src, dest, distance):
    """
    Add connection between locations
    """
    if src not in graph:
        graph[src] = {}

    graph[src][dest] = distance
    print(f"Edge added: {src} -> {dest} ({distance})")


def add_location(graph, location):
    """
    Add new location to campus
    """
    if location not in graph:
        graph[location] = {}
        print(f"{location} added to campus")
    else:
        print("Location already exists!")


def remove_location(graph, location):
    """
    Remove location from graph
    """
    if location in graph:
        graph.pop(location)

        for node in graph:
            if location in graph[node]:
                del graph[node][location]

        print(f"{location} removed from campus")
    else:
        print("Location not found!")