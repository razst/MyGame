import pygame
import sys
from pygame.locals import *

clock = pygame.time.Clock()
screen = pygame.display.set_mode((562,600))

bg = pygame.image.load("bg.jpg")
car = pygame.image.load("car.png")


# car_x = screen.get_width()/2 - car.get_size()(0)/2

# screen.blit(ship, (ship_left,ship_top))


pygame.display.set_caption('car racer')

while True:
    clock.tick(60)

    screen.blit(bg,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()