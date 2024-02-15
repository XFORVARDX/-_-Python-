import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
 
plt.style.use('dark_background')
 
fig = plt.figure()
ax = plt.axes(xlim=(-50, 50), ylim=(-50, 50))
line, = ax.plot([], [], lw=2)
 
 
# Функция инициализации.
def init():
    # создение пустого графа.
    line.set_data([], [])
    return line,
 
 
xdata, ydata = [], []
 
 
# функция анимации
def animate(i):
    t = 0.1 * i
 
    # x, y данные на графике
    x = t * np.sin(t)
    y = t * np.cos(t)
 
    # добавление новых точек в список точек осей x, y
    xdata.append(x)
    ydata.append(y)
    line.set_data(xdata, ydata)
    return line,
 
 
# Заголовок анимации
plt.title('Создаем спираль в matplotlib')
# Скрываем лишние данные
plt.axis('off')
 
# Вызов анимации.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=500, interval=20, blit=True)
 
# Сохраняем анимацию как gif файл
anim.save('coil.gif', writer='imagemagick')