import pygame
pygame.init()
info = pygame.display.Info()
res = (info.current_w, info.current_h)
screen = pygame.display.set_mode(res)
running = True