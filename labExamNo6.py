import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_line(x1, y1, x2, y2):
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0) 
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()
