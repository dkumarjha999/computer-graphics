from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

def Round(a):
	return int(a+.5)

def init():
	glClearColor(1.0,1.0,1.0,0.0)
	glColor3f(1.0,0.0,0.0)
	glPointSize(3.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0.0,600.0,0.0,600.0)
	
def readinput():
	global xc,yc,r,h
	xc=input("Enter Xcoordinate of center : ")
	yc=input("Enter Ycoordinate of center : ")
	r=input("Enter Radius of cylinder : ")
	h=input("Enter height of cylinder : ")
def setpixel(x,y):
	glBegin(GL_POINTS)
	glVertex2i(x,y)
	glEnd()
	glFlush()
	
def circledraw(xc,yc,r,h):
	for i in range(h):
		section=1000   # we can vary section for more or less plotting points
		theta=0
		xs=1/float(section)
		setpixel(Round(xc),Round(yc))
		while(theta<=360):
			x=xc+r*math.cos(theta)
			y=yc+r*math.sin(theta)
			theta+=xs;
			setpixel(Round(x),Round(y))
		yc+=1
		
def display():
	glClear(GL_COLOR_BUFFER_BIT)
	circledraw(xc,yc,r,h)
	
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(600,600)
	glutInitWindowPosition(100,100)
	glutCreateWindow("Parametric Circle Drawing Method ")
	readinput()
	glutDisplayFunc(display)
	init()
	glutMainLoop()
main()
