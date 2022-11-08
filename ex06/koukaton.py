import pygame as pg
import sys
from random import randint


key_delta = {
    pg.K_UP:    [0, -1],
    pg.K_DOWN:  [0, +1],
    pg.K_LEFT:  [-1, 0],
    pg.K_RIGHT: [+1, 0],
}


#画面外に行くのを防止するため
def check_bound(obj_rct, scr_rct):

    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate


def main():
    score = 0
    time = int(pg.time.get_ticks () /1000)

    #フォントの用意  
    font1 = pg.font.SysFont("hg正楷書体pro", 75)
    
    #スコアのテキスト
    text1 = font1.render("スコア："+str(score), True, (0, 0, 0))

    # 練習1
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()
    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()
    

    # 練習3
    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400

    # 練習5
    bomb_sfc = pg.Surface((20, 20)) # 空のSurface
    bomb_sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10) # 円を描く
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = randint(0, scrn_rct.width)
    bomb_rct.centery = randint(0, scrn_rct.height)

    #餌の生成
    esa_sfc = pg.Surface((20, 20)) 
    esa_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(esa_sfc, (255, 255, 0), (10, 10), 10)
    esa_rct = esa_sfc.get_rect()
    esa_rct.centerx = randint(0, scrn_rct.width)
    esa_rct.centery = randint(0, scrn_rct.height)

    # 練習6
    vx, vy = +1, +1


    clock = pg.time.Clock() # 練習1
    while True:
        #timeの再設定
        time = int(pg.time.get_ticks() / 1000)
        text2 = font1.render("タイム："+str(time), True, (0, 0, 0))

        scrn_sfc.blit(bg_sfc, bg_rct) # 練習2
        
        for event in pg.event.get(): # 練習2
            if event.type == pg.QUIT:
                return

        key_states = pg.key.get_pressed()
        for key, delta in key_delta.items():
            if key_states[key]:
                tori_rct.centerx += delta[0]
                tori_rct.centery += delta[1]
                # 練習7
                if check_bound(tori_rct, scrn_rct) != (+1, +1):
                    tori_rct.centerx -= delta[0]
                    tori_rct.centery -= delta[1]
        scrn_sfc.blit(tori_sfc, tori_rct) # 練習3

        # 練習7
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko
        vy *= tate
        bomb_rct.move_ip(vx, vy) # 練習6
        scrn_sfc.blit(bomb_sfc, bomb_rct) # 練習5
        scrn_sfc.blit(esa_sfc, esa_rct)#餌の表示
        scrn_sfc.blit(text1, (0, 0))#スコアの表示
        scrn_sfc.blit(text2, (0, 80))#タイマーの表示

        #スコアの更新と餌の再配置
        if tori_rct.colliderect(esa_rct):
            score +=1
            text1 = font1.render("スコア：" + str(score), True, (0, 0, 0))
            esa_rct.centerx = randint(0, scrn_rct.width)
            esa_rct.centery = randint(0, scrn_rct.height)
            scrn_sfc.blit(esa_sfc, esa_rct)

        # 練習8
        if tori_rct.colliderect(bomb_rct): # こうかとんrctが爆弾rctと重なったら
            return

        pg.display.update() #練習2
        clock.tick(1000)

if __name__ == "__main__":
    pg.init() # 初期化
    main() # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()