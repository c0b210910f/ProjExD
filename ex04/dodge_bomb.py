import pygame as pg
import sys
from random import randint

def check_bound(obj_rct, scr_rct): #当たり判定のための関数
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate =  -1
    return yoko, tate


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600,900))
    scrn_rct = scrn_sfc.get_rect()

    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()#練習問題１

    go_sfc = pg.image.load("fig/go.jpeg") #ゲームオーバーの画像
    go_rct = go_sfc.get_rect()

    gc_sfc = pg.image.load("fig/gc.png") #ゲームクリアの画像
    gc_rct = gc_sfc.get_rect()

    tori_sfc = pg.image.load("fig/6.png") #こうかとんの画像
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400

    bomb_sfc = pg.Surface((20,20)) #爆弾
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx, bomb_rct.centery = randint(0, scrn_rct.width), randint(0, scrn_rct.height)

    bomb_sfc2 = pg.Surface((20,20)) #爆弾2
    bomb_sfc2.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc2, (0, 0, 255), (10, 10), 10)
    bomb_rct2 = bomb_sfc2.get_rect()
    bomb_rct2.centerx, bomb_rct2.centery = randint(0, scrn_rct.width), randint(0, scrn_rct.height)

    vx, vy = +1, +1
    vx2, vy2 = +1, +1

    clock = pg.time.Clock()

    while True:

        scrn_sfc.blit(bg_sfc, bg_rct)    

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return#練習問題２

        key_states = pg.key.get_pressed() #こうかとんの移動
        if key_states[pg.K_UP]:
            tori_rct.centery -= 1
        if key_states[pg.K_DOWN]:
            tori_rct.centery += 1
        if key_states[pg.K_LEFT]:
            tori_rct.centerx -= 1
        if key_states[pg.K_RIGHT]:
            tori_rct.centerx += 1
        
        yoko, tate = check_bound(tori_rct, scrn_rct) #こうかとんが画面外に行くのを防止
        if yoko == -1:
            if key_states[pg.K_LEFT]:
                tori_rct.centerx += 1
            if key_states[pg.K_RIGHT]:
                tori_rct.centerx -= 1
        if tate == -1:
            if key_states[pg.K_UP]:
                tori_rct.centery += 1
            if key_states[pg.K_DOWN]:
                tori_rct.centery -= 1
        scrn_sfc.blit(tori_sfc, tori_rct)#練習問題３

        yoko, tate = check_bound(bomb_rct, scrn_rct) #爆弾の壁反射と加速
        vx *=yoko
        vy *=tate
        if vx < 0:
            vx -=0.001
        if vx > 0:
            vx +=0.001
        if vy < 0:
            vy -=0.001
        if vy > 0:
            vy +=0.001
        
        yoko, tate = check_bound(bomb_rct2, scrn_rct)
        vx2 *=yoko
        vy2 *=tate
        if vx2 < 0:
            vx2 -=0.001
        if vx2 > 0:
            vx2 +=0.001
        if vy2 < 0:
            vy2 -=0.001
        if vy2 > 0:
            vy2 +=0.001

        bomb_rct.move_ip(vx, vy)
        scrn_sfc.blit(bomb_sfc, bomb_rct)#練習問題５

        bomb_rct2.move_ip(vx2, vy2)
        scrn_sfc.blit(bomb_sfc2, bomb_rct2)

        if tori_rct.colliderect(bomb_rct): #爆弾に当たった時の処理
            scrn_sfc.blit(go_sfc, go_rct)
            pg.display.update()
            clock.tick(0.25)
            return
        if tori_rct.colliderect(bomb_rct2):
            scrn_sfc.blit(go_sfc, go_rct)
            pg.display.update()
            clock.tick(0.25)
            return

        time = pg.time.get_ticks()/1000
        if time > 10:                        #ゲームクリアの処理
            scrn_sfc.blit(gc_sfc, gc_rct)
            pg.display.update()
            clock.tick(0.25)
            return


        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()

    sys.exit()
