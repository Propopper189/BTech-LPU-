import heapq

def a_star(graph, heuristic, start, goal):

    # Open list implemented as a priority queue
    open_list = []
    heapq.heappush(open_list, (0, start))

    # Cost from start to a node (g(n))
    g_cost = {start: 0}

    # To reconstruct the path
    parent = {start: None}

    while open_list:
        # Node with lowest f(n) = g(n) + h(n)
        current_f, current_node = heapq.heappop(open_list)

        # Goal check
        if current_node == goal: 
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]
            return path[::-1], g_cost[goal]
        
        # Explore neighbors
        for neighbor, cost in graph[current_node]:
            tentative_g = g_cost[current_node] + cost

            # If a better path is found
            if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g
                f_cost = tentative_g + heuristic[neighbor]
                heapq.heappush(open_list, (f_cost, neighbor))
                parent[neighbor] = current_node

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('G', 2),],
    'F': [],
    'G': []
}

heuristic = {
    'A': 5, 
    'B': 3,
    'C': 4,
    'D': 4,
    'E': 1,
    'F': 6,
    'G': 0
}

path, cost = a_star(graph, heuristic, 'A', 'G')
print("Path: ", path)
print("Cost: ", cost)