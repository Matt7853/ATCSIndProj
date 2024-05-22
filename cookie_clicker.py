import sys
import pygame as pg
import time as t
import math as m

class Building(object):
    def __init__(self, base_cost, base_cps, order, name):
        self.name = name
        self.cost = base_cost
        self.cps = base_cps
        self.ammount = 0
        self.is_hidden = True
        self.box = pg.Rect(760, order, 320, 40)

    def get_box(self):
        return self.box

    def get_cps(self):
        return self.cps
    
    def change_cps(self, factor):
        self.cps += (self.cps * factor)
    
    def get_price(self):
        return self.cost
    
    def get_number(self):
        return self.ammount
    
    def get_name(self):
        return self.name
    
    def locked(self):
        return self.is_hidden == True
    
    def buy_one(self):
        self.cost += (self.cost*0.15)
        self.ammount += 1
    
class Cursors(Building):
    def __init__(self, cost = 15, cps = 0.1, order = 0, name = "Cursor"):
        super().__init__(cost, cps, order, name)
        self.is_hidden = False

class Grandmama(Building):
    def __init__(self, cost = 100, cps = 1, order = 45, name = "Grandma"):
        super().__init__(cost, cps, order, name)
        

class Farm(Building):
    def __init__(self, cost = 1100, cps = 8, order = 90, name = "Farm"):
        super().__init__(cost, cps, order, name)
        

class Mine(Building):
    def __init__(self, cost = 12000, cps = 47, order = 135, name = "Mine"):
        super().__init__(cost, cps, order, name)
        

class Factory(Building):
    def __init__(self, cost = 130000, cps = 260, order = 180, name = "Factory"):
        super().__init__(cost, cps, order, name)
        

class Bank(Building):
    def __init__(self, cost = 1400000, cps = 1400, order = 225, name = "Bank"):
        super().__init__(cost, cps, order, name)
        

class Temple(Building):
    def __init__(self, cost = 20000000, cps = 7800, order = 270, name = "Temple"):
        super().__init__(cost, cps, order, name)
        

class Wizerd(Building):
    def __init__(self, cost = 330000000, cps = 44000, order = 315, name = "Tower"):
        super().__init__(cost, cps, order, name)
        

class Enterprise(Building):
    def __init__(self, cost = 5100000000, cps = 260000, order = 360, name = "Shipment"):
        super().__init__(cost, cps, order, name)
        

class PEChem(Building):
    def __init__(self, cost = 75000000000, cps = 1600000, order = 405, name = "Alchemist"):
        super().__init__(cost, cps, order, name)

class Sanchez(Building):
    def __init__(self, cost = 1000000000000, cps = 10000000, order = 450, name = "Portal"):
        super().__init__(cost, cps, order, name)

"""
def num_format(num, round_to=1):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num = round(num / 1000.0, round_to)
    return '{:.{}f}{}'.format(num, round_to, ['', '00', ' million', ' billion', ' trillion', 'T', 'P'][magnitude])
"""
# "{:.0f}".

def main():
    pg.init()
    screen = pg.display.set_mode((1080, 720))

    TOTAL_FONT = pg.freetype.Font("Verdana.ttf", 24)
    CPS_FONT = pg.freetype.Font("Verdana.ttf", 14)
    BLD_FONT = pg.freetype.Font("Verdana.ttf", 20)
    
    clock = pg.time.Clock()
    # A pygame.Rect to define the area.
    cookie = pg.Rect(20, 60, 250, 250)
    buildbox = pg.Rect(760, 0, 320, 490)

    dev_cookup = pg.Rect(300, 285, 10, 10)
    dev_cpup =  pg.Rect(315, 285, 10, 10)
    dev_cookdown = pg.Rect(300, 300, 10, 10)
    dev_cpdown =  pg.Rect(315, 300, 10, 10)

    global COOKIES
    COOKIES = 0
    global CPS
    CPS = 0

    done = False

    cursors = Cursors()
    grandmas = Grandmama()
    farms = Farm()
    mines = Mine()
    factories = Factory()
    banks = Bank()
    temples = Temple()
    towers = Wizerd()
    shipments = Enterprise()
    alchemists = PEChem()
    portals = Sanchez()
    buildings = [cursors, grandmas, farms, mines, factories, banks, temples, towers, shipments, alchemists, portals]
    
    time_start = t.time()

    while not done:
        if (t.time() - time_start) > 0.03:
            COOKIES += (CPS * 0.03)
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
                            if building.get_box().collidepoint(event.pos):
                                if COOKIES >= building.get_price():
                                    COOKIES -= building.get_price()
                                    CPS += building.get_cps()
                                    building.buy_one()
                    


        screen.fill((30, 30, 30))

        pg.draw.rect(screen, (0, 255, 0), dev_cookup)
        pg.draw.rect(screen, (0, 255, 0), dev_cpup)        
        pg.draw.rect(screen, (255, 0, 0), dev_cookdown)
        pg.draw.rect(screen, (255, 0, 0), dev_cpdown)


        pg.draw.rect(screen, (100, 200, 70), cookie)
        pg.draw.rect(screen, (0, 0, 255), buildbox)
        TOTAL_FONT.render_to(screen, (20, 15), ("{:.0f}".format(COOKIES) + " Cookies"), (255,255,255))
        CPS_FONT.render_to(screen, (20, 40), (str("{:.1f}".format(CPS)) + " Cookies Per Second"), (255,255,255))

        y_shift = 10
        for building in buildings:
            pg.draw.rect(screen, (255, 165, 0), building.get_box())
            BLD_FONT.render_to(screen, (770, y_shift), (str(building.get_number())), (255,255,255))
            BLD_FONT.render_to(screen, (790, y_shift), (str(building.get_name())), (255,255,255))
            BLD_FONT.render_to(screen, (900, y_shift), ((str(m.ceil(building.get_price())))), (95,0,160))
            y_shift += 45



        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    sys.exit()
