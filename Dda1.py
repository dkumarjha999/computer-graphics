from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def Round(a):
	return int(a+.5)

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
	
def getinput():
	global x1,y1,x2,y2
	x1=input("Enter x1 coordinate : ")
	y1=input("Enter y1 coordinate : ")
	x2=input("Enter x2 coordinate : ")
	y2=input("Enter y2 coordinate : ")
	
def linedda(x1,y1,x2,y2):
	delta_x=x2-x1
	delta_y=y2-y1
	dx=abs(delta_x)
	dy=abs(delta_y)
	x,y=x1,y1
	setpixel(Round(x),Round(y))
	steps=dx if dx>dy else dy
	if steps!=0:
		xinc=delta_x/float(steps)
		yinc=delta_y/float(steps)
	else:
		xinc=0
		yinc=0	
	
	for i in range(int(steps)):
		if delta_x>0:
			x+=xinc
		else:
			x-=xinc
		if delta_y>0:
			y+=yinc
		else:
			y-=yinc
		setpixel(Round(x),Round(y))
		
def display():
	glClear(GL_COLOR_BUFFER_BIT)
	linedda(x1,y1,x2,y2)


def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(600,600)
	glutInitWindowPosition(50,50)
	glutCreateWindow(" LINE DDA ")
	getinput()
	glutDisplayFunc(display)
	init()
	glutMainLoop()
main()
		
	
		
