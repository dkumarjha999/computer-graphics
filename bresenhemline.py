from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def init():
	glClearColor(1.0,1.0,1.0,0.0)
	glColor3f(0.0,0.0,1.0)
	glPointSize(3.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0.0,600.0,0.0,600.0)
	
	
def readinput():
	global x1,y1,x2,y2
	x1=input("Enter X1 Coordinate : ")
	y1=input("Enter y1 Coordinate : ")
	x2=input("Enter X2 Coordinate : ")
	y2=input("Enter y2 Coordinate : ")
	
def breline(x1,y1,x2,y2):
	delta_x=x2-x1
	delta_y=y2-y1
	dx=abs(delta_x)
	dy=abs(delta_y)
	x,y=x1,y1
	if dx>dy:
		pk=2*dy-dx
		setpixel(x,y)
		for i in range(dx):
			if pk>=0:
				pk1=pk+2*(dy-dx)
				x+=1
				y+=1
				pk=pk1
			if pk<0:
				pk2=pk+2*dx
				x+=1
				y=y
				pk=pk2
			setpixel(x,y)
	else:
		pk11=2*dy-dx
		setpixel(x,y)
		for i in range(dy):
			if pk11>=0:
				pk21=pk11+2*(dx-dy)
				x+=1
				y+=1
				pk11=pk21
			if pk11<0:
				pk21=pk11+2*dy
				x=x
				y+=1
				pk11=pk21
			setpixel(x,y)
			
	
def setpixel(x,y):
	glBegin(GL_POINTS)
	glVertex2f(x,y)
	glEnd()
	glFlush()
	
def display():
	glClear(GL_COLOR_BUFFER_BIT)
	breline(x1,y1,x2,y2)
	


def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(600,600)
	glutInitWindowPosition(100,100)
	glutCreateWindow("BresenHems Line ")
	readinput()
	glutDisplayFunc(display)
	init()
	glutMainLoop()
	
main()
			
	
