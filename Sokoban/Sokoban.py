from const import *
from function import *
import pygame,sys,copy

pygame.init()


level=[["x","x","x","x","x","x","x","x"],
       ["x","x","x","o","o","o","x","x"],
       ["x","p","l","s","o","o","x","x"],
       ["x","x","x","o","s","p","x","x"],
       ["x","p","x","x","s","o","x","x"],
       ["x","o","x","o","p","o","x","x"],
       ["x","s","o","c","s","s","p","x"],
       ["x","o","o","o","p","o","o","x"],
       ["x","x","x","x","x","x","x","x"]]


screen=pygame.display.set_mode((width_field*len(level[0]),width_field*len(level)+width_window_game))



restart=copy.deepcopy(level)
while True:


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit(0)
        elif event.type==pygame.KEYDOWN and event.key==pygame.K_LEFT:
             moveleft(level,human)
             moves+=1
        elif event.type==pygame.KEYDOWN and event.key==pygame.K_RIGHT:
            moveright(level,human)
            moves+=1
        elif event.type==pygame.KEYDOWN and event.key==pygame.K_UP:
            moveup(level,human)
            moves+=1
        elif event.type==pygame.KEYDOWN and event.key==pygame.K_DOWN:
            movedown(level,human)
            moves+=1
        elif event.type==pygame.KEYDOWN and event.key==pygame.K_r:
            level=restart
            moves=0
        elif countincomplete(level,"p")==0:
            grats = dispfont.render("Congratulations!" , 0, (120, 70, 0))
            screen.blit(grats, [int(width_field * len(level[0]) *3/4), width_field * len(level)])


    printmap(screen, level)

    czas = pygame.time.get_ticks() / 1000

    if seconds<czas:
        seconds+=1
    timer = dispfont.render("Time: " + str(seconds), 0, (120, 70, 0))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(0,width_field * len(level),width_field*len(level[0]),width_window_game,))
    screen.blit(timer, [0, width_field * len(level)])

    counter = dispfont.render("Moves: " + str(moves), 0, (120, 70, 0))
    screen.blit(counter, [int(width_field * len(level[0])/2), width_field * len(level)])


    pygame.display.flip()



