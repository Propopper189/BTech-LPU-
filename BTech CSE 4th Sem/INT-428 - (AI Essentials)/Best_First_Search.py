import heapq

def best_first_search(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], start))
    closed = set()
    parent = {start: None}

    while open_list:
        _, current = heapq.heappop(open_list)

        # Goal test
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]

        closed.add(current)

        # Expand current node
        for neighbor in graph[current]:
            if neighbor not in closed:
                parent[neighbor] = current
                heapq.heappush(open_list, (heuristic[neighbor], neighbor))

    return None

graph = {
    'A': ['B', 'C'], 
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

heuristic = {
    'A': 6, 
    'B': 4, 
    'C': 5, 
    'D': 2,
    'E': 1,
    'F': 0
}

path = best_first_search(graph, 'A', 'F', heuristic)
print("Path found:", path)
