import pygame
pygame.init()



info = pygame.display.Info()
resolution = (info.current_w, info.current_h)

screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()
playercords = [info.current_w/2, info.current_h/2]
controls = pygame.key.get_pressed()
movespeed = 10

def process_input():
    global controls
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    controls = pygame.key.get_pressed()
   

def update():
    if controls[pygame.K_w]:
        playercords[1] -= movespeed
    if controls[pygame.K_s]:
        playercords[1] += movespeed
    if controls[pygame.K_d]:
        playercords[0] += movespeed
    if controls[pygame.K_a]:
        playercords[0] -= movespeed

def draw():
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 255), playercords, 100)
    pygame.display.flip()

import time
running = True
while running:
    process_input()
    update()
    draw()
    clock.tick(165)