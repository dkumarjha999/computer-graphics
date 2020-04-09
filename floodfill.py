from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy 
import math
import sys

sys.setrecursionlimit(16000)

from bresenhemcirimport import *

def init():
    glClearColor(0.0,0.0,0.0,0.0)
    glMatrixMode
    (GL_PROJECTION)
    gluOrtho2D(0,600,0,600)


def fill_it(x,y,fillColor,prevColor):
    color=glReadPixels(x,y,1.0,1.0,GL_RGB,GL_FLOAT)
    if((color!=prevColor).any()):
        return
    glColor3f(fillColor[0],fillColor[1],fillColor[2])
    for i in range(xc-x,xc+x):
    	for  j in range(yc-y,yc+y):
    		    glBegin(GL_POINTS)
		    glVertex2f(i,j)
		    glEnd()
		    glFlush()
		    #fill_it(i,j,fillColor,prevColor)
		    


def setseed():
	prevColor= [0,0,0]
	fillColor= [1,0,1]
	fill_it(xc,yc,fillColor,prevColor)
              
def getinput():
	global xc,yc,r
	xc=input("Enter center xc of circle : ")
	yc=input("Enter center yc of circle : ")
	r=input("Enter radius of circle : ")

def world():
    drawcircle(r,xc,yc)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(600,600)
    glutInitWindowPosition(50,50)
    glutCreateWindow('flood fill recursive fill')
    getinput()
    glutDisplayFunc(world)
    print("Enter 1 to for boundary fill else fill will no take place : ")
    n=int(input("Ente your choice : "))
    if n==1:
    	setseed()
    else:
    	print("fill not happend because its not 1 ")
    init()
    glutMainLoop()
   
main()

