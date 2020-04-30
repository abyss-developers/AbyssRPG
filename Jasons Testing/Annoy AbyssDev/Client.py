import pyautogui
import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

screen_height = 786
screen_width = 1024

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("I am not sorry")

#--Colors for Funz hehehe--#
black = (0, 0, 0)
white = (91, 91, 91)
light_grey = (200, 200, 200)
bg_color = pygame.Color('grey12')
game_font = pygame.font.Font("freesansbold.ttf", 20)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill(light_grey)

    clock.tick(60)
    pygame.display.flip()
