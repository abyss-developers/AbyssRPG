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

class dialogue:
    def __init__(self, speaker, dialogue_text):
        self.speaker = speaker
        self.text = dialogue_text
        self.dialogue_body = pygame.Rect(0,50,600,50)

    def show_dialogue(self):
        pygame.draw.rect(screen, red, self.dialogue_body)
        print("{}:{}".format(self.speaker,self.text))
        

def redraw_game_window():
    screen.fill(white)
    debug.show_dialogue()

white = (91, 91, 91)
red = (250,250,250)

debug = dialogue("jason","hello")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    redraw_game_window()

    clock.tick(60)
    pygame.display.flip()

