import random
import globals
import pygame
from colors import *

class enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(enemy, self).__init__()
        self.position = [random.randint(0, globals.res[0]), random.randint(0, globals.res[1])]
        self.sizze = [100, 100]
        self.image = pygame.Surface(self.sizze)
        self.image.fill(BLACK)
        self.rect = self.image.get_rect(center = self.position)
        self.speed = 10

    def update(self):
        if self.rect.right < 0:
            self.kill()


    def Draw(self):
        globals.screen.blit(self.image, self.rect)