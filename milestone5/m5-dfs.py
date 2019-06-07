#!/usr/bin/env python

# Given this graph
graph = {'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}

# Write a depth first search to visit every node in the graph count the number of edges traversed
def dfs_visit(graph, start):
    queue = [start]
    path = []
    count = 1

    while queue:
        vertex = queue.pop()
        count += 1
        if vertex in path:
           continue
        path.append(vertex)
        for neighbor in graph[vertex]:
            queue.append(neighbor)
    return count

ans = dfs_visit(graph, 'A')
print(ans)
