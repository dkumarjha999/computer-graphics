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
	
def setpixel(x,y):
	glBegin(GL_POINTS)
	glVertex2i(x,y)
	glEnd()
	glFlush()
	
def circledraw():
	section=.5  # we can vary section for more or less plotting points
	theta=2
	xs=1/float(section)
	#setpixel(Round(xc),Round(yc))
	for i in range(360):
	        x=50+theta
		y=50+(30*math.sin(theta))/theta
		theta+=xs;
		setpixel(Round(x),Round(y))


def display():
	glClear(GL_COLOR_BUFFER_BIT)
	circledraw()
	
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(600,600)
	glutInitWindowPosition(100,100)
	glutCreateWindow("sine Drawing Method ")
	#readinput()
	glutDisplayFunc(display)
	init()
	glutMainLoop()
main()
