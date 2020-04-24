import pygame, os, sys

pygame.init()
clock = pygame.time.Clock()

screen_height = 786
screen_width = 1024

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Project Elephant")

def absolute_path(path: str) -> str:
    """Returns the absolute path of a given path based on this file"""
    return os.path.join(os.path.dirname(__file__), path)

def redraw_game_window():
    screen.fill(white)

white = (91, 91, 91)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    redraw_game_window()

    clock.tick(60)
    pygame.display.flip()

