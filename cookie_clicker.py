import sys
import pygame as pg
import time as t

class Building(object):
    def __init__(self, base_cost, base_cps):
        self.cost = base_cost
        self.cps = base_cps
        self.ammount = 0
        self.is_hidden = True

    def get_cps(self):
        return self.cps
    
    def get_price(self):
        return self.cost
    
    def get_number(self):
        return self.ammount
    

    def buy_one(self):
        self.cost += (self.cost*0.15)
        self.ammount += 1
    
class Cursors(Building):
    def __init__(self, cost = 15, cps = 1):
        super().__init__(cost, cps)
        self.is_hidden = False
class Grandmama(Building):
    def __init__(self, cost = 15, cps = 1):
        super().__init__(cost, cps)
        self.is_hidden = False


def main():
    pg.init()
    screen = pg.display.set_mode((1080, 720))

    TOTAL_FONT = pg.freetype.Font("Verdana.ttf", 24)
    CPS_FONT = pg.freetype.Font("Verdana.ttf", 14)
    BLD_FONT = pg.freetype.Font("Verdana.ttf", 20)
    
    clock = pg.time.Clock()
    # A pygame.Rect to define the area.
    cookie = pg.Rect(20, 60, 250, 250)
    cursor = pg.Rect(880, 0, 200, 40)

    global COOKIES
    COOKIES = 0
    global CPS
    CPS = 0

    done = False

    cursors = Cursors()
    time_start = t.time()

    while not done:
        if (t.time() - time_start) > .05:
            COOKIES += (CPS * .05)
            time_start = t.time()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button.
                    # Check if the rect collides with the mouse pos.
                    if cookie.collidepoint(event.pos):
                        COOKIES += 1
                    if cursor.collidepoint(event.pos):
                        if COOKIES >= cursors.get_price():
                            COOKIES -= cursors.get_price()
                            CPS += cursors.get_cps()
                            cursors.buy_one()


        screen.fill((30, 30, 30))
        pg.draw.rect(screen, (100, 200, 70), cookie)
        pg.draw.rect(screen, (255, 165, 0), cursor)

        TOTAL_FONT.render_to(screen, (20, 15), ("{:.2f}".format(COOKIES) + " Cookies"), (255,255,255))
        CPS_FONT.render_to(screen, (20, 40), (str(CPS) + " Cookies Per Second"), (255,255,255))
        BLD_FONT.render_to(screen, (890, 10), (str(cursors.get_number())), (255,255,255))
        BLD_FONT.render_to(screen, (990, 10), ("{:.2f}".format(cursors.get_price())), (255,255,255))


        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    sys.exit()
