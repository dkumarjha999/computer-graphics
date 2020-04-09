from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


def Round(a):
	return int(a+.5)

def init():
	glClearColor(0.0,1.0,1.0,0.0)
	glColor3f(0.0,0.0,1.0)
	glPointSize(2.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0.0,600.0,0.0,600.0)
def setpixel(x,y):
	glBegin(GL_POINTS)
	glVertex2i(x,y)
	glEnd()
	glFlush()
	
def readinput():
	global x1,y1,x2,y2
	x1=input("Enter x1 : ")
	y1=input("Enter Y1 : ")
	x2=input("Enter x2 : ")
	y2=input("Enter Y2 : ")
	
def linedda(x1,y1,x2,y2):
	delta_x=x2-x1
	delta_y=y2-y1
	dx=abs(x2-x1)
	dy=abs(y2-y1)
	x,y=x1,y1
	steps=dx if dx>dy else  dy
	if steps!=0:
		change_x=dx/float(steps)
		change_y=dy/float(steps)
	else:
		change_x=0
		change_y=0
	
	setpixel(Round(x),Round(y))
	for k in range(steps):
		if delta_x>0:
			x+=change_x
		else:
			x-=change_x
		if delta_y>0:
			y+=change_y
		else:
			y-=change_y
		setpixel(Round(x),Round(y))
	
def display():
	glClear(GL_COLOR_BUFFER_BIT)
	linedda(x1,y1,x2,y2)

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(600,600)
	glutInitWindowPosition(100,100)
	glutCreateWindow("Simple DDA ")
	readinput()
	glutDisplayFunc(display)
	init()
	glutMainLoop()
main()
	
	

