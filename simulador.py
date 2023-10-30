import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np

# Puntos de control
P0 = np.array([2, 2])
P1 = np.array([9, 4])
T0 = np.array([-3, -4])
T1 = np.array([-10, -8])

# Crear la figura
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.2, bottom=0.35)

# Crear la curva de Hermite
t_values = np.linspace(0, 1, 500)

# Mostrar los puntos de control
plt.scatter([P0[0], P1[0]], [P0[1], P1[1],], c='red', marker='o', label='Puntos de control')

# Inicializar la línea de la curva (vacía)
line, = plt.plot([], [], label='Curva de Hermite', color='blue')

# Sliders para ajustar los vectores tangentes
axcolor = 'lightgoldenrodyellow'
ax_T0_x = plt.axes([0.2, 0.2, 0.65, 0.03], facecolor=axcolor)
ax_T0_y = plt.axes([0.2, 0.25, 0.65, 0.03], facecolor=axcolor)
ax_T1_x = plt.axes([0.2, 0.15, 0.65, 0.03], facecolor=axcolor)
ax_T1_y = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor=axcolor)

s_T0_x = Slider(ax_T0_x, 'T0_x', -10, 10, valinit=T0[0])
s_T0_y = Slider(ax_T0_y, 'T0_y', -10, 10, valinit=T0[1])
s_T1_x = Slider(ax_T1_x, 'T1_x', -10, 10, valinit=T1[0])
s_T1_y = Slider(ax_T1_y, 'T1_y', -10, 10, valinit=T1[1])

# Función para actualizar la curva
def update(val):
    T0[0] = s_T0_x.val
    T0[1] = s_T0_y.val
    T1[0] = s_T1_x.val
    T1[1] = s_T1_y.val
    curve_points = [(2*t**3 - 3*t**2 + 1) * (P0) + (t**3 - 2*t**2 + t) * T0 + (-2*t**3 + 3*t**2) * (P1) + (t**3 - t**2) * T1 for t in t_values]
    x_curve, y_curve = zip(*curve_points)
    line.set_xdata(x_curve)
    line.set_ydata(y_curve)
    plt.draw()

s_T0_x.on_changed(update)
s_T0_y.on_changed(update)
s_T1_x.on_changed(update)
s_T1_y.on_changed(update)

plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.grid()
plt.legend()
plt.show()

