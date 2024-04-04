# -*- coding: UTF-8 -*-
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
def draw_text(pos,text,color=(255,255,255,255),
              font_name="Tahoma",size=20):
    font = pygame.font.SysFont (font_name, size)
    text_face = font.render(text, True, color,(0,0,0,255))     
    text_buffer = pygame.image.tostring(text_face, "RGBA", True)     
    glRasterPos2d(*pos)
    glDrawPixels(text_face.get_width(), text_face.get_height(), 
                 GL_RGBA, GL_UNSIGNED_BYTE, text_buffer)
pygame.init()
fpsClock = pygame.time.Clock()
pygame.display.set_mode((800,600), pygame.DOUBLEBUF|pygame.OPENGL)
pygame.display.set_caption("Ex06)
glViewport(0,0,800,600)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluOrtho2D(-1.0,1.0,1.0,-1.0)
running = True
while running:
    fpsClock.tick(30)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    draw_text((-0.5, 0.0), "Hello, World!! สวัสดีชาวโลก",(255,255,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()
