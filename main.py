import glfw
from OpenGL.GL import *
from OpenGL.GLU import *


def hermite_curve(P1, P2, T1, T2, num_points):
    points = []

    for t in [i * 0.001 for i in range(num_points)]:
        h1 = 2 * t ** 3 - 3 * t ** 2 + 1
        h2 = t ** 3 - 2 * t ** 2 + t
        h3 = -2 * t ** 3 + 3 * t ** 2
        h4 = t ** 3 - t ** 2

        x = h1 * P1[0] + h2 * T1[0] + h3 * P2[0] + h4 * T2[0]
        y = h1 * P1[1] + h2 * T1[1] + h3 * P2[1] + h4 * T2[1]

        points.append((x, y))

    return points


def draw_curve(curve_points):
    glLineWidth(2.0)
    glBegin(GL_LINE_STRIP_ADJACENCY)
    glColor(1, 0, 0)  # Color rojo
    for point in curve_points:
        glVertex2f(point[0], point[1])

    glEnd()


def draw_control_points(P1, P2):
    glPointSize(7.0)
    glBegin(GL_POINTS)

    glColor(0, 1, 0)
    glVertex2f(P1[0], P1[1])
    glVertex2f(P2[0], P2[1])

    glEnd()


P1 = [2, 2]
P2 = [9, 4]
T1 = [-3, -4]
T2 = [-10, -8]

curve_points = hermite_curve(P1, P2, T1, T2, 1001)

glfw.init()
glfw.window_hint(glfw.SAMPLES, 4)  # 4x antialiasing
window = glfw.create_window(1000, 800, "Curva de Hermite en OpenGL", None, None)
glfw.make_context_current(window)

center_x = (P1[0] + P2[0]) / 2
center_y = (P1[1] + P2[1]) / 2

window_aspect_ratio = 1000 / 800

while not glfw.window_should_close(window):
    glfw.poll_events()

    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(center_x - 5 * window_aspect_ratio, center_x + 5 * window_aspect_ratio, center_y - 5, center_y + 5, -1, 1) 

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    draw_curve(curve_points)
    draw_control_points(P1, P2)

    glfw.swap_buffers(window)

glfw.terminate()