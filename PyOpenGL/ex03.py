# -*- coding: UTF-8 -*-
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
def draw_tri():
    glBegin(GL_TRIANGLES)
    glColor3f(1.0,0.0,0.0)
    glVertex2f(-0.5, -0.5)
    glColor3f(0.0,1.0,0.0)
    glVertex2f( 0.0,  0.5)
    glColor3f(0.0,0.0,1.0)
    glVertex2f( 0.5, -0.5)
    glEnd()
pygame.init()
fpsClock = pygame.time.Clock()
pygame.display.set_mode((800,600), pygame.DOUBLEBUF|pygame.OPENGL)
pygame.display.set_caption("Ex03")
glViewport(0,0,800,600)
gluOrtho2D(-1.0,1.0,1.0,-1.0)
running = True
glLineWidth(4)
glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
while running:
    fpsClock.tick(30)
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    draw_tri()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                glPointSize(5)
                glPolygonMode(GL_FRONT_AND_BACK, GL_POINT)
            if event.key == pygame.K_2:
                glLineWidth(4)
                glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
            if event.key == pygame.K_3:
                glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    pygame.display.flip()
pygame.quit()
