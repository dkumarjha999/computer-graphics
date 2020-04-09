#Python code to import function in other pgm  to draw line using DDA algorithm  
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
def ROUND(a):
	return int(a+0.5)

def init():
	glClearColor(1.0,1.0,1.0,0.0)
	#glClolor3f(1.0,0.0,0.0)
	glPointSize(3.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0.0,600.0,0.0,600.0)

def setPixel(x,y):
	glBegin(GL_POINTS)
	glVertex2i(x,y)
	glEnd()
	glFlush()



def lineDDA(x0,y0,xEnd,yEnd):
	delta_x=xEnd-x0
	delta_y=yEnd-y0
	dx=abs(xEnd-x0)
	dy=abs(yEnd-y0)
	x,y=x0,y0
	steps=dx if dx>dy else dy
	if steps !=0:
		change_x=dx/float(steps)
		change_y=dy/float(steps)
	else:
		change_x=0
		change_y=0
	setPixel(ROUND(x),ROUND(y))
	
	for k in range(steps):
		if delta_x >= 0:  
			x+=change_x
		else:
			x-=change_x
		if delta_y >= 0:
			y+=change_y
		else:
			y-=change_y
		setPixel(ROUND(x),ROUND(y))
