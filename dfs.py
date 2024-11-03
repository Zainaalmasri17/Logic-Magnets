
def dfs(stack, start, visited=None):
    visited = set()
    visited.add(start)
    start=level_num 
    
    
    
    for neighbor in dfs[start]:
        if neighbor not in visited:
            
            dfs(stack, neighbor, visited)
    
    return visited


   

