import pygame,sys
from const import *
import copy

def indexe(a,elem):
    x=[]
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j]in (elem):
                x.append((i,j))
    return x

def countincomplete(a,elem):
    x=0
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j]== elem:
                x+=1
    return x



def moveleft(level,human):
    if level[indexe(level, human)[0][0]][indexe(level, human)[0][1] - 1] in ("p"):
        level[indexe(level, human)[0][0]][indexe(level, human)[0][1] - 1] = "e"
        if level[indexe(level, human)[1][0]][indexe(level, human)[1][1]] in ("i", "j", "k", "l"):
            level[indexe(level, human)[1][0]][indexe(level, human)[1][1]] = "o"
        else:
            level[indexe(level, human)[1][0]][indexe(level, human)[1][1]] = "p"
    elif level[indexe(level, human)[0][0]][indexe(level, human)[0][1] - 1] in ("o"):
        level[indexe(level, human)[0][0]][indexe(level, human)[0][1] - 1] = "i"
        if level[indexe(level, human)[1][0]][indexe(level, human)[1][1]] in ("i", "j", "k", "l"):
            level[indexe(level, human)[1][0]][indexe(level, human)[1][1]] = "o"
        else:
            level[indexe(level, human)[1][0]][indexe(level, human)[1][1]] = "p"
    elif level[indexe(level, human)[0][0]][indexe(level, human)[0][1] - 1] in ("s"):
        if level[indexe(level, human)[0][0]][indexe(level, human)[0][1] - 2] == "o":
            level[indexe(level, human)[0][0]][indexe(level, human)[0][1] - 2] = "s"
            level[indexe(level, human)[0][0]][indexe(level, human)[0][1] - 1] = "i"
            if level[indexe(level, human)[1][0]][indexe(level, human)[1][1]] in ("i", "j", "k", "l"):
                level[indexe(level, human)[1][0]][indexe(level, human)[1][1]] = "o"
            else:
                level[indexe(level, human)[1][0]][indexe(level, human)[1][1]] = "p"
        elif level[indexe(level, human)[0][0]][indexe(level, human)[0][1] - 2] == "p":
            level[indexe(level, human)[0][0]][indexe(level, human)[0][1] - 2] = "c"
            level[indexe(level, human)[0][0]][indexe(level, human)[0][1] - 1] = "i"
            if level[indexe(level, human)[1][0]][indexe(level, human)[1][1]] in ("i", "j", "k", "l"):
                level[indexe(level, human)[1][0]][indexe(level, human)[1][1]] = "o"
            else:
                level[indexe(level, human)[1][0]][indexe(level, human)[1][1]] = "p"
    elif level[indexe(level, human)[0][0]][indexe(level, human)[0][1] - 1] in ("c"):
        if level[indexe(level, human)[0][0]][indexe(level, human)[0][1] - 2] == "o":
            level[indexe(level, human)[0][0]][indexe(level, human)[0][1] - 2] = "s"
            level[indexe(level, human)[0][0]][indexe(level, human)[0][1] - 1] = "e"
            if level[indexe(level, human)[1][0]][indexe(level, human)[1][1]] in ("i", "j", "k", "l"):
                level[indexe(level, human)[1][0]][indexe(level, human)[1][1]] = "o"
            else:
                level[indexe(level, human)[1][0]][indexe(level, human)[1][1]] = "p"
        elif level[indexe(level, human)[0][0]][indexe(level, human)[0][1] - 2] == "p":
            level[indexe(level, human)[0][0]][indexe(level, human)[0][1] - 2] = "c"
            level[indexe(level, human)[0][0]][indexe(level, human)[0][1] - 1] = "e"
            if level[indexe(level, human)[1][0]][indexe(level, human)[1][1]] in ("i", "j", "k", "l"):
                level[indexe(level, human)[1][0]][indexe(level, human)[1][1]] = "o"
            else:
                level[indexe(level, human)[1][0]][indexe(level, human)[1][1]] = "p"

    return level



def moveright(level,human):
    if level[indexe(level, human)[0][0]][indexe(level, human)[0][1] + 1] in ("p"):
        level[indexe(level, human)[0][0]][indexe(level, human)[0][1] + 1] = "g"
        if level[indexe(level, human)[0][0]][indexe(level, human)[0][1]] in ("i", "j", "k", "l"):
            level[indexe(level, human)[0][0]][indexe(level, human)[0][1]] = "o"
        else:
            level[indexe(level, human)[0][0]][indexe(level, human)[0][1]] = "p"
    elif level[indexe(level, human)[0][0]][indexe(level, human)[0][1] + 1] in ("o"):
        level[indexe(level, human)[0][0]][indexe(level, human)[0][1] + 1] = "k"
        if level[indexe(level, human)[0][0]][indexe(level, human)[0][1]] in ("i", "j", "k", "l"):
            level[indexe(level, human)[0][0]][indexe(level, human)[0][1]] = "o"
        else:
            level[indexe(level, human)[0][0]][indexe(level, human)[0][1]] = "p"
    elif level[indexe(level, human)[0][0]][indexe(level, human)[0][1] + 1] in ("s"):
        if level[indexe(level, human)[0][0]][indexe(level, human)[0][1] + 2] == "o":
            level[indexe(level, human)[0][0]][indexe(level, human)[0][1] + 2] = "s"
            level[indexe(level, human)[0][0]][indexe(level, human)[0][1] + 1] = "k"
            if level[indexe(level, human)[0][0]][indexe(level, human)[0][1]] in ("i", "j", "k", "l"):
                level[indexe(level, human)[0][0]][indexe(level, human)[0][1]] = "o"
            else:
                level[indexe(level, human)[0][0]][indexe(level, human)[0][1]] = "p"
        elif level[indexe(level, human)[0][0]][indexe(level, human)[0][1] + 2] == "p":
            level[indexe(level, human)[0][0]][indexe(level, human)[0][1] + 2] = "c"
            level[indexe(level, human)[0][0]][indexe(level, human)[0][1] + 1] = "k"
            if level[indexe(level, human)[0][0]][indexe(level, human)[0][1]] in ("i", "j", "k", "l"):
                level[indexe(level, human)[0][0]][indexe(level, human)[0][1]] = "o"
            else:
                level[indexe(level, human)[0][0]][indexe(level, human)[0][1]] = "p"
    elif level[indexe(level, human)[0][0]][indexe(level, human)[0][1] + 1] in ("c"):
        if level[indexe(level, human)[0][0]][indexe(level, human)[0][1] + 2] == "o":
            level[indexe(level, human)[0][0]][indexe(level, human)[0][1] + 2] = "s"
            level[indexe(level, human)[0][0]][indexe(level, human)[0][1] + 1] = "g"
            if level[indexe(level, human)[0][0]][indexe(level, human)[0][1]] in ("i", "j", "k", "l"):
                level[indexe(level, human)[0][0]][indexe(level, human)[0][1]] = "o"
            else:
                level[indexe(level, human)[1][0]][indexe(level, human)[1][1]] = "p"
        elif level[indexe(level, human)[0][0]][indexe(level, human)[0][1] + 2] == "p":
            level[indexe(level, human)[0][0]][indexe(level, human)[0][1] + 2] = "c"
            level[indexe(level, human)[0][0]][indexe(level, human)[0][1] + 1] = "g"
            if level[indexe(level, human)[0][0]][indexe(level, human)[0][1]] in ("i", "j", "k", "l"):
                level[indexe(level, human)[0][0]][indexe(level, human)[0][1]] = "o"
            else:
                level[indexe(level, human)[0][0]][indexe(level, human)[0][1]] = "p"


    return level

def moveup(level,human):
    if level[indexe(level, human)[0][0]-1][indexe(level, human)[0][1]] in ("p"):
        level[indexe(level, human)[0][0]- 1][indexe(level, human)[0][1] ] = "f"
        if level[indexe(level, human)[1][0]][indexe(level, human)[1][1]] in ("i", "j", "k", "l"):
            level[indexe(level, human)[1][0]][indexe(level, human)[1][1]] = "o"
        else:
            level[indexe(level, human)[1][0]][indexe(level, human)[1][1]] = "p"
    elif level[indexe(level, human)[0][0] - 1][indexe(level, human)[0][1]] in ("o"):
        level[indexe(level, human)[0][0] - 1][indexe(level, human)[0][1]] = "j"
        if level[indexe(level, human)[1][0]][indexe(level, human)[1][1]] in ("i", "j", "k", "l"):
            level[indexe(level, human)[1][0]][indexe(level, human)[1][1]] = "o"
        else:
            level[indexe(level, human)[1][0]][indexe(level, human)[1][1]] = "p"
    elif level[indexe(level, human)[0][0] - 1][indexe(level, human)[0][1]] in ("s"):
        if level[indexe(level, human)[0][0] - 2][indexe(level, human)[0][1]] == "o":
            level[indexe(level, human)[0][0] - 2][indexe(level, human)[0][1]] = "s"
            level[indexe(level, human)[0][0] - 1][indexe(level, human)[0][1]] = "j"
            if level[indexe(level, human)[1][0]][indexe(level, human)[1][1]] in ("i", "j", "k", "l"):
                level[indexe(level, human)[1][0]][indexe(level, human)[1][1]] = "o"
            else:
                level[indexe(level, human)[1][0]][indexe(level, human)[1][1]] = "p"
        elif level[indexe(level, human)[0][0] - 2][indexe(level, human)[0][1]] == "p":
            level[indexe(level, human)[0][0] - 2][indexe(level, human)[0][1]] = "c"
            level[indexe(level, human)[0][0]- 1][indexe(level, human)[0][1] ] = "j"
            if level[indexe(level, human)[1][0]][indexe(level, human)[1][1]] in ("i", "j", "k", "l"):
                level[indexe(level, human)[1][0]][indexe(level, human)[1][1]] = "o"
            else:
                level[indexe(level, human)[1][0]][indexe(level, human)[1][1]] = "p"
    elif level[indexe(level, human)[0][0]-1][indexe(level, human)[0][1]] in ("c"):
        if level[indexe(level, human)[0][0] - 2][indexe(level, human)[0][1]] == "o":
            level[indexe(level, human)[0][0]- 2][indexe(level, human)[0][1] ] = "s"
            level[indexe(level, human)[0][0]- 1][indexe(level, human)[0][1] ] = "f"
            if level[indexe(level, human)[1][0]][indexe(level, human)[1][1]] in ("i", "j", "k", "l"):
                level[indexe(level, human)[1][0]][indexe(level, human)[1][1]] = "o"
            else:
                level[indexe(level, human)[1][0]][indexe(level, human)[1][1]] = "p"
        elif level[indexe(level, human)[0][0] - 2][indexe(level, human)[0][1]] == "p":
            level[indexe(level, human)[0][0]- 2][indexe(level, human)[0][1] ] = "c"
            level[indexe(level, human)[0][0] - 1][indexe(level, human)[0][1]] = "f"
            if level[indexe(level, human)[1][0]][indexe(level, human)[1][1]] in ("i", "j", "k", "l"):
                level[indexe(level, human)[1][0]][indexe(level, human)[1][1]] = "o"
            else:
                level[indexe(level, human)[1][0]][indexe(level, human)[1][1]] = "p"

    return level

def movedown(level,human):
    if level[indexe(level, human)[0][0]+1][indexe(level, human)[0][1]] in ("p"):
        level[indexe(level, human)[0][0]+ 1][indexe(level, human)[0][1] ] = "h"
        if level[indexe(level, human)[0][0]][indexe(level, human)[0][1]] in ("i", "j", "k", "l"):
            level[indexe(level, human)[0][0]][indexe(level, human)[0][1]] = "o"
        else:
            level[indexe(level, human)[0][0]][indexe(level, human)[0][1]] = "p"
    elif level[indexe(level, human)[0][0] + 1][indexe(level, human)[0][1]] in ("o"):
        level[indexe(level, human)[0][0] + 1][indexe(level, human)[0][1]] = "l"
        if level[indexe(level, human)[0][0]][indexe(level, human)[0][1]] in ("i", "j", "k", "l"):
            level[indexe(level, human)[0][0]][indexe(level, human)[0][1]] = "o"
        else:
            level[indexe(level, human)[0][0]][indexe(level, human)[0][1]] = "p"
    elif level[indexe(level, human)[0][0] + 1][indexe(level, human)[0][1]] in ("s"):
        if level[indexe(level, human)[0][0] + 2][indexe(level, human)[0][1]] == "o":
            level[indexe(level, human)[0][0] + 2][indexe(level, human)[0][1]] = "s"
            level[indexe(level, human)[0][0] + 1][indexe(level, human)[0][1]] = "l"
            if level[indexe(level, human)[0][0]][indexe(level, human)[0][1]] in ("i", "j", "k", "l"):
                level[indexe(level, human)[0][0]][indexe(level, human)[0][1]] = "o"
            else:
                level[indexe(level, human)[1][0]][indexe(level, human)[1][1]] = "p"
        elif level[indexe(level, human)[0][0] + 2][indexe(level, human)[0][1]] == "p":
            level[indexe(level, human)[0][0] + 2][indexe(level, human)[0][1]] = "c"
            level[indexe(level, human)[0][0]+ 1][indexe(level, human)[0][1] ] = "l"
            if level[indexe(level, human)[0][0]][indexe(level, human)[0][1]] in ("i", "j", "k", "l"):
                level[indexe(level, human)[0][0]][indexe(level, human)[0][1]] = "o"
            else:
                level[indexe(level, human)[0][0]][indexe(level, human)[0][1]] = "p"
    elif level[indexe(level, human)[0][0]+1][indexe(level, human)[0][1]] in ("c"):
        if level[indexe(level, human)[0][0] + 2][indexe(level, human)[0][1]] == "o":
            level[indexe(level, human)[0][0]+ 2][indexe(level, human)[0][1] ] = "s"
            level[indexe(level, human)[0][0]+ 1][indexe(level, human)[0][1] ] = "h"
            if level[indexe(level, human)[0][0]][indexe(level, human)[0][1]] in ("i", "j", "k", "l"):
                level[indexe(level, human)[0][0]][indexe(level, human)[0][1]] = "o"
            else:
                level[indexe(level, human)[0][0]][indexe(level, human)[0][1]] = "p"
        elif level[indexe(level, human)[0][0] + 2][indexe(level, human)[0][1]] == "p":
            level[indexe(level, human)[0][0]+ 2][indexe(level, human)[0][1] ] = "c"
            level[indexe(level, human)[0][0] + 1][indexe(level, human)[0][1]] = "h"
            if level[indexe(level, human)[0][0]][indexe(level, human)[0][1]] in ("i", "j", "k", "l"):
                level[indexe(level, human)[0][0]][indexe(level, human)[0][1]] = "o"
            else:
                level[indexe(level, human)[0][0]][indexe(level, human)[0][1]] = "p"

    return level

def printmap(screen,level):
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j]=="x":
                screen.blit(wall,[width_field*j,width_field*i])
            elif level[i][j]=="o":
                screen.blit(ground, [width_field * j, width_field * i])
            elif level[i][j]=="s":
                screen.blit(store, [width_field * j, width_field * i])
            elif level[i][j]=="p":
                screen.blit(object, [width_field * j, width_field * i])
            elif level[i][j] == "c":
                screen.blit(object_store, [width_field * j, width_field * i])
            elif level[i][j] == "i":
                screen.blit(mover_left, [width_field * j, width_field * i])
            elif level[i][j] == "j":
                screen.blit(mover_up, [width_field * j, width_field * i])
            elif level[i][j] == "k":
                screen.blit(mover_right, [width_field * j, width_field * i])
            elif level[i][j] == "l":
                screen.blit(mover_down, [width_field * j, width_field * i])
            elif level[i][j] == "e":
                screen.blit(store_left, [width_field * j, width_field * i])
            elif level[i][j] == "f":
                screen.blit(store_up, [width_field * j, width_field * i])
            elif level[i][j] == "g":
                screen.blit(store_right, [width_field * j, width_field * i])
            elif level[i][j] == "h":
                screen.blit(store_down, [width_field * j, width_field * i])
    return None
