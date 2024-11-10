from collections import deque
from grid import Grid
from Cell import Cell
from State import States,Node
from collections import deque

def bfs(root:States):
    # print("hello")
    queue = deque([root,[]])
    visited = set()
    
    while queue:
        init_state = queue.popleft()
        if init_state in visited:
            continue

        visited.add(init_state)

        if init_state.initgrid.win():
            print('you won :)')
            return init_state.initgrid.printgrid()
        
        else:
            print('you lost')
        red=init_state.initgrid.find_red_position()
        # purple = init_state.initgrid.find_purple_position()
        init_state.expand_red_moves(red)
        # init_state.expand_purple_moves(purple)
        for child in init_state.root.root.children:
            if child not in visited:
                queue.append(child)
                child.data.printgrid()
                if child.data.win():
                    print('you won :)')
                    return child.data.printgrid()






# /////////////////////////PURPLE/////////////////////////////////////////////////
# g = Grid(4)
# s = States(g)
# c1 =Cell("metal", [1,2], g)
# c2=Cell("purple", [2,0], g)
# c3 =Cell("circle", [1,3], g)
# c4 =Cell("circle", [1,1], g)
# g.printgrid()
# print()
# # g.movecell(c2, [0,3])
# # g.movepurpleaction([0,3])
# # g.printgrid()
# # print()
# # s.expand_purple_moves(c2)
# dfs(s)
 #////////////////////////////RED/////////////////////////////////////////////////////  
g=Grid(5)
s1 = States(g)
c1 =Cell("red", [3,2], g)
c2=Cell("circle", [2,1], g)
c3 =Cell("circle", [2,2], g)
c4 =Cell("circle", [2,3], g)
c5 =Cell("metal", [2,0], g)
c6 =Cell("metal", [2,4], g)
g.printgrid()
print()
bfs(s1)
