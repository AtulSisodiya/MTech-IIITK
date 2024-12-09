graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = [] # visited nodes
queue = []   #queue 

def bfs(visited, graph, node): #creating function BFS
  visited.append(node)
  queue.append(node)

  while queue:          #loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)


print("BFS of given Graph ")
bfs(visited, graph, '5') #starting node