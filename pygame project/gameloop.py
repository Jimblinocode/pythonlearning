import globals
from player import Player
import colors
import pygame 
from enemies import enemy

class game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.fps = 165
        self.player = Player()
        self.Enemy = enemy()

    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                globals.running = False
        controls = pygame.key.get_pressed()
        self.player.process_input(controls)

    def update(self):
        self.player.update()
        self.Enemy.update()

    def draw(self):
        globals.screen.fill(colors.GREY)
        self.player.draw()
        self.Enemy.Draw()
        pygame.display.flip()    

    def run(self):
        while globals.running:
            self.process_input()
            self.update()
            self.draw()
            self.clock.tick(self.fps)


Game = game()
Game.run()