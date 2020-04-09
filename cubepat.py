from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
def draw():
    glClearColor(1.0,0.0,0.0,0.0)   # used for windows background colour
    glClear(GL_COLOR_BUFFER_BIT)
    glutWireCube(1.5)
    glFlush()
    
    
glutInit(sys.argv) 
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(700, 500)                  #size of window created
glutInitWindowPosition(100, 100)                              # position of window where to create
glutCreateWindow(" Cube  Design Program")    # taskbar title 
glutDisplayFunc(draw)  # calling function to draw the teaport
glutMainLoop()
