#!/usr/bin/env python

# Given this graph
graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}

def bfs_shortest_path(graph, start, goal):
    # keep track of all the paths to be checked
    explored = []

    queue = [start]

    # return path if start is goal
    if start == goal:
        return "Home sweet home!"
    while queue:
        path = queue.pop(0)

        vertex = path[-1]
        if vertex not in explored:
            linked_vertices = graph[vertex]
        for vertex_link in linked_vertices:
            path_to_goal = list(path)
            path_to_goal.append(vertex_link)
            queue.append(path_to_goal)
            if vertex_link == goal:
                return path_to_goal
        explored.append(vertex)

    # Find the shortest path to the goal
    return "Cannot reach goal"

ans = bfs_shortest_path(graph,'A', 'E')
print(ans)
