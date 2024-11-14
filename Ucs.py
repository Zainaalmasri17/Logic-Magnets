import heapq
from State import States
from grid import Grid
from Cell import Cell

class Graph :
    def __init__(self):
        self.graph = {}

    def addEdge(self, start, end, cost):
        if start not in self.graph:
            self.graph[start] = []
        self.graph[start].append((end, cost))
    

def uniform_cost_search(graph, root: States, goal):
    # Priority queue to store (cost, node, path)
    queue = [(0,root, [])]
    visited = set()
    
    while queue:
        cost, init_state, path = heapq.heappop(queue)

        if init_state in visited:
            continue

        path = path + [init_state]
        visited.add(init_state)

        purple = init_state.initgrid.find_purple_position()
        children=init_state.expand_purple_moves(purple)
            
        if init_state.initgrid.win():
            print('You won :)')
            init_state.initgrid.printgrid()
            print("Path to win:", path)
            return cost, path

        for neighbor, weight in graph[init_state]:
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor, path))

    return float("inf"), []

# Example graph represented as an adjacency list
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Running UCS
# start_node = 'A'
# goal_node = 'D'
# cost, path = uniform_cost_search(graph, start_node, goal_node)
# print(f"Cost: {cost}, Path: {path}")

g = Grid(4)
c1 = Cell("metal", [1, 2], g)
c2 = Cell("purple", [2, 0], g)
c3 = Cell("circle", [1, 3], g)
c4 = Cell("circle", [1, 1], g)

goalG = Grid(4)
gc1 = Cell("metal", [1, 3], goalG)
gc2 = Cell("purple", [1, 1], goalG)

state = States(g)
# state.initgrid.printgrid()
# print()
print('goal state: ')
goalstate = States(goalG)
# goalstate.initgrid.printgrid()
# print()
graph = Graph()
graph.addEdge(state, state, 0)

p = g.find_purple_position()
ss = state.expand_purple_moves(p)
for s1 in ss:
    s1.initgrid.printgrid()
    print()
# print(ss)
# uniform_cost_search(graph)