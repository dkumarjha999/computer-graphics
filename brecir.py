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
	global xc,yc,r
	xc=input("Enter xc centre of circle : ")
	yc=input("Enter yc centre of circle : ")
	r=input("Enter radius of circle : ")
	
def drawcir(xc,yc,r):
	pk=3-2*r
	setpixel(xc,yc)
	setpixel(0,r)
	x,y=0,r
	while(x<y):
		if pk>0:
			pk1=pk+10+4*(x-y)
			x=x+1
			y=y-1
			pk=pk1
		if pk<0:
			pk11=pk+6+4*x
			x=x+1
			y=y
			pk=pk11
		setpixel(xc+x,yc+y)
		setpixel(xc-x,yc+y)
		setpixel(xc+x,yc-y)
		setpixel(xc-x,yc-y)
		setpixel(xc+y,yc+x)
		setpixel(xc-y,yc+x)
		setpixel(xc+y,yc-x)
		setpixel(xc-y,yc-x)

	
	
def display():
	glClear(GL_COLOR_BUFFER_BIT)
	drawcir(xc,yc,r)


def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(600,600)
	glutInitWindowPosition(50,50)
	glutCreateWindow("BRESENHAMS CIRCLE ")
	getinput()
	glutDisplayFunc(display)
	init()
	glutMainLoop()
main()

