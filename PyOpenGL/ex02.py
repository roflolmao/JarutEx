# -*- coding: UTF-8 -*-
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
def render():
    glBegin(GL_LINES)
    # Line No.1
    glColor3f(1.0,0.0,0.0)
    glVertex2f(-0.5, -0.5)
    glColor3f(0.0,1.0,0.0)
    glVertex2f( 0.0,  0.5)
    # Line No.2
    glColor3f(0.0,1.0,0.0)
    glVertex2f( 0.0,  0.5)
    glColor3f(0.0,0.0,1.0)
    glVertex2f( 0.5, -0.5)
    # Line No.3
    glColor3f(0.0,0.0,1.0)
    glVertex2f( 0.5, -0.5)
    glColor3f(1.0,0.0,0.0)
    glVertex2f(-0.5, -0.5)
    glEnd()

if __name__=="__main__":
    pygame.init()
    fpsClock = pygame.time.Clock()
    pygame.display.set_mode((320,240), pygame.DOUBLEBUF|pygame.OPENGL)
    pygame.display.set_caption("ex02")
    glViewport(0,0,320,240)
    gluOrtho2D(-1.0,1.0,1.0,-1.0)
    running = True
    while running:
        fpsClock.tick(30)
        glClearColor(1.0, 1.0, 1.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        render()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
    pygame.quit()
