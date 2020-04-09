from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from bresenhemcirimport import *
from dda_import import *

def init():
	glClearColor(1.0,1.0,1.0,0.0)
	glColor3f(0.0,0.0,1.0)
	glPointSize(3.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0.0,600.0,0.0,600.0)
	
def setpixel(x,y):
	glBegin(GL_POINTS)
	glVertex2i(x,y)
	glEnd()
	glFlush()
	
def readinput():
	global x1,y1,x2,y2,x3,y3,x4,y4,xc,yc,r
	x1=input(" enter x1 of rect : ")
	y1=input(" enter y1 of rect : ")
	x2=input(" enter x2 of rect : ")
	y2=input(" enter y2 of rect : ")
	x3=input(" enter x3 of rect : ")
	y3=input(" enter y3 of rect : ")
	x4=input(" enter x4 of rect : ")
	y4=input(" enter y4 of rect : ")
	xc=input(" enter xc of circle : ")
	yc=input(" enter yc of circle : ")
	r=input(" enter r of circle : ")
	
	
def display():
	glClear(GL_COLOR_BUFFER_BIT)
	lineDDA(x1,y1,x2,y2)
	lineDDA(x2,y2,x3,y3)
	lineDDA(x4,y4,x3,y3)
	lineDDA(x1,y1,x4,y4)
	drawcircle(r,xc,yc)
	
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(600,600)
	glutInitWindowPosition(50,50)
	glutCreateWindow("BOUNCING BALL ")
	readinput()
	glutDisplayFunc(display)
	init()
	glutMainLoop()
main()
	
