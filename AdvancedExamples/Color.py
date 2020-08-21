# Create a program that changes screen colour from user input (mouse click)
import os
import sys
import random

import pygame as pg

CAPTION = "Click to change colour"
SCREEN_SIZE = (500, 500)

class App(object):

    def __init__(self):
        self.screen = pg.display.get_surface() #Get reference to display
        self.clock = pg.time.Clock()  #Create clock to restrict frame rate
        self.fps = 60
        self.done = False
        self.keys = pg.key.get_pressed() #All keys pressed
        self.colour = pg.Color("black")
    
    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or self.keys[pg.K_ESCAPE]:
                self.done == True
            elif event.type == pg.MOUSEBUTTONDOWN:
                self.colour = [random.randint(0, 255) for _ in range(3)]
            elif event.type in (pg.KEYUP, pg.KEYDOWN):
                self.key = pg.key.get_pressed()

    def main_loop(self):
        while not self.done:
            self.event_loop()
            self.screen.fill(self.colour)
            pg.display.update()
            self.clock.tick(self.fps)

def main():
    os.environ['SDL_VIDEO_CENTERED'] = '1' # create the window
    pg.init()
    pg.display.set_caption(CAPTION)
    pg.display.set_mode(SCREEN_SIZE)
    App().main_loop()
    pg.quit()
    sys.exit()

if __name__ == "__main__":
    main()