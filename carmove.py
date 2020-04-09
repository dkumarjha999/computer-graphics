from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from dda_import import *
from bresenhemcirimport import *
import sys

def myInit():
	glClearColor(0.0,0.0,0.0,1.0)
	glColor3f(1.0,0.0,0.0)
	glPointSize(1.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0.0,700.0,0.0,700.0)
	
def setPixel(xcoordinate,ycoordinate):
	glBegin(GL_POINTS)
	glPointSize(1.0)
	glColor3f(1.0,0.0,0.0)
	glVertex2f(xcoordinate,ycoordinate)
	glEnd()
	glFlush()

def car():
    glPointSize(2.0)
    glColor3f(0.0,1.0,0.0)
    drawcircle(50,150,100)
    glColor3f(0.0,1.0,0.0)
    drawcircle(50,350,100)
   
    
def body():
    lineDDA(50,100,100,100)
    lineDDA(50,100,50,190)
    lineDDA(50,190,175,390)
    lineDDA(175,390,350,380)
    lineDDA(350,380,450,175)
    lineDDA(450,175,550,150)
    lineDDA(550,150,560,100)
    lineDDA(560,100,400,100)
    lineDDA(100,100,300,100)
    
def road():
    glPointSize(1.0)
    i=0
    while i<70:
        lineDDA(0,70-i,600,70-i)
        i=i+1
	
def Display():
    glClear(GL_COLOR_BUFFER_BIT)
    road()
    car()
    body()
    
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(700,700)
	glutInitWindowPosition(50,50)
	glutCreateWindow("car road line")
	glutDisplayFunc(Display)
	myInit()
	glutMainLoop()
main()
