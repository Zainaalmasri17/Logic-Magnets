import heapq
from grid import Grid
from State import States
from Cell import Cell
class Node:
    def __init__(self, state, parent=None, cost=0):
        self.state = state
        self.parent = parent
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

def ucs(start_state):
    # Priority queue to store (cost, node) tuples
    frontier = []
    heapq.heappush(frontier, (0, Node(start_state)))

    # Visited set to store visited states
    visited = set()

    while frontier:
        # Pop the node with the lowest cost
        cost, current_node = heapq.heappop(frontier)

        # If the goal is found, reconstruct the path
        if current_node.state.initgrid.win():
            return reconstruct_path(current_node)

        # If the current state is already visited, skip
        if current_node.state in visited:
            continue

        # Mark the current state as visited
        visited.add(current_node.state)

        # Explore neighbors
        purple_positions = current_node.state.initgrid.find_purple_position()
        for purple_pos in purple_positions:
            new_board = current_node.state.copy_grid()
            new_cell = Cell("purple", purple_pos, new_board)
            new_board.movecell(new_cell, purple_pos)
            neighbor_state = States(new_board)
            step_cost = 1  # Assuming each move has a cost of 1
            new_cost = current_node.cost + step_cost
            neighbor_node = Node(neighbor_state, current_node, new_cost)
            heapq.heappush(frontier, (new_cost, neighbor_node))

    # Return None if no path is found
    return None

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]

# Example usage
if __name__ == "__main__":
    g = Grid(4)
    s = States(g)
    c1 = Cell("metal", [1, 2], g)
    c2 = Cell("purple", [2, 0], g)
    c3 = Cell("circle", [1, 3], g)
    c4 = Cell("circle", [1, 1], g)
    g.printgrid()
    print()

    # Use UCS to find the path to a win
    path_to_win = ucs(s)

    if path_to_win:
        print("Winning path found!")
        for state in path_to_win:
            state.initgrid.printgrid()
            print()
    else:
        print("No solution found.")
