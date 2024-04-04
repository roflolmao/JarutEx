# -*- coding: UTF-8 -*-
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
vertices = ((-0.5, 0.5),
            (0.5,0.5),
            (0.5,-0.5),
            (-0.5,-0.5))
colors = ((1.0,0.0,0.0),
          (0.0,1.0,0.0),
          (0.0,0.0,1.0),
          (1.0,1.0,1.0))
rect = ((0,1,2),(2,3,0))
def draw(obj):
    glBegin(GL_TRIANGLES)
    for edge in obj:
        for v in edge:
            glColor3fv(colors[v])
            glVertex2fv(vertices[v])
    glEnd()
pygame.init()
fpsClock = pygame.time.Clock()
pygame.display.set_mode((800,600), pygame.DOUBLEBUF|pygame.OPENGL)
pygame.display.set_caption("Ex04")
glViewport(0,0,800,600)
gluOrtho2D(-1.0,1.0,1.0,-1.0)
running = True
while running:
    fpsClock.tick(30)
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    draw(rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()
