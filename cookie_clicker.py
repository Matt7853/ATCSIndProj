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
    
    def change_cps(self, factor):
        self.cps += (self.cps * factor)
    
    def get_price(self):
        return self.cost
    
    def get_number(self):
        return self.ammount
    
    def locked(self):
        return self.is_hidden == True
    
    def buy_one(self):
        self.cost += (self.cost*0.15)
        self.ammount += 1
    
class Cursors(Building):
    def __init__(self, cost = 15, cps = 1):
        super().__init__(cost, cps)
        self.is_hidden = False

class Grandmama(Building):
    def __init__(self, cost = 100, cps = 5):
        super().__init__(cost, cps)

class Farm(Building):
    def __init__(self, cost = 1000, cps = 25):
        super().__init__(cost, cps)


def main():
    pg.init()
    screen = pg.display.set_mode((1080, 720))

    TOTAL_FONT = pg.freetype.Font("Verdana.ttf", 24)
    CPS_FONT = pg.freetype.Font("Verdana.ttf", 14)
    BLD_FONT = pg.freetype.Font("Verdana.ttf", 20)
    
    clock = pg.time.Clock()
    # A pygame.Rect to define the area.
    cookie = pg.Rect(20, 60, 250, 250)
    buildbox = pg.Rect(880, 0, 200, 490)

    dev_cookup = pg.Rect(300, 285, 10, 10)
    dev_cpup =  pg.Rect(315, 285, 10, 10)
    dev_cookdown = pg.Rect(300, 300, 10, 10)
    dev_cpdown =  pg.Rect(315, 300, 10, 10)

    curs_box = pg.Rect(880, 0, 200, 40)
    grand_box = pg.Rect(880, 45, 200, 40)
    farm_box = pg.Rect(880, 90, 200, 40)

    global COOKIES
    COOKIES = 0
    global CPS
    CPS = 0

    done = False

    cursors = Cursors()
    grandmas = Grandmama()
    farms = Farm()
    
    time_start = t.time()

    while not done:
        if (t.time() - time_start) > 0.05:
            COOKIES += (CPS * 0.05)
            time_start = t.time()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button.
                    # Check if the rect collides with the mouse pos.
                    if dev_cookup.collidepoint(event.pos):
                        COOKIES += 100000
                    if dev_cpup.collidepoint(event.pos):
                        CPS += 100
                    if dev_cookdown.collidepoint(event.pos):
                        COOKIES -= 100000
                    if dev_cpdown.collidepoint(event.pos):
                        CPS -= 100

                    if cookie.collidepoint(event.pos):
                        COOKIES += 1
                    elif buildbox.collidepoint(event.pos):
                        for building in buildings:
                            if building[0].collidepoint(event.pos):
                                if COOKIES >= building[1].get_price():
                                    COOKIES -= building[1].get_price()
                                    CPS += building[1].get_cps()
                                    building[1].buy_one()
                    


        screen.fill((30, 30, 30))

        pg.draw.rect(screen, (0, 255, 0), dev_cookup)
        pg.draw.rect(screen, (0, 255, 0), dev_cpup)        
        pg.draw.rect(screen, (255, 0, 0), dev_cookdown)
        pg.draw.rect(screen, (255, 0, 0), dev_cpdown)


        pg.draw.rect(screen, (100, 200, 70), cookie)
        pg.draw.rect(screen, (0, 0, 255), buildbox)
        TOTAL_FONT.render_to(screen, (20, 15), ("{:.0f}".format(COOKIES) + " Cookies"), (255,255,255))
        CPS_FONT.render_to(screen, (20, 40), (str(CPS) + " Cookies Per Second"), (255,255,255))

        buildings = [[curs_box, cursors], [grand_box, grandmas], [farm_box, farms]]
        y_shift = 10
        for building in buildings:
            pg.draw.rect(screen, (255, 165, 0), building[0])
            BLD_FONT.render_to(screen, (890, y_shift), (str(building[1].get_number())), (255,255,255))
            BLD_FONT.render_to(screen, (990, y_shift), ("{:.2f}".format(building[1].get_price())), (255,255,255))
            y_shift += 45



        pg.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    sys.exit()
