from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

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
	global px,py
	n=int(input("Enter number of control points : "))
	px=[0 for x in range(n)]
	py=[0 for y in range(n)]
	for i in range(n):
		px[i]=input("Enter x of control point : ")
		py[i]=input("Enter y of control point : ")
		
def fact(n):
	if n==0:
		return 1
	else:
		return(n*fact(n-1))
		
		
def bezcoff(n,k):
	cof=fact(n)/(fact(n-k)*fact(k))
	return cof
	
	
def bez():
	n=len(px)
	u=0.0
	while u<=1.0:
		x=0.0
		y=0.0
		for k in range(n):
			x+=bezcoff(n,k)*pow(u,k)*pow(1-u,n-k)
			y+=bezcoff(n,k)*pow(u,k)*pow(1-u,n-k)
		setpixel(x,y)
		u+=0.00000001
	
	
def Bezcurve():
	while True:
		getinput()
		bez()
		print("Enter any decimal to continue")
		check=int(input("Enter 0 to exit: "))
		if check==0:
			sleep(5)
			sys.exit()
		else:
			pass	
	

def display():
	glClear(GL_COLOR_BUFFER_BIT)	
	Bezcurve()
	
	
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(600,600)
	glutInitWindowPosition(100,100)
	glutCreateWindow("Bezier Curve ")
	glutDisplayFunc(display)
	init()
	glutMainLoop()
	
main()
	
	
	
	
	
	
	
	
	
	
