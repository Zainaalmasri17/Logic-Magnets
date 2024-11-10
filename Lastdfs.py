from grid import Grid
from Cell import Cell
from State import States

def dfs(root: States):
    stack = [(root, [])]  
    visited = set()
    
    while stack:
        init_state, path = stack.pop()
        if init_state in visited:
            continue

        visited.add(init_state)

        if init_state.initgrid.win():
            print('You won :)')
            init_state.initgrid.printgrid()
            print("Path to win:", path)
            return path

        purple = init_state.initgrid.find_purple_position()
        init_state.expand_purple_moves(purple)

        for child in init_state.root.root.children:
            if child not in visited:
                stack.append((child, path + [child.data]))
                child.data.printgrid()
                print()
            if child.data.win():
                print('You won :)')
                child.data.printgrid()
                # print("Path to win:", path + [child.data])
                return path + [child.data]

        return None


if __name__ == "__main__":
    g = Grid(4)
    s = States(g)
    c1 = Cell("metal", [1, 2], g)
    c2 = Cell("purple", [2, 0], g)
    c3 = Cell("circle", [1, 3], g)
    c4 = Cell("circle", [1, 1], g)
    g.printgrid()
    print()

    
    s.expand_purple_moves(c2)

  
    path_to_win = dfs(s)

    if path_to_win:
        print("Winning path found!")
    else:
        print("No solution found.")
