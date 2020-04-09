from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
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
	global xc,yc,rx,ry
	xc=input("Enter xc centre of ellipse : ")
	yc=input("Enter yc centre of ellipse : ")
	rx=input("Enter radius rx of ellipse : ")
	ry=input("Enter radius ry of ellipse : ")
	
def drawcir(xc,yc,rx,ry):
	setpixel(Round(xc),Round(yc))
	theta=0
	section=1000
	steps=1/float(section)
	
	while(theta<=360):
		theta+=steps
		x=rx*math.cos(theta)
		y=ry*math.sin(theta)
		setpixel(Round(xc+x),Round(yc+y))
		

def display():
	glClear(GL_COLOR_BUFFER_BIT)
	drawcir(xc,yc,rx,ry)
	
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
	
	
	
	
	
	
	
	
	
	

