import pygame
from pygame.locals import *
import sys
import time
import pyganim

pygame.init()

# set up the window
windowSurface = pygame.display.set_mode((320, 240), 0, 32)
pygame.display.set_caption('Pyganim Test 1')

# create the animation objects   ('filename of image',    duration_in_seconds)
boomAnim = pyganim.PygAnimation([('data/kaboom_frame1.png', 0.1),
                                 ('data/kaboom_frame2.png', 0.1),
                                 ('data/kaboom_frame3.png', 0.1),
                                 ('data/kaboom_frame4.png', 0.1),
                                 ('data/kaboom_frame5.png', 0.1),
                                 ('data/kaboom_frame6.png', 0.1),
                                 ('data/kaboom_frame7.png', 0.1)])
boomAnim.play() # there is also a pause() and stop() method

mainClock = pygame.time.Clock()
BGCOLOR = (0,0,0)
while True:
    windowSurface.fill(BGCOLOR)
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

    boomAnim.blit(windowSurface, (100, 50))

    pygame.display.update()
    mainClock.tick(30) # Feel free to experiment with any FPS setting.
