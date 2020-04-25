import pygame, sys, os
from settings import *

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("AbyssRPG Alpha 0.0.0")

def absolute_path(path: str) -> str:
    """Returns the absolute path of a given path based on this file"""
    return os.path.join(os.path.dirname(__file__), path) 

class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def blitPlayer(self):
        self.hitbox = pygame.Rect(self.x * tilesize, self.y * tilesize, tilesize, tilesize)
        self.draw = pygame.draw.rect(screen, gray, self.hitbox)

    def move(self, dx=0, dy=0): # 0 by default
        self.x += dx
        self.y += dy

def draw_grid():
    for x in range(0, screen_width, tilesize):
        pygame.draw.line(screen, gray, (x, 0), (x, screen_height))
    for y in range(0, screen_height, tilesize):
        pygame.draw.line(screen, gray, (0, y), (screen_width, y))

def graphics():
    screen.fill(tinted_white)
    draw_grid()
    player.blitPlayer()

#--Game Variables--#
player = Player(3, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_LEFT:
                player.move(dx=-1)
            if event.key == pygame.K_RIGHT:
                player.move(dx=1)
            if event.key == pygame.K_UP:
                player.move(dy=-1)
            if event.key == pygame.K_DOWN:
                player.move(dy=1)
    
    graphics()

    clock.tick(60)
    pygame.display.flip()
