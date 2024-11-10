from grid import Grid
from Cell import Cell
class levels():
g=Grid(4)
g2=Grid(6)
g3=Grid(4)
g4=Grid(6)
g5=Grid(6)
g6=Grid(4)
g7=Grid(6)
g8=Grid(4)
g9=Grid(7)
g10=Grid(4)
g11=Grid(5)
g12=Grid(5)
g13=Grid(6)
g14=Grid(4)
g15=Grid(5)
g16=Grid(5)
g17=Grid(4)
g18=Grid(6)
g19=Grid(5)
g20=Grid(5)
g21=Grid(4)
g22=Grid(5)
g23=Grid(5)
g24=Grid(5)
g25=Grid(5)
alllevels_list = [
  [ 
        # [1,1]
    g,
    Cell("purple", [2,0], g),
    None,
    Cell("circle", [1,3], g),
    Cell("circle", [1,1], g),
    Cell("metal", [1,2], g),
  ],
   [
        #  2,2
    g2,
    Cell("purple", [5,0], g2),
    None,
    Cell("circle", [0,2], g2),
    Cell("circle", [2,2], g2),
    Cell("circle", [2,4], g2),
    Cell("circle", [4,2], g2),
    Cell("circle", [2,0], g2),
    Cell("metal", [1,2], g2),
    Cell("metal", [2,1], g2),
    Cell("metal", [2,3], g2),
    Cell("metal", [3,2], g2),          
  ],
  [
    # 1,1/2,3    
    g3,
    Cell("purple", [2,0], g3),
    None,
    Cell("circle", [0,3], g3),
    Cell("circle", [1,1], g3),
    Cell("circle", [2,3], g3),
    Cell("metal",  [1,2], g3),    
  ],
  [
    # 2,4/0,5
     g4,
    Cell("purple", [2,3],g4),
    None,
    Cell("circle", [0,3], g4),
    Cell("circle", [0,5], g4),
    Cell("circle", [4,4], g4),
    Cell("metal",  [1,4], g4), 
    Cell("metal",  [3,4], g4),   
        
  ],
  [
    # 3,5/3,3
     g5,
    Cell("purple", [3,4],g5),
    None,
    Cell("circle", [0,3], g5),
    Cell("circle", [0,5], g5),
    Cell("circle", [3,3], g5),
    Cell("metal",  [1,3], g5), 
    Cell("metal",  [2,3], g5), 
    Cell("metal",  [1,5], g5), 
    Cell("metal",  [2,5], g5),    
        
  ],
   [ 
        # 1,0/2,3
    g6,
    Cell("purple", [2,0], g6),
    None,
    Cell("circle", [1,2], g6),
    Cell("circle", [0,3], g6),
    Cell("circle", [2,3], g6),
    Cell("metal", [1,1], g6),
    Cell("metal", [1,3], g6),
  ],
  [
    # 3,2/4,5
     g7,
    Cell("purple", [2,3],g7),
    None,
    Cell("circle", [0,2], g7),
    Cell("circle", [2,5], g7),
    Cell("circle", [4,5], g7),
    Cell("metal",  [1,2], g7), 
    Cell("metal",  [2,2], g7), 
    Cell("metal",  [3,3], g7), 
    Cell("metal",  [3,4], g7),    
        
  ],
  [ 
        # 2,1/0,2/
    g8,
    Cell("purple", [2,0], g8),
    None,
    Cell("circle", [0,0], g8),
    Cell("circle", [0,2], g8),
    Cell("circle", [2,2], g8),
    Cell("metal", [1,1], g8),
    Cell("metal", [1,2], g8),
  ],
   [
    # 2,4/2,3
     g9,
    Cell("purple", [2,0],g9),
    None,
    Cell("circle", [2,1], g9),
    Cell("circle", [2,6], g9),
    Cell("metal",  [2,3], g9), 
    Cell("metal",  [2,5], g9), 
       
        
  ],
    [ 
        #3,2/1,3/ 
    g10,
    Cell("purple", [0,0], g10),
    None,
    Cell("circle", [1,1], g10),
    Cell("circle", [1,3], g10),
    Cell("circle", [3,0], g10),
    Cell("circle", [3,3], g10),
    Cell("metal", [2,2], g10),
    Cell("metal", [2,3], g10),
    Cell("metal", [3,1], g10),
  ],
  [
    # 2,2
     g11,
    None, 
    Cell("red", [3,2],g11),
    Cell("circle", [2,1], g11),
    Cell("circle", [2,2], g11),
    Cell("circle", [2,3], g11),
    Cell("metal",  [2,0], g11),
    Cell("metal",  [2,4], g11), ],
     [
    #4,0/
     g12,
    None, 
    Cell("red", [3,1],g12),
    Cell("circle", [2,0], g12),
    Cell("circle", [4,0], g12),
    Cell("circle", [4,2], g12),
    Cell("metal",  [0,0], g12), 
    Cell("metal",  [1,0], g12),
    Cell("metal",  [4,3], g12),
       ],
    [
        #0,2/2,1
    g13,
    None,  
    Cell("red", [2,3], g13),
    Cell("circle", [0,3], g13),
    Cell("circle", [1,1], g13),
    Cell("circle", [2,1], g13),
    Cell("metal", [0,0], g13),
    Cell("metal", [0,4], g13),
    Cell("metal", [0,5], g13),
            
  ],
   [ 
        #0,0/2,2
    g14,
    None,
    Cell("red", [3,3], g14),
    Cell("circle", [1,0], g14),
    Cell("circle", [1,2], g14),
    Cell("circle", [2,1], g14),
    Cell("circle", [2,2], g14),
    Cell("metal", [0,3], g14),
    Cell("metal", [2,0], g14),
    Cell("metal", [3,0], g14),
  ],
  [ 
        #0,0/2,2/nooo
    g15,
    Cell("purple",[0,2], g15),
    Cell("red", [2,2], g15),
    Cell("circle", [1,4], g15),
    Cell("circle", [2,4], g15),
    Cell("metal", [0,0], g15),
    Cell("metal", [0,4], g15),
    
  ],
  [ 
        #2,2/p4,0/r0,4
    g16,
    Cell("purple",[2,4], g16),
    Cell("red", [2,0], g16),
    Cell("circle", [0,3], g16),
    Cell("circle", [0,4], g16),
    Cell("circle", [4,0], g16),
    Cell("circle", [4,3], g16),
    Cell("metal", [1,2], g16),
    Cell("metal", [3,2], g16),
    
  ], 
   [ 
        #2,2/p4,0/r0,4 ///no
    g17,
    Cell("purple",[3,3], g17),
    Cell("red", [0,0], g17),
    Cell("circle", [1,1], g17),
    Cell("circle", [1,3], g17),
    Cell("circle", [2,2], g17),
    Cell("circle", [3,1], g17),
    Cell("metal", [0,2], g17),
    Cell("metal", [2,0], g17),
    
  ], 
    [ 
        #2,2/p4,0/r0,4
    g18,
    Cell("purple",[5,3], g18),
    Cell("red", [5,2], g18),
    Cell("circle", [3,1], g18),
    Cell("circle", [3,2], g18),
    Cell("circle", [3,3], g18),
    Cell("circle", [2,3], g18),
    Cell("metal", [3,0], g18),
    Cell("metal", [1,3], g18),
     Cell("metal", [3,5], g18),
  ],
  [ 
        #r2,3/r2,1/p1,2/p4,2 /yes
    g19,
    Cell("purple",[0,2], g19),
    Cell("red", [2,2], g19),
    Cell("circle", [1,0], g19),
    Cell("circle", [1,4], g19),
    Cell("circle", [2,1], g19),
    Cell("circle", [3,0], g19),
    Cell("circle", [3,2], g19),
    Cell("circle", [3,4], g19),
    Cell("metal", [0,1], g19),
    Cell("metal", [0,3], g19),
     Cell("metal", [4,1], g19),
      Cell("metal", [4,3], g19),
  ], 
  [ 
        #p0,3/r2,0/not
    g20,
    Cell("purple",[4,2], g20),
    Cell("red", [4,3], g20),
    Cell("circle", [0,3], g20),
    Cell("circle", [1,0], g20),
    Cell("circle", [2,0], g20),
    Cell("circle", [3,0], g20),
    Cell("metal", [0,1], g20),
    Cell("metal", [0,2], g20),
    Cell("metal", [4,0], g20),
      
  ], 
  [ 
        #p0,2/r2,0
    g21,
    Cell("purple",[2,0], g21),
    Cell("red", [2,3], g21),
    Cell("circle", [0,2], g21),
    Cell("circle", [1,0], g21),
    Cell("circle", [2,1], g21),
    Cell("metal", [0,1], g21),
    Cell("metal", [1,1], g21),
    Cell("metal", [1,2], g21),
      
  ], 
   [ 
        #r3,3/p1,0/r0,1
    g22,
    Cell("purple",[0,0], g22),
    Cell("red", [3,2], g22),
    Cell("circle", [0,1], g22),
    Cell("circle", [1,0], g22),
    Cell("circle", [1,4], g22),
    Cell("circle", [2,1], g22),
    Cell("metal", [0,3], g22),
    Cell("metal", [0,4], g22),
    Cell("metal", [3,0], g22),
      
  ], 
    [ 
        #p0,4/r2,2/p0,2/
    g23,
    Cell("purple",[3,2], g23),
    Cell("red", [3,4], g23),
    Cell("circle", [0,2], g23),
    Cell("circle", [2,1], g23),
    Cell("circle", [2,2], g23),
    Cell("circle", [2,3], g23),
    Cell("metal", [0,3], g23),
    Cell("metal", [1,4], g23),
    Cell("metal", [2,0], g23),
      
  ], 
  
   [ 
        #r3,1/p2,3/r4,1
    g24,
    Cell("purple",[1,4], g24),
    Cell("red", [3,0], g24),
    Cell("circle", [0,3], g24),
    Cell("circle", [2,1], g24),
    Cell("circle", [2,3], g24),
    Cell("circle", [4,1], g24),
    Cell("circle", [4,2], g24),
    Cell("metal", [0,1], g24),
    Cell("metal", [1,3], g24),
    Cell("metal", [3,4], g24),
      
  ],
   [ 
        #r3,1/p2,3/r4,1
    g25,
    Cell("purple",[4,0], g25),
    Cell("red", [0,3], g25),
    Cell("circle", [2,0], g25),
    Cell("circle", [4,1], g25),
    Cell("circle", [4,2], g25),
    Cell("metal", [0,0], g25),
    Cell("metal", [1,2], g25),
    Cell("metal", [3,2], g25),
    Cell("metal", [4,3], g25),
      
  ],
]
