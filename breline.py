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
	
def setpixel(x,y):
	glBegin(GL_POINTS)
	glVertex2f(x,y)
	glEnd()
	glFlush()
	
def getinput():
	global x1,y1,x2,y2
	x1=input("Enter x1 coordinate : ")
	y1=input("Enter y1 coordinate : ")
	x2=input("Enter x2 coordinate : ")
	y2=input("Enter y2 coordinate : ")
	
def breline(x1,y1,x2,y2):
	delta_x=x2-x1
	delta_y=y2-y1
	dx=abs(delta_x)
	dy=abs(delta_y)
	m=dy/float(dx)
	steps=dx if dx>dy else dy
	x,y=x1,y1
	setpixel(x,y)
	for i in range(int(steps)):
		if m<=1:
			pk=2*delta_y-delta_x
			if pk>=0:
				pk1=pk+2*(delta_y-delta_x)
				if delta_x>0:
					x+=1
				else:
					x-=1
				if delta_y>0:
					y+=1
				else:
					y-=1
			if pk<0:
				pk11=pk+2*delta_y
				if delta_x>0:
					x+=1
				else:
					x-=1
				if delta_y>0:
					y=y
				else:
					y=y

		if m<=1:
			pk=2*delta_y-delta_x
			if pk>=0:
				pk1=pk+2*(delta_y-delta_x)
				if delta_x>0:
					x+=1
				else:
					x-=1
				if delta_y>0:
					y+=1
				else:
					y-=1
			if pk<0:
				pk11=pk+2*delta_y
				if delta_x>0:
					x+=1
				else:
					x-=1
				if delta_y>0:
					y=y
				else:
					y=y
		if m>1:
			pk=2*delta_x-delta_y
			if pk>=0:
				pk2=pk+2*(delta_x-delta_y)
				if delta_x>0:
					x+=1
				else:
					x-=1
				if delta_y>0:
					y+=1
				else:
					y-=1
			if pk<0:
				pk11=pk+2*delta_x
				if delta_x>0:
					x=x
				else:
					x=x
				if delta_y>0:
					y+=1
				else:
					y-=1
		setpixel(x,y)
		

	
	
def display():
	glClear(GL_COLOR_BUFFER_BIT)
	breline(x1,y1,x2,y2)


def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(600,600)
	glutInitWindowPosition(50,50)
	glutCreateWindow("BRESENHAMS LINE ")
	getinput()
	glutDisplayFunc(display)
	init()
	glutMainLoop()
main()

