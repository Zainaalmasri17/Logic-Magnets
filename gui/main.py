import pygame
import time
import random 

pygame.font.init()
WIDTH, HEIGHT = 600, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Logic Magnets")

# Load and scale the background image
BG = pygame.transform.scale(pygame.image.load("360_F_296153501_B34baBHDkFXbl5RmzxpiOumF4LHGCvAE.jpg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 5
FONT = pygame.font.SysFont("comicsans", 30)
def drawgrid(self,size):
    grid=[]
    for row in range(self.size):
        grid.append(["@"]*self.size)


    return grid
        

def drawempty(size,x):
    WIN.blit(BG, (0, 0)) 

    # Render the elapsed time text
    
    
    pygame.draw.rect(WIN, "red", player)
    pygame.display.update()  
def draw(player, elapsed_time):
    WIN.blit(BG, (0, 0)) 

    # Render the elapsed time text
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))
    pygame.draw.rect(WIN, "red", player)
    pygame.display.update()  

def main():
    run = True
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time=0
    while run:
        clock.tick(60)
        
        
        elapsed_time = time.time() - start_time
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL  # Move left
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL  # Move right

        draw(player, elapsed_time)  

    pygame.quit()  

if __name__ == "__main__":  
    pygame.init()  
    main()
