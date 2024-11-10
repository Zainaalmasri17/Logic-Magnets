from Cell import Cell
from Tree import Tree,Node
from grid import Grid
class States:
   def __init__(self,grid:Grid):
      self.initgrid=grid
      self.red_moves=[]
      self.purple_moves=[]
      self.root =Tree(grid)

   def root(self):
      self.tree.root=Node(self.initgrid)


   def getallcellmoves(self,cell:Cell):   
       possiblemoves=[]
       size=self.initgrid.size
       for r in range(size):
           for c in range(size):
            if self.initgrid.grid[r][c] in ["@","O"]:
                possiblemoves.append([r,c])
       if cell.symbol =="+":
           self.red_moves.append(possiblemoves)
       elif cell.symbol =="-":
        self.purple_moves.append(possiblemoves)
       return possiblemoves
   
   def copy_grid(self): 
      new_grid = Grid(self.initgrid.size) 
      new_grid.grid = [row[:] for row in self.initgrid.grid]
      return new_grid

   def expand_purple_moves(self, cell: Cell):
      purple_positions = self.getallcellmoves(cell) 
      for purple_pos in purple_positions: 
         newboard = self.copy_grid()
         newpurple= newboard.find_purple_position() 
         newboard.movecell(newpurple, purple_pos)
         newboard.movepurpleaction(newpurple.pos)
         # new_node = Node(newboard) 
         # self.tree.add_edge(self.tree.root, new_node) 
         self.root.root.add_child(newboard)

         
         
   def expand_red_moves(self, cell: Cell):
      red_position = self.getallcellmoves(cell) 
      for red_pos in red_position: 
         newboard = self.copy_grid()
         newred= newboard.find_red_position() 
         newboard.movecell(newred, red_pos)
         newboard.moveredaction(newred.pos)
         # new_node = Node(newboard) 
         # self.tree.add_edge(self.tree.root, new_node) 
         self.root.root.add_child(newboard)

         # newboard.printgrid()
         # print(len(self.root.root.children))     


     

   


      
    
     
     