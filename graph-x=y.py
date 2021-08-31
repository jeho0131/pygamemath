import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600,400))
fps = pygame.time.Clock()
size = screen.get_size()
dt = 0.001

px = size[0] // 4
py = size[1] // 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255,255,255))

    pygame.draw.line(screen, (0,0,0), (0, py), (size[0],py), 1)
    pygame.draw.line(screen, (0,0,0), (px, 0), (px, size[1]), 1)

    #np = py - (dt/2)
    pp = py
    pnmp = py

    for i in range(2, 500):
        pygame.draw.line(screen, (255,0,0), (px + i-1, pp), (px + i, np), 1)
        pygame.draw.line(screen, (0,0,255), (px + i-1, py - (((i-1)*(i-1))/2)/1000), (px + i, py - ((i*i)/2)/1000), 1)
        pygame.draw.line(screen, (0,255,0), (px + (i-1), pnmp), (px + i, np - pp), 1)
        pnmp = np - pp
        pp = np
        #np = py - (((i*i)*dt)/2)

    pygame.display.update()
    fps.tick(24)
    
