# -*- coding: UTF-8 -*-
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
vertices = ((-1,  1, -1),
            ( 1,  1, -1),
            ( 1, -1, -1),
            (-1, -1, -1),
            (-1,  1,  1),
            ( 1,  1,  1),
            ( 1, -1,  1),
            (-1, -1,  1))
colors = (  (1.0,0.0,0.0),
            (0.0,1.0,0.0),
            (0.0,0.0,1.0),
            (1.0,1.0,1.0),
            (1.0,0.0,0.0),
            (0.0,1.0,0.0),
            (0.0,0.0,1.0),
            (1.0,1.0,1.0))
cube = (    (0,1,2), #front
            (2,3,0),
            (1,0,4), # top
            (4,5,1),
            (3,2,6), # bottom
            (6,7,3),
            (4,0,3), # Left
            (3,7,4),
            (1,5,6), # right
            (6,2,1),
            (5,4,7), # back
            (7,6,5))
def draw3D(obj):
    glBegin(GL_TRIANGLES)
    for edge in obj:
        for v in edge:
            glColor3fv(colors[v])
            glVertex3fv(vertices[v])
    glEnd()
pygame.init()
fpsClock = pygame.time.Clock()
ratio = 8.0/6.0
pygame.display.set_mode((800,600), pygame.DOUBLEBUF|pygame.OPENGL)
pygame.display.set_caption("Ex4.4")
glViewport(0,0,800,600)
running = True
gluPerspective(30.0, ratio, 0.1, 50.0)
glTranslatef(0.0, 0.0, -10.0)
glClearColor(0.0, 0.0, 0.0, 1.0)
glEnable(GL_DEPTH_TEST)
while running:
    fpsClock.tick(30)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef( 1, 1, 1, 1)
    draw3D(cube)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()
