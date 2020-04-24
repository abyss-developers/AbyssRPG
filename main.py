import pygame, sys
from framework import *

pygame.init()
clock = pygame.time.Clock()

screen_height = 786
screen_width = 1024

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Project Elephant")

class dialogue:
    def __init__(self, speaker, dialogue_text):
        self.speaker = speaker
        self.text = dialogue_text
        self.dialogue_rect = pygame.Rect(50,50,600,50)
        self.game_font = pygame.font.Font("freesansbold.ttf",32)

    def show_dialogue(self):
        pygame.draw.rect(screen, gray, self.dialogue_rect)
        speaker_text = self.game_font.render(self.speaker, True, gray)
        screen.blit(speaker_text,(100,100))

        print("{}:{}".format(self.speaker,self.text))

def redraw_game_window():
    screen.fill(tinted_white)
    debug.show_dialogue()

tinted_white = (91, 91, 91)
gray = (250,250,250)

debug = dialogue("jason","hello")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    redraw_game_window()

    clock.tick(60)
    pygame.display.flip()
