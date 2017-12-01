import pygame,sys,copy
pygame.init()

width_field=80
width_window_game=100
seconds=1
moves=0

dispfont = pygame.font.SysFont("Arial", 30)


human=["e","f","g","h","i","j","k","l"]

wall = pygame.image.load("wall.bmp")
wall = pygame.transform.scale(wall, (width_field,width_field))
store = pygame.image.load("store.bmp")
store = pygame.transform.scale(store, (width_field,width_field))
ground = pygame.image.load("ground.bmp")
ground = pygame.transform.scale(ground, (width_field,width_field))
object = pygame.image.load("object.bmp")
object = pygame.transform.scale(object, (width_field,width_field))
object_store = pygame.image.load("object_store.bmp")
object_store= pygame.transform.scale(object_store, (width_field,width_field))
mover_down = pygame.image.load("mover-down.bmp")
mover_down = pygame.transform.scale(mover_down, (width_field,width_field))
mover_up = pygame.image.load("mover-up.bmp")
mover_up = pygame.transform.scale(mover_up, (width_field,width_field))
mover_left = pygame.image.load("mover-left.bmp")
mover_left = pygame.transform.scale(mover_left, (width_field,width_field))
mover_right = pygame.image.load("mover-right.bmp")
mover_right = pygame.transform.scale(mover_right, (width_field,width_field))
store_right = pygame.image.load("store-right.bmp")
store_right = pygame.transform.scale(store_right, (width_field,width_field))
store_left = pygame.image.load("store-left.bmp")
store_left = pygame.transform.scale(store_left, (width_field,width_field))
store_up = pygame.image.load("store-up.bmp")
store_up = pygame.transform.scale(store_up, (width_field,width_field))
store_down = pygame.image.load("store-down.bmp")
store_down = pygame.transform.scale(store_down, (width_field,width_field))