from queue import PriorityQueue

def astar_algorithm(graph, start, goal, heuristic):
    """
    A* algorithm implementation.

    :param graph: dict, adjacency list representing the graph. Each key is a node, and its value is a list of tuples (neighbor, cost).
    :param start: str/int, starting node.
    :param goal: str/int, goal node.
    :param heuristic: dict, estimated cost from each node to the goal.
    :return: tuple, (path, total_cost)
    """
    # Priority queue to hold nodes with their costs
    open_set = PriorityQueue()
    open_set.put((0, start))  # (f_score, node)

    # To store the actual cost to reach each node from the start
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    # To reconstruct the path
    came_from = {}

    while not open_set.empty():
        _, current = open_set.get()

        if current == goal:
            # Reconstruct the path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, g_score[goal]

        for neighbor, cost in graph[current]:
            tentative_g_score = g_score[current] + cost

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic[neighbor]
                open_set.put((f_score, neighbor))

    return None, float('inf')  # No path found

# Example usage:
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 0
}

start_node = 'A'
goal_node = 'D'

path, total_cost = astar_algorithm(graph, start_node, goal_node, heuristic)
print(f"Path: {path}")
print(f"Total cost: {total_cost}")
