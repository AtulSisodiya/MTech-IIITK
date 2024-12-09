import heapq

def uniform_cost(graph,start,goal):
    priority_queue = [(0,start,[start])]
    visited = set()

    while priority_queue:
        cost,node,path = heapq.heappop(priority_queue)

        if node == goal:
            return cost,path
        
        if node not in visited:
            visited.add(node)

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue,(cost + weight, neighbor, path + [neighbor]))
    return float('inf'), []

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('F', 3)],
    'D': [('B', 2), ('G', 2)],
    'E': [('B', 5), ('G', 1)],
    'F': [('C', 3), ('G', 6)],
    'G': [('D', 2), ('E', 1), ('F', 6)]
}

cost, path = uniform_cost(graph,'A','G')
print(f"Cost: {cost}, Path: {path} ")
