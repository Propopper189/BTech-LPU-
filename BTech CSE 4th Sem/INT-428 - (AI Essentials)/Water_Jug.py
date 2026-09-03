from collections import deque

def water_jug_bfs(capacity_a, capacity_b, target):
    # Initial state
    start = (0, 0)
    # Queue for BFS : (state, path)
    queue = deque()
    queue.append((start, [start]))
    
    # Visited States
    visited = set()
    visited.add(start)
    while queue:
        (x, y), path = queue.popleft()
        
        # Goal test
        if x == target or y == target: 
            return path
            
        # Generate all possible next states
        next_states = [
            (capacity_a, y),  # Fill Jug A
            (x, capacity_b),  # Fill Jug B
            (0, y),           # Fill Jug A
            (x, 0),           # Empty Jug B
            # Pour A -> B
            (x - min(x, capacity_b - y), 
            y + min(y, capacity_b - y)),
            
            # Pour B -> A
            (x + min(y, capacity_a - x),
            y - min(y, capacity_a - x))
            ]
        print(next_states)
        for state in next_states:
            if state not in visited:
                    visited.add(state)
                    queue.append((state, path + [state]))
solution = water_jug_bfs(4, 3, 2)
if solution:
    print(solution)
else:
    print("No Solution Found")