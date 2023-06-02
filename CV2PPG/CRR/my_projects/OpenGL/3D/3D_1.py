from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0) # установка цвета фона

def draw_cube():
    glBegin(GL_QUADS)
    # передняя грань
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f( 1.0, -1.0, 1.0)
    glVertex3f( 1.0,  1.0, 1.0)
    glVertex3f(-1.0,  1.0, 1.0)
    # задняя грань
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0,  1.0, -1.0)
    glVertex3f( 1.0,  1.0, -1.0)
    glVertex3f( 1.0, -1.0, -1.0)
    # правая грань
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f( 1.0, -1.0,  1.0)
    glVertex3f( 1.0, -1.0, -1.0)
    glVertex3f( 1.0,  1.0, -1.0)
    glVertex3f( 1.0,  1.0,  1.0)
    # левая грань
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0,  1.0)
    glVertex3f(-1.0,  1.0,  1.0)
    glVertex3f(-1.0,  1.0, -1.0)
    # верхняя грань
    glColor3f(0.0, 1.0, 1.0)
    glVertex3f(-1.0,  1.0,  1.0)
    glVertex3f( 1.0,  1.0,  1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    # нижняя грань
    glColor3f(1.0, 0.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f( 1.0, -1.0, -1.0)
    glVertex3f( 1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glEnd()

def draw_sphere():
    quad = gluNewQuadric()
    glColor3f(1.0, 1.0, 1.0)
    gluSphere(quad, 0.5, 20, 20)

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    draw_cube()
    glTranslatef(2.0, 0.0, 0.0)
    draw_sphere()
    glutSwapBuffers()

if __name__ == 'main':
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutCreateWindow("3D Primitives")
    glEnable(GL_DEPTH_TEST)
    glutDisplayFunc(draw)
    init()
    glutMainLoop()
