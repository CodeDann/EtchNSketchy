import sys
import turtle
import pygame as pg
from pygame.locals import *

pg.init()
currPos = [200, 500]
endPos = [100, 100]
currColor = 'grey'
modifier = 10
fps = 60
fpsClock = pg.time.Clock()

width, height = 949, 774
screen = pg.display.set_mode((width, height))
screen.fill((255, 255, 255))
bg = pg.image.load('etch_n_sketchy.png')
wm = pg.image.load('welcome_message.png')

def updatePos( current_position, indicator):
    fullMove = 50
    halfMove = 25
    if indicator == 1: #UP
        return [current_position[0], current_position[1] - fullMove]
    elif indicator == 2: #Right
        return [current_position[0] + fullMove, current_position[1]]
    elif indicator == 3: #Left
        return [current_position[0] - fullMove, current_position[1]]
    elif indicator == 4: #Down
        return [current_position[0], current_position[1] + fullMove]
    elif indicator == 5: #UpHalf
        return [current_position[0], current_position[1] - halfMove]
    elif indicator == 6: #DownHalf
        return [current_position[0], current_position[1] + halfMove]
    elif indicator == 7: #RightHalf
        return [current_position[0] + halfMove, current_position[1]]
    elif indicator == 8: #LeftHalf
        return [current_position[0] - halfMove, current_position[1]]


screen.blit(wm, (100,100))
while True:
    screen.blit(bg, (0, 0))
    for event in pg.event.get():
        pressed_keys = pg.key.get_pressed()
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif pressed_keys[K_UP] and pressed_keys[K_LSHIFT]:
            newPos = updatePos(currPos, 5)
            pg.draw.line(screen, currColor, currPos, newPos)
            currPos = newPos
        elif pressed_keys[K_DOWN] and pressed_keys[K_LSHIFT]:
            newPos = updatePos(currPos, 6)
            pg.draw.line(screen, currColor, currPos, newPos)
            currPos = newPos
        elif pressed_keys[K_RIGHT] and pressed_keys[K_LSHIFT]:
            newPos = updatePos(currPos, 7)
            pg.draw.line(screen, currColor, currPos, newPos)
            currPos = newPos
        elif pressed_keys[K_LEFT] and pressed_keys[K_LSHIFT]:
            newPos = updatePos(currPos, 8)
            pg.draw.line(screen, currColor, currPos, newPos)
            currPos = newPos
        elif pressed_keys[K_UP]:
            newPos = updatePos(currPos, 1)
            pg.draw.line(screen, currColor,  currPos, newPos)
            currPos = newPos
        elif pressed_keys[K_DOWN]:
            newPos = updatePos(currPos, 4)
            pg.draw.line(screen, currColor,  currPos, newPos)
            currPos = newPos
        elif pressed_keys[K_LEFT]:
            newPos = updatePos(currPos, 3)
            pg.draw.line(screen, currColor,  currPos, newPos)
            currPos = newPos
        elif pressed_keys[K_RIGHT]:
            newPos = updatePos(currPos, 2)
            pg.draw.line(screen, currColor,  currPos, newPos)
            currPos = newPos
        elif pressed_keys[K_1]:
            currColor = 'orange'
        elif pressed_keys[K_2]:
            currColor = 'purple'
        elif pressed_keys[K_3]:
            currColor = 'green'
        elif pressed_keys[K_4]:
            currColor = 'blue'
        elif pressed_keys[K_5]:
            screen.fill((255, 255, 255))



    pg.display.flip()
    fpsClock.tick(fps)




