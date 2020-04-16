import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

# Решение задачи на упругое столкновение тел

# Временные интервалы
seconds_in_year = 365 * 24 * 60 * 60
seconds_in_day = 24 * 60 * 60
years = 2

# Определяем переменную величину
t = np.arange(0, years*seconds_in_year, 3*seconds_in_day)

# Определяем функцию для системы диф. уравнений
def move_func(s, t):
    (x1, v_x1, y1, v_y1,
     x2, v_x2, y2, v_y2,
     x3, v_x3, y3, v_y3) = s

    # Динамика первого тела под влиянием второго и третьего
    dxdt1 = v_x1
    dv_xdt1 = - G * m2 * (x1 - x2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5\
              - G * m3 * (x1 - x3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5

    dydt1 = v_y1
    dv_ydt1 = - G * m2 * (y1 - y2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5\
              - G * m3 * (y1 - y3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5

    # Динамика второго тела под влиянием первого и третьего
    dxdt2 = v_x2
    dv_xdt2 = - G * m1 * (x2 - x1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5\
              - G * m3 * (x2 - x3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5

    dydt2 = v_y2
    dv_ydt2 = - G * m1 * (y2 - y1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5\
              - G * m3 * (y2 - y3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5

    # Динамика третьего тела под влиянием первого и второго
    dxdt3 = v_x3
    dv_xdt3 = - G * m1 * (x3 - x1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5\
              - G * m2 * (x3 - x2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5

    dydt3 = v_y3
    dv_ydt3 = - G * m1 * (y3 - y1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5\
              - G * m2 * (y3 - y2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5

    return (dxdt1, dv_xdt1, dydt1, dv_ydt1,
            dxdt2, dv_xdt2, dydt2, dv_ydt2,
            dxdt3, dv_xdt3, dydt3, dv_ydt3)


# Определяем начальные значения и параметры
radius = 5*10**9

x10 = 0
v_x10 = - 1000
y10 = 0
v_y10 = 0

x20 = - 150*10**9
v_x20 = 0
y20 = 0
v_y20 = 0

x30=0
v_x30=0
y30=150*10**9
v_y30=-1000

s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30)

m1 = 1.1 * 10**(28)
m2 = 1.1 * 10**(28)
m3 = 1.1 * 10**(28)
G = 6.67 * 10**(-11)

# Проверка на условия столкновения
#move_array = np.ndarray(shape=(len(t), 6)) # Массив для записи координат
#
#for i in range(len(t)-1):
#
#    # Разбиваем все время t на маленькие промежутки tau
#    tau = [t[i], t[i+1]]
#
#    # Решаем задачу в маленьком промежутке времени tau
#    sol = odeint(move_func, s0, tau)
#
#    # Записываем координаты новых положений в массив
#    move_array[i, 0] = sol[1,0]
#    move_array[i, 1] = sol[1,2]
#    move_array[i, 2] = sol[1,4]
#    move_array[i, 3] = sol[1,6]
#    move_array[i, 4] = sol[1,8]
#    move_array[i, 5] = sol[1,10]
#
#    # Определенные положения и скорости становяться начальными условиями для
#    # следующего маленького промежутка времени tau
#    x10 = sol[1,0]
#    v_x10 = sol[1,1]
#    y10 = sol[1,2]
#    v_y10 = sol[1,3]
#
#    x20 = sol[1,4]
#    v_x20 = sol[1,5]
#    y20 = sol[1,6]
#    v_y20 = sol[1,7]
#
#    x30=sol[1,8]
#    v_x30=sol[1,9]
#    y30=sol[1,10]
#    v_y30=sol[1,11]
#
#    # Проверка на столкновение и пересчет условий
#    r12 = np.sqrt((x10 - x20)**2 + (y10 - y20)**2)
#    if r12 <= 2*radius:
#        V_x10 = (2 * m2 * v_x20 + v_x10 * (m1 - m2)) / (m1 + m2)
#        V_x20 = (2 * m1 * v_x10 + v_x20 * (m2 - m1)) / (m1 + m2)
#    else:
#        V_x10 = v_x10
#        V_x20 = v_x20
#
#    s0 = (x10, V_x10, y10, v_y10,
#          x20, V_x20, y20, v_y20)
#
#
#    r13 = np.sqrt((x10 - x30)**2 + (y10 - y30)**2)
#    if r13 <= 2*radius:
#        V_x10 = (2 * m3 * v_x30 + v_x10 * (m1 - m3)) / (m1 + m3)
#        V_x30 = (2 * m1 * v_x10 + v_x30 * (m3 - m1)) / (m1 + m3)
#    else:
#        V_x10 = v_x10
#        V_x30 = v_x30
#
#    s0 = (x10, V_x10, y10, v_y10,
#          x30, V_x30, y30, v_y30)
#
#    r32 = np.sqrt((x30 - x20)**2 + (y30 - y20)**2)
#    if r32 <= 2*radius:
#        V_x30 = (2 * m2 * v_x20 + v_x30 * (m3 - m2)) / (m3 + m2)
#        V_x20 = (2 * m3 * v_x30 + v_x20 * (m2 - m3)) / (m3 + m2)
#    else:
#        V_x30 = v_x30
#        V_x20 = v_x20
#
#    s0 = (x30, V_x30, y30, v_y30,
#          x20, V_x20, y20, v_y20,
#          x30, v_x30, y30, v_y30)

sol = odeint(move_func, s0, t)


# Строим решение в виде графика и анимируем
fig = plt.figure()

bodys = []

for i in range(0, len(t), 1):
    body1, = plt.plot(sol[:i, 0], sol[:i, 2], 'o', color='r', ms=20)
    # body1_line, = plt.plot(move_array[:i, 0], move_array[:i, 1], '-', color='r')

    body2, = plt.plot(sol[:i, 4], sol[:i, 6], 'o', color='g', ms=20)
    # body2_line, = plt.plot(move_array[:i, 2], move_array[:i, 3], '-', color='g')

    body3, = plt.plot(sol[:i, 8],sol[:i, 10], 'o', color='k', ms=20)
    # body2_line, = plt.plot(move_array[:i, 2], move_array[:i, 3], '-', color='g')

    bodys.append([body1, body2, body3])

ani = ArtistAnimation(fig, bodys, interval=50)

plt.axis('equal')
ani.save('Colissions.gif')
plt.show()