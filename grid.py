import keyboard

from Cell import Cell

class Grid:

    def __init__(self,size):
        self.size=size
        self.grid=self.drawgrid()
   
    def drawgrid(self):
        grid=[]
        for row in range(self.size):
            grid.append(["@"]*self.size)
        return grid
    
    def printgrid(self):
        for row in self.grid:
            print("  ".join(row))
        print()   
    def find_purple_position(self):
      for r in range(self.size):
          for c in range(self.size):
            if self.grid[r][c]=="-":
                # return self.grid[r][c]
                return Cell('purple', [r,c], self)

    def find_red_position(self):
      for r in range(self.size):
          for c in range(self.size):
             if self.grid[r][c] == "+":
                return Cell('red',[r,c],self)

          
                    
    def movecell(self,cell:Cell,newposition:list):
        if self.grid[newposition[0]][newposition[1]] == "@" or  self.grid[newposition[0]][newposition[1]] == "O":
            self.grid[cell.pos[0]][cell.pos[1]] = "@"
            self.grid[newposition[0]][newposition[1]] = cell.symbol
            cell.pos[0] = newposition[0]
            cell.pos[1] = newposition[1]
        else: 
            return 
        # return self.printgrid()
        return self
    # ///////////////////////////////////////MOVE BY KEYBOARD/////////////////////////////    
    def move_up(self, cell:Cell):
        newpos = []
        if  0 <= cell.pos[0] - 1 < self.size:
            newpos = [cell.pos[0]-1, cell.pos[1]]
            self.movecell(cell, newpos)
        return newpos
       
    def move_down(self, cell:Cell):
        newpos = []
        if  0 <= cell.pos[0] + 1 < self.size:
            newpos = [cell.pos[0]+1, cell.pos[1]]
            self.movecell(cell, newpos)
        return newpos

    def move_left(self):
        newpos = [self.cell.pos[0], self.cell.pos[1] - 1]
        self.movecell(newpos)

    def move_right(self):
        newpos = [self.cell.pos[0], self.cell.pos[1] + 1]
        self.movecell(newpos)

    def run(self, cell:Cell):
        # r = True
        # try:
        while True:
            # self.printgrid()  # Print the grid
            if keyboard.is_pressed('w'):  # Move up
                newpos = self.move_up(cell)
                self.movepurpleaction(newpos)
                break
            elif keyboard.is_pressed('s'):  # Move left
                newpos1 = self.move_down(cell)
                self.movepurpleaction(newpos1)
                break

            # elif keyboard.is_pressed('d'):  # Move right
            #     self.move_right()   
        # except KeyboardInterrupt: print("Program interrupted and stopped.")


    
    # /////////////////////////////////////GET the POOSIBLE MOVES OF THE CELL/////////////////////////////////// 
    def getcellmoves(self,cell:Cell):
        possiblemoves=[]
        size=self.size
        for r in range(size):
            for c in range(size):
                if self.grid[r][c] in ["@","O"]:
                   possiblemoves.append([r,c])
        return possiblemoves            
    # ///////////////////////////////////////CHECK FOR WINNING///////////////////////////////////////////
    def win(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.grid[row][col] =="O":
                    return False
        return True
    def copy_grid(self): 
      new_grid = Grid(self.size) 
      new_grid.grid = [row[:] for row in self.grid]
      return new_grid

    def movethepurpleaction(self, newposition: list):
        
        self.movepurpleaction_right(newposition)
        self.movepurpleaction_left(newposition)
        self.movepurpleaction_up(newposition)
        self.movepurpleaction_down(newposition)

    def movepurpleaction_right(self, newposition: list):
        newrow = newposition[0]  # x
        newcol = newposition[1]  # y
        size = self.size

        # Right
        start = -1
        end = -1
        for r in range(newcol + 1, size):
            if self.grid[newrow][r] in ["M", "+", "-"]:
                start = r
                break

        for r in range(start + 1, size):
            if self.grid[newrow][r] in ["@"]:
                end = r
                break

        while start != -1 and end != -1 and end > start:
            x = end - 1
            sym = self.grid[newrow][x]
            self.grid[newrow][x] = "@"
            self.grid[newrow][end] = sym
            end -= 1

    def movepurpleaction_left(self, newposition: list):
        newrow = newposition[0]
        newcol = newposition[1]
        size = self.size

        # Left
        start = -1
        end = -1
        for r in range(newcol - 1, -1, -1):
            if self.grid[newrow][r] in ["M", "+", "-"]:
                start = r
                break

        for r in range(start - 1, -1, -1):
            if self.grid[newrow][r] in ["@"]:
                end = r
                break

        while start != -1 and end != -1 and end < start:
            x = end + 1
            sym = self.grid[newrow][x]
            self.grid[newrow][x] = "@"
            self.grid[newrow][end] = sym
            end += 1
        
    def movepurpleaction_up(self, newposition: list):
        newrow = newposition[0]
        newcol = newposition[1]
        size = self.size

        # Up
        start = -1
        end = -1
        for r in range(newrow - 1, -1, -1):
            if self.grid[r][newcol] in ["M", "+", "-"]:
                start = r
                break

        for r in range(start - 1, -1, -1):
            if self.grid[r][newcol] in ["@"]:
                end = r
                break

        while start != -1 and end != -1 and end < start:
            x = end + 1
            sym = self.grid[x][newcol]
            self.grid[x][newcol] = "@"
            self.grid[end][newcol] = sym
            end += 1

    def movepurpleaction_down(self, newposition: list):
        newrow = newposition[0]
        newcol = newposition[1]
        size = self.size

        # Down
        start = -1
        end = -1
        for r in range(newrow + 1, size):
            if self.grid[r][newcol] in ["M", "+", "-"]:
                start = r
                break

        for r in range(start + 1, size):
            if self.grid[r][newcol] in ["@"]:
                end = r
                break

        while start != -1 and end != -1 and end > start:
            x = end - 1
            sym = self.grid[x][newcol]
            self.grid[x][newcol] = "@"
            self.grid[end][newcol] = sym
            end -= 1
        
    # ////////////////MOVE THE PURPLE////////////////////
    def movepurpleaction(self, newposition: list):
        newrow = newposition[0]
        newcolumn = newposition[1]
        sym = ""
        size = self.size
         
    
        # Check for rows
        for row in range(size):
            if self.grid[newrow][row] in ["M", "+"]:
                sym = self.grid[newrow][row]
                if row > newposition[1]:
                    if row + 1 < size:  
                        self.grid[newrow][row] = "@"
                        self.grid[newrow][row + 1] = sym
                        break
                else:
                    if row - 1 >= 0:  
                        self.grid[newrow][row] = "@"
                        self.grid[newrow][row - 1] = sym
                        break
    
        # Check for columns
        for column in range(self.size):
            if self.grid[column][newcolumn] in ["M", "+"]:
                sym = self.grid[column][newcolumn]
                if column > newposition[0]:
                    if column + 1 < size:  # Check if cell is within the bounds
                        self.grid[column][newcolumn] = "@"
                        self.grid[column + 1][newcolumn] = sym
                        break
                else:
                    if column - 1 >= 0:  
                        self.grid[column][newcolumn] = "@"
                        self.grid[column - 1][newcolumn] = sym
                        break
    
        return sym
    
    def moveredaction(self, newposition: list):
        newrow = newposition[0]
        newcolumn = newposition[1]
        size = self.size

        # Move magnets horizontally 
        for r in range(size):
            rowsym = self.grid[newrow][r]
            if rowsym in ["M", "-"]:
                if r > newcolumn:  # Move to the left
                    if r - 1 >= 0 and self.grid[newrow][r - 1] in ["@", "O"]:
                        self.grid[newrow][r] = "@"
                        self.grid[newrow][r - 1] = rowsym
                        
        for r in range(newcolumn,-1,-1):
            rowsym = self.grid[newrow][r]
            if rowsym in ["M", "-"]:                
                if r < newcolumn:  # Move to the right
                    if r + 1 < size and self.grid[newrow][r + 1] in ["@", "O"]:
                        self.grid[newrow][r] = "@"
                        self.grid[newrow][r + 1] = rowsym
                    

        # Move vertically 
        for c in range(size):
            columnsym = self.grid[c][newcolumn]
            if columnsym in ["M", "-"]:
                if c > newrow:  # Move up the magnets
                    if c - 1 >= 0 and self.grid[c - 1][newcolumn] in ["@", "O"]:
                        self.grid[c][newcolumn] = "@"
                        self.grid[c - 1][newcolumn] = columnsym
        for c in range(newrow,-1,-1):
            columnsym = self.grid[c][newcolumn]
            if columnsym in ["M", "-"]:
                if c < newrow:  # Move down the megnets
                    if c + 1 < size and self.grid[c + 1][newcolumn] in ["@", "O"]:
                        self.grid[c][newcolumn] = "@"
                        self.grid[c + 1][newcolumn] = columnsym