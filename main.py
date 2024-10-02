import pygame
from pygame.locals import *
import sys

# Custom Classes
import Player

pygame.init()

# Starter Parameters
vector = pygame.math.Vector2

HEIGHT = 720
WIDTH = 1280

FPS = 60
walkCount = 0

FramePerSec = pygame.time.Clock()
 
displaySurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kitty Distribution")

#background = pygame.image.load('LEVEL_1.png')

player1 = Player.Player(vector)

all_sprites = pygame.sprite.Group()
all_sprites.add(player1)

def redrawGameWindow():
    global walkCount

   # displaySurface.blit(background, (0, 50))

    if walkCount + 1 >= 12:
        walkCount = 0
        
    if player1.moveLeft:
        displaySurface.blit(pygame.transform.flip(player1.moveRightList[walkCount//5], True, False), player1.pos)
        walkCount += 1                          
    elif player1.moveRight:
        displaySurface.blit(player1.moveRightList[walkCount//5], player1.pos)
        walkCount += 1
    else:
        displaySurface.blit(player1.playerImage, player1.pos)
        walkCount = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    displaySurface.fill((255,255,255))

    font = pygame.font.SysFont("Arial", 36)
    txtsurf = font.render(str(walkCount), True, (0,0,0))

    displaySurface.blit(txtsurf, (200 - txtsurf.get_width() // 2, 150 - txtsurf.get_height() // 2))
    redrawGameWindow()
    
    pygame.display.update()
    FramePerSec.tick(FPS)

    player1.move()
    