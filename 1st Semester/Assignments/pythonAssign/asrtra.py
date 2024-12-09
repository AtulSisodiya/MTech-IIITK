import heapq

def a_star(graph, start, goal, heur):
    # Priority queue for the open list
    open_list = []
    heapq.heappush(open_list, (0, start, None))

    g_cost = {start: 0}  # Cost from start to each node
    parents = {start: None}  # Parent pointers for path reconstruction

    while open_list:
        current_f, current_node, parent = heapq.heappop(open_list)

        # Update parent of the current node
        parents[current_node] = parent

        # If the goal is reached, reconstruct the path
        if current_node == goal:
            path = []
            while current_node:
                path.append(current_node)
                current_node = parents[current_node]
            return path[::-1]

        # Iterate through neighbors of the current node
        for neighbor, cost in graph[current_node]:  # Iterate directly over the list of tuples
            tent_g = g_cost[current_node] + cost

            # Update costs and enqueue neighbors
            if neighbor not in g_cost or tent_g < g_cost[neighbor]:
                g_cost[neighbor] = tent_g
                f_cost = tent_g + heur(neighbor, goal)
                heapq.heappush(open_list, (f_cost, neighbor, current_node))

    # If no path is found, return None
    return None

# Define the graph as a dictionary where values are lists of (neighbor, cost) tuples
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

# Define a heuristic function
def heur(node, goal):
    heuristic = {
        'A': 7,
        'B': 6,
        'C': 2,
        'D': 0
    }
    return heuristic.get(node, float('inf'))

# Define start and goal nodes
start = 'A'
goal = 'D'

# Find the shortest path
path = a_star(graph, start, goal, heur)
print("Path:", path)
