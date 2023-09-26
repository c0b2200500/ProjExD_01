import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01-20230926/fig/pg_bg.jpg")
    bg_img_r = pg.transform.flip(bg_img,True, False)
    kk_img = pg.image.load("ex01-20230926/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_img_r = pg.transform.rotozoom(kk_img, 10, 1.0)
    list2 =[kk_img,kk_img_r]
    tmr = 0
    x = tmr
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img_r, [(1600-x), 0])
        screen.blit(bg_img,[3200-x,0])
        if x == 3200:
            x = 0
        screen.blit(list2[(tmr//50)%2], [300, 200])
        pg.display.update()
        tmr += 1  
        x += 1
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()