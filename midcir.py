from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def Round(a):
	return int(a+.5)

def init():
	glClearColor(1.0,1.0,1.0,0.0)
	glColor3f(1.0,0.0,0.0)
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
	global xc,yc,r
	xc=input("Enter xc centre of circle : ")
	yc=input("Enter yc centre of circle : ")
	r=input("Enter radius of circle : ")
	
def drawcir(xc,yc,r):
	pk=1.25-r
	setpixel(Round(xc),Round(yc))
	setpixel(Round(0),Round(r))
	x,y=0,r
	while(x<=y):
		if pk>=0:
			pk1=pk+5+2*(x-y)
			x=x+1
			y=y-1
			pk=pk1
		if pk<0:
			pk11=pk+3+2*x
			x=x+1
			y=y
			pk=pk11
		setpixel(Round(xc+x),Round(yc+y))
		setpixel(Round(xc-x),Round(yc+y))
		setpixel(Round(xc+x),Round(yc-y))
		setpixel(Round(xc-x),Round(yc-y))
		setpixel(Round(xc+y),Round(yc+x))
		setpixel(Round(xc-y),Round(yc+x))
		setpixel(Round(xc+y),Round(yc-x))
		setpixel(Round(xc-y),Round(yc-x))

def display():
	glClear(GL_COLOR_BUFFER_BIT)
	drawcir(xc,yc,r)
	
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(600,600)
	glutInitWindowPosition(200,200)
	glutCreateWindow(" Mid Point Circle ")
	getinput()
	glutDisplayFunc(display)
	init()
	glutMainLoop()
	
main()	
	
	
	
	
	
	
	
	
	
	

