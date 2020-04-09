from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

def init():
	glClearColor(1.0,1.0,1.0,0.0)
	glColor3f(1.0,0.0,0.0)
	glPointSize(3.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0.0,600.0,0.0,600.0)

def readinput():
	global r,xc,yc
	r=input("Enter radius of  circle : ")
	xc=input("Enter x coordinate of center : ")
	yc=input("Enter y coordinate of center : ")
def drawcircle(r,xc,yc):
	pk=3-2*r
	setpixel(0,r)
	x,y=0,r
	while(x<y):
		if pk<0:
			pk1=pk+6+4*x
			x=x+1
			y=y
			pk=pk1
		if pk>0:
			pk2=pk+10+4*(x-y)
			x=x+1
			y=y-1
			pk=pk2
		setpixel(xc+x,yc+y)
		setpixel(xc+x,yc-y)
		setpixel(xc-x,yc+y)
		setpixel(xc-x,yc-y)
		setpixel(xc+y,yc+x)
		setpixel(xc+y,yc-x)
		setpixel(xc-y,yc+x)
		setpixel(xc-y,yc-x)
	
def display():
	glClear(GL_COLOR_BUFFER_BIT)
	drawcircle(r,xc,yc)
def setpixel(x,y):
	glBegin(GL_POINTS)
	glVertex2f(x,y)
	glEnd()
	glFlush()

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(600,600)
	glutInitWindowPosition(100,100)
	glutCreateWindow("BRESENHAMS CIRCLE ALgo ")
	readinput()
	glutDisplayFunc(display)
	init()
	glutMainLoop()
main()
	
	
	
