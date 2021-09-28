# Link: https://www.hackerrank.com/challenges/bfsshortreach/problem

#!/bin/python3

import sys
from queue import Queue

class Node():
    def __init__(self):
        self.distance = -1
        self.children = []
        self.visited = False

def bfs(n, m, edges, s):
    nodes = [Node() for _ in range(n)]
    for edge in edges:
        first, second = [nodes[i - 1] for i in edge]
        first.children.append(second)
        second.children.append(first)
    
    top = nodes[s - 1]
    top.distance = 0
    queue = Queue()
    queue.put(top)
    while(not queue.empty()):
        node = queue.get()
        for child in node.children:
            if (not child.visited) or (child.distance > node.distance + 6):
                child.distance = node.distance + 6
                child.visited = True
                queue.put(child)
    del nodes[s - 1]
    return [node.distance for node in nodes]
    

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n, m = [int(x) for x in input().strip().split(' ')]
        edges = []
        for edges_i in range(m):
           edges_t = [int(edges_temp) for edges_temp in input().strip().split(' ')]
           edges.append(edges_t)
        s = int(input().strip())
        result = bfs(n, m, edges, s)
        print (" ".join(map(str, result)))
