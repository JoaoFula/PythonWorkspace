# Create a dragable box
import os
import sys
import pygame as pg

CAPTION = "Drag the Red Box"
SCREEN_SIZE = (1000, 600)

class character(object):
    SIZE = (150, 150)
    def __init__(self, pos):
        self.rect = pg.Rect((0,0), character.SIZE)
        self.rect.center = pos 
        self.text, self.text_rect = self.setup_font()
        self.click = False

    def setup_font(self):
        font = pg.font.SysFont('timesnewroman', 30)
        message = "I'm a red square"
        label = font.render(message, True, pg.Color("White"))
        label_rect = label.get_rect()
        return label, label_rect

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            self.click = True
            pg.mouse.get_rel()
    
    def update(self, screen_rect):
        if self.click:
            self.rect.move_ip(pg.mouse.get_rel())
            self.rect.clamp_ip(screen_rect)
            self.text_rect.center = (self.rect.centerx, self.rect.centery + 90)

    def draw(self, surface):
        surface.fill(pg.Color("Red"), self.rect)
        surface.blit(self.text, self.text_rect)

class App(object):
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.fps = 60
        self.done = False
        self.keys = pg.key.get_pressed()
        self.player = character(self.screen_rect.center)

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or self.keys[pg.K_ESCAPE]:
                self.done = True
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                self.player.check_click(event.pos)
            elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
                self.player.click = False
            elif event.type in (pg.KEYUP, pg.KEYDOWN):
                self.keys == pg.key.get_pressed()

    def render(self):
        self.screen.fill(pg.Color("black"))
        self.player.draw(self.screen)
        pg.display.update()

    def main_loop(self):
        while not self.done:
            self.event_loop()
            self.player.update(self.screen_rect)
            self.render()
            self.clock.tick(self.fps)

def main():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pg.init()
    pg.display.set_caption(CAPTION)
    pg.display.set_mode(SCREEN_SIZE)
    App().main_loop()
    pg.quit()
    sys.exit()

if __name__ == "__main__":
    main()