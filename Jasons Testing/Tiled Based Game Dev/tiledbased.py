import pygame, sys, os
from settings import *

pygame.init()
clock = pygame.time.Clock()
pygame.key.set_repeat(500, 100) # If you hold down a button for 500 milli, repeat every 100 millie

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("AbyssRPG Alpha 0.0.0")

def absolute_path(path: str) -> str:
    """Returns the absolute path of a given path based on this file"""
    return os.path.join(os.path.dirname(__file__), path) 

class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.blitPlayer()

    def collisions(self, dx=0, dy=0):
        for i in walls:
            if i.x == self.x + dx and i.y == self.y + dy:
                return True
        return False

    def blitPlayer(self):
        self.playerHitbox = pygame.Rect(self.x * tilesize, self.y * tilesize, tilesize, tilesize)
        self.drawrect = pygame.draw.rect(screen, red, self.playerHitbox)

    def move(self, dx=0, dy=0): # 0 by default
        if not self.collisions(dx, dy):
            self.x += dx
            self.y += dy

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.wallHitbox = pygame.Rect(self.x * tilesize, self.y * tilesize, tilesize, tilesize)
        self.drawrect = pygame.draw.rect(screen, gray, self.wallHitbox)
        pygame.sprite.Sprite.__init__(self, walls)


def draw_grid():
    for x in range(0, screen_width, tilesize):
        pygame.draw.line(screen, gray, (x, 0), (x, screen_height))
    for y in range(0, screen_height, tilesize):
        pygame.draw.line(screen, gray, (0, y), (screen_width, y))

def graphics():
    screen.fill(dark_gray)
    draw_grid()
    player.blitPlayer()
    for x in range(10, 20):
        Wall(x, 5)

#--Game Variables--#
player = Player(5, 0)
walls = pygame.sprite.Group()

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
