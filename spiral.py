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
	global xc,yc,r,n
	xc=input("Enter Xcoordinate of center : ")
	yc=input("Enter Ycoordinate of center : ")
	r=input("Enter Radius of circle : ")
	n=input("Enter number of turn in circle : ")
def setpixel(x,y):
	glBegin(GL_POINTS)
	glVertex2i(x,y)
	glEnd()
	glFlush()
	
def circledraw(xc,yc,r,n):
	section=1000   # we can vary section for more or less plotting points
	theta=0
	xs=1/float(section)
	setpixel(Round(xc),Round(yc))
	i=0
	while(i<=(int(n/2))):
		theta=0
		while(0<=theta<180):
			x=xc+r*math.cos(theta)
			y=yc+r*math.sin(theta)
			theta+=xs;
			setpixel(Round(x),Round(y))
		r=2*r
		while(180<=theta<=360):
			x=xc+r*math.cos(theta)
			y=yc+r*math.sin(theta)
			theta+=xs;
			setpixel(Round(x),Round(y))
		i+=1
		r=2*r



def display():
	glClear(GL_COLOR_BUFFER_BIT)
	circledraw(xc,yc,r,n)
	
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
