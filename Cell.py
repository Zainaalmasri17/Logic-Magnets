# from grid import Grid

class Cell: 
  def __init__(self,color,pos:list,grid):
    self.color=color
    self.pos=pos
    self.grid=grid
    self.symbol=self.symcells()

  def symcells(self):
        if self.color == "red":
            self.symbol = "+"
        elif self.color == "purple":
            self.symbol = "-"
        elif self.color == "metal":
            self.symbol = "M"
        elif self.color == "circle":
            self.symbol = "O"
        else:
            self.symbol = "X"  
        self.grid.grid[self.pos[0]][self.pos[1]] = self.symbol
        return self.symbol  

    
