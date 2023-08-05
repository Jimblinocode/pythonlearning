import pygame
import globals
from colors import *

class Player:
    def __init__(self) -> None:
        self.pos = [globals.res[0]/2, globals.res[1]/2]
        self.size = [100, 100]
        self.img = pygame.Surface(self.size)
        self.img.fill(WHITE)
        self.rect = self.img.get_rect(center = self.pos)
        self.R = False 
        self.L = False
        self.U = False
        self.D = False
        self.speed = 10
    
    def process_input(self, controls):
        self.U = controls[pygame.K_w]
        self.D = controls[pygame.K_s]
        self.R = controls[pygame.K_d]
        self.L = controls[pygame.K_a]

    def update(self):
        if self.U:
            self.pos[1] -= self.speed
        if self.D:
            self.pos[1] += self.speed
        if self.R:
            self.pos[0] += self.speed
        if self.L:
            self.pos[0] -= self.speed
        self.rect = self.img.get_rect(center = self.pos)
        margin_X = self.size[0]/2
        margin_Y = self.size[0]/2

        if self.pos[0] - margin_X < 0:
            self.pos[0] = margin_X
        if self.pos[0] + margin_X > globals.res[0]:
            self.pos[0] = globals.res[0] - margin_X
        if self.pos[1] - margin_Y < 0:
            self.pos[1] = margin_Y
        if self.pos[1] + margin_Y > globals.res[1]:
            self.pos[1] = globals.res[1] - margin_Y
        self.rect = self.img.get_rect(center = self.pos)

    def draw(self):
        globals.screen.blit(self.img, self.rect)
