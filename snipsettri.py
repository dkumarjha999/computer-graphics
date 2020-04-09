from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def getinput():
	global x1,y1,x2,y2,x3,y3,n
	x1=input("Enter x1 of triangle : ")
	y1=input("Enter y1 of triangle : ")
	x2=input("Enter x2 of triangle : ")
	y2=input("Enter y2 of triangle : ")
	x3=input("Enter x3 of triangle : ")
	y3=input("Enter y3 of triangle : ")
	#n=input("Enter degree of snipset of triangle : ")
	
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
	
def dispaly():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0,1.0,1.0)
	lineDDA(x1,y1,x2,y2,x3,y3)
	
def init():
	glClearColor(1.0,1.0,1.0,0.0)
	glPointSize(3.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0.0,600.0,0.0,600.0)
	
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(600,600)
	glutInitWindowPosition(50,50)
	glutCreateWindow("seirpenskytriangle")
	getinput()
	glutDisplayFunc(display)
	init()
	glutMainLoop()
	
main()
