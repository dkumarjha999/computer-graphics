
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
def draw():
    glClearColor(1.0,0.0,0.0,0.0)   # used for windows background colour
    glClear(GL_COLOR_BUFFER_BIT)
    #glutWireTeapot(0.5)
    glutWireSphere(0.75, 15, 15)  #first argument used for separation between the circles
    glFlush()
    
    
glutInit(sys.argv) 
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 500)                  #size of window created
glutInitWindowPosition(200, 150)                              # position of window where to create
glutCreateWindow(" many circle  Design Program")    # taskbar title 
glutDisplayFunc(draw)  # calling function to draw the teaport
glutMainLoop()
