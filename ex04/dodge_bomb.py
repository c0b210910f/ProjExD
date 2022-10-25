import pygame as pg
import sys
from random import randint

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600,900))
    scrn_rct = scrn_sfc.get_rect()

    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()#練習問題１

    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400

    bomb_sfc = pg.Surface((20,20))
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10)
    bomb_rct = tori_sfc.get_rect()
    bomb_rct.centerx, bomb_rct.centery = randint(0, scrn_rct.width), randint(0, scrn_rct.height)

    clock = pg.time.Clock()

    while True:

        scrn_sfc.blit(bg_sfc, bg_rct)    

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return#練習問題２

        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP]:
            tori_rct.centery -= 1
        if key_states[pg.K_DOWN]:
            tori_rct.centery += 1
        if key_states[pg.K_LEFT]:
            tori_rct.centerx -= 1
        if key_states[pg.K_RIGHT]:
            tori_rct.centerx += 1
        
        scrn_sfc.blit(tori_sfc, tori_rct)#練習問題３
        scrn_sfc.blit(bomb_sfc, bomb_rct)#練習問題５
        
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
