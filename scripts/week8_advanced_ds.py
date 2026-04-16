def shortest_path(graph, start, end):
    visited = set()
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    prev = {}

    while visited != set(graph.keys()):
        current = min(
            (node for node in graph if node not in visited),
            key=lambda x: dist[x]
        )

        visited.add(current)

        for neighbor, weight in graph[current].items():
            new_dist = dist[current] + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                prev[neighbor] = current

    # Build path
    path = []
    curr = end
    while curr:
        path.insert(0, curr)
        curr = prev.get(curr)

    return path, dist[end]