from Cell import Cell
from State import States
from grid import Grid

g=Grid(4)
s=States(g)
c1 =Cell("metal", [1,3], g)
c2=Cell("red", [2,0], g)
c3 =Cell("circle", [1,2], g)
c4 =Cell("circle", [1,1], g)
g.printgrid()
# to make sure that the  move cell function is returning object
print(g.movecell(c2,[1,0])) 
g.moveredaction([1,0])
# # print(c2.pos)
# print(g.printgrid())
# #print(c2.symbol)
# print(g.find_red_position())
# print(s.getallcellmoves(c2))
# s.expand_purple_moves(c2) 

# print()
# print()
# print(g.printgrid())


