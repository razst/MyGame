import pygame
import sys
from pygame.locals import *
import random

MOVE_SPEED = 30
MAX_PALYERS = 2
LEFT_LANE_X = 100
RIGHT_LANE_X = 380
PLAYER_SPEED = 1

clock = pygame.time.Clock()
screen = pygame.display.set_mode((562,600))

bg = pygame.image.load("bg.jpg")
car = pygame.image.load("car.png")
car_red = pygame.image.load("car_red.png")


car_x = screen.get_width()/2 + 10
car_y = screen.get_height() - car.get_size()[1]

players = []


def findTopPlayerY():
    global players
    min_y=screen.get_height()

    for car in players:
        if car[1]<min_y:
            min_y=car[1]
    return min_y 


# def removePlayers():
#     global players
#     for car in players:
#         if car[1]>screen.get_height()-car.get_size()[1]:
#             players.remove()
def generatePalyers():
    global players
    if (findTopPlayerY()> car.get_size()[1]) and (len(players)<MAX_PALYERS):
        x = random.randint(0,1)
        if x==0:
            x = random.randint(LEFT_LANE_X,LEFT_LANE_X+car.get_size()[0])
            players.append([x,0])
        else:
            x = random.randint(screen.get_width()/2 + 10,RIGHT_LANE_X)
            players.append([x,0])


def showPlayers():
    print(players)
    global screen
    for car in players:
        screen.blit(car_red, (car[0],car[1]))


def movePlayers():
    global players
    for car in players:
        car[1]+=PLAYER_SPEED

def check_boundries():
    global car_x
    if car_x<0:
        car_x=0
    if car_x>screen.get_width()-car.get_size()[0]:
        car_x = screen.get_width()-car.get_size()[0]




pygame.display.set_caption('Car racer')

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                car_x -= MOVE_SPEED
            elif event.key == K_RIGHT:
                car_x += MOVE_SPEED
    
    screen.blit(bg,(0,0))
    movePlayers()
    generatePalyers()
    showPlayers()
    check_boundries()
    screen.blit(car, (car_x,car_y))


    pygame.display.update()