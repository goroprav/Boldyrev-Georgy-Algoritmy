import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

# Решение задачи на упругое столкновение тел

# Временные интервалы
seconds_in_year = 365 * 24 * 60 * 60
seconds_in_day = 24 * 60 * 60
years = 3

# Определяем переменную величину
t = np.arange(0, years*seconds_in_year, 2*seconds_in_day)

# Определяем функцию для системы диф. уравнений
def move_func(s, t):
    
    (x1, v_x1, y1, v_y1,
     x2, v_x2, y2, v_y2,
     x3, v_x3, y3, v_y3,
     x4, v_x4, y4, v_y4,
     x5, v_x5, y5, v_y5,
     x6, v_x6, y6, v_y6,
     x7, v_x7, y7, v_y7,
     x8, v_x8, y8, v_y8,
     x9, v_x9, y9, v_y9,
     x10, v_x10, y10, v_y10)=s
     
     
     
    dxdt1 = v_x1
    dv_xdt1 = - G * m2 * (x1 - x2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
    
    dydt1 = v_y1
    dv_ydt1 = - G * m2 * (y1 - y2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
    
    
    dxdt1 = v_x1
    dv_xdt1 = - G * m3 * (x1 - x3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5
    
    dydt1 = v_y1
    dv_ydt1 = - G * m3 * (y1 - y3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5
    
    
    dxdt1 = v_x1
    dv_xdt1 = - G * m4 * (x1 - x4) / ((x1 - x4)**2 + (y1 - y4)**2)**1.5
    
    dydt1 = v_y1
    dv_ydt1 = - G * m4 * (y1 - y4) / ((x1 - x4)**2 + (y1 - y4)**2)**1.5
    
    
    dxdt1 = v_x1
    dv_xdt1 = - G * m5 * (x1 - x5) / ((x1 - x5)**2 + (y1 - y5)**2)**1.5
    
    dydt1 = v_y1
    dv_ydt1 = - G * m5 * (y1 - y5) / ((x1 - x5)**2 + (y1 - y5)**2)**1.5
    
    
    dxdt1 = v_x1
    dv_xdt1 = - G * m6 * (x1 - x6) / ((x1 - x6)**2 + (y1 - y6)**2)**1.5
    
    dydt1 = v_y1
    dv_ydt1 = - G * m6 * (y1 - y6) / ((x1 - x6)**2 + (y1 - y6)**2)**1.5
    
    
    dxdt1 = v_x1
    dv_xdt1 = - G * m7 * (x1 - x7) / ((x1 - x7)**2 + (y1 - y7)**2)**1.5
    
    dydt1 = v_y1
    dv_ydt1 = - G * m7 * (y1 - y7) / ((x1 - x7)**2 + (y1 - y7)**2)**1.5
    
    
    dxdt1 = v_x1
    dv_xdt1 = - G * m8 * (x1 - x8) / ((x1 - x8)**2 + (y1 - y8)**2)**1.5
    
    dydt1 = v_y1
    dv_ydt1 = - G * m8 * (y1 - y8) / ((x1 - x8)**2 + (y1 - y8)**2)**1.5
    
    
    dxdt1 = v_x1
    dv_xdt1 = - G * m9 * (x1 - x9) / ((x1 - x9)**2 + (y1 - y9)**2)**1.5
    
    dydt1 = v_y1
    dv_ydt1 = - G * m9 * (y1 - y9) / ((x1 - x9)**2 + (y1 - y9)**2)**1.5
    
    
    dxdt1 = v_x1
    dv_xdt1 = - G * m10 * (x1 - x10) / ((x1 - x10)**2 + (y1 - y10)**2)**1.5
    
    dydt1 = v_y1
    dv_ydt1 = - G * m10 * (y1 - y10) / ((x1 - x10)**2 + (y1 - y10)**2)**1.5
    
    
    
    
    

    # Динамика второго тела под влиянием первого, третьего и четвертого
    #ddddddddddd#
    #333333333333
    dxdt2 = v_x2
    dv_xdt2 = - G * m1 * (x2 - x1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
    
    dydt2 = v_y2
    dv_ydt2 = - G * m1 * (y2 - y1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
    
    dxdt2 = v_x2
    dv_xdt2 = - G * m3 * (x2 - x3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5
    
    dydt2 = v_y2
    dv_ydt2 = - G * m3 * (y2 - y3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5
    
    
    dxdt2 = v_x2
    dv_xdt2 = - G * m4 * (x2 - x4) / ((x2 - x4)**2 + (y2 - y4)**2)**1.5
    
    dydt2 = v_y2
    dv_ydt2 = - G * m4 * (y2 - y4) / ((x2 - x4)**2 + (y2 - y4)**2)**1.5
    
    
    dxdt2 = v_x2
    dv_xdt2 = - G * m5 * (x2 - x5) / ((x2 - x5)**2 + (y2 - y5)**2)**1.5
    
    dydt2 = v_y2
    dv_ydt2 = - G * m5 * (y2 - y5) / ((x2 - x5)**2 + (y2 - y5)**2)**1.5
    
    
    dxdt2 = v_x2
    dv_xdt2 = - G * m6 * (x2 - x6) / ((x2 - x6)**2 + (y2 - y6)**2)**1.5
    
    dydt2 = v_y2
    dv_ydt2 = - G * m6 * (y2 - y6) / ((x2 - x6)**2 + (y2 - y6)**2)**1.5
    
    
    dxdt2 = v_x2
    dv_xdt2 = - G * m7 * (x2 - x7) / ((x2 - x7)**2 + (y2 - y7)**2)**1.5
    
    dydt2 = v_y2
    dv_ydt2 = - G * m7 * (y2 - y7) / ((x2 - x7)**2 + (y2 - y7)**2)**1.5
    
    
    dxdt2 = v_x2
    dv_xdt2 = - G * m8 * (x2 - x8) / ((x2 - x8)**2 + (y2 - y8)**2)**1.5
    
    dydt2 = v_y2
    
    dv_ydt2 = - G * m8 * (y2 - y8) / ((x2 - x8)**2 + (y2 - y8)**2)**1.5
    
    
    dxdt2 = v_x2
    dv_xdt2 = - G * m9 * (x2 - x9) / ((x2 - x9)**2 + (y2 - y9)**2)**1.5
    
    dydt2 = v_y2
    dv_ydt2 = - G * m9 * (y2 - y9) / ((x2 - x9)**2 + (y2 - y9)**2)**1.5
    
    
    dxdt2 = v_x2
    dv_xdt2 = - G * m10 * (x2 - x10) / ((x2 - x10)**2 + (y2 - y10)**2)**1.5
    
    dydt2 = v_y2
    dv_ydt2 = - G * m10 * (y2 - y10) / ((x2 - x10)**2 + (y2 - y10)**2)**1.5
    
    
    #fffffffffffff
    
    
    
    #ddddddddddd
    #ddddddddddd
    dxdt3 = v_x3
    dv_xdt3 = - G * m1 * (x3 - x1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5
    
    dydt3 = v_y3
    dv_ydt3 = - G * m1 * (y3 - y1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5
    
    
    
    dxdt3 = v_x3
    dv_xdt3 = - G * m2 * (x3 - x2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5
    
    dydt3 = v_y3
    dv_ydt3 = - G * m2 * (y3 - y2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5
    
    
    dxdt3 = v_x3
    dv_xdt3 = - G * m4 * (x3 - x4) / ((x3 - x4)**2 + (y3 - y4)**2)**1.5
    
    dydt3 = v_y3
    dv_ydt3 = - G * m4 * (y3 - y4) / ((x3 - x4)**2 + (y3 - y4)**2)**1.5
    
    
    dxdt3= v_x3
    dv_xdt3 = - G * m5 * (x3 - x5) / ((x3 - x5)**2 + (y3 - y5)**2)**1.5
    
    dydt3 = v_y3
    dv_ydt3 = - G * m5 * (y3 - y5) / ((x3 - x5)**2 + (y3 - y5)**2)**1.5
    
    
    dxdt3 = v_x3
    dv_xdt3 = - G * m6 * (x3 - x6) / ((x3 - x6)**2 + (y3 - y6)**2)**1.5
    
    dydt3 = v_y3
    dv_ydt3 = - G * m6 * (y3 - y6) / ((x3 - x6)**2 + (y3 - y6)**2)**1.5
    
    
    dxdt3 = v_x3
    dv_xdt3 = - G * m7 * (x3 - x7) / ((x3 - x7)**2 + (y3 - y7)**2)**1.5
    
    dydt3 = v_y3
    dv_ydt3 = - G * m7 * (y3 - y7) / ((x3 - x7)**2 + (y3 - y7)**2)**1.5
    
    
    dxdt3 = v_x3
    dv_xdt3 = - G * m8 * (x3 - x8) / ((x3 - x8)**2 + (y3 - y8)**2)**1.5
    
    dydt3 = v_y3
    dv_ydt3 = - G * m8 * (y3 - y8) / ((x3 - x8)**2 + (y3 - y8)**2)**1.5
    
    
    dxdt3 = v_x3
    dv_xdt3 = - G * m9 * (x3 - x9) / ((x3 - x9)**2 + (y3 - y9)**2)**1.5
    
    dydt3 = v_y3
    dv_ydt3 = - G * m9 * (y3 - y9) / ((x3 - x9)**2 + (y3 - y9)**2)**1.5
    
    
    dxdt3 = v_x3
    dv_xdt3 = - G * m10 * (x3 - x10) / ((x3 - x10)**2 + (y3 - y10)**2)**1.5
    
    dydt3 = v_y3
    dv_ydt3 = - G * m10 * (y3 - y10) / ((x3 - x10)**2 + (y3 - y10)**2)**1.5
    
    #kkkkkk
    
    
    
    #ggggg
    #gggggg
    
    dxdt5 = v_x5
    dv_xdt5 = - G * m1 * (x5 - x1) / ((x5 - x1)**2 + (y5 - y1)**2)**1.5
    
    dydt5 = v_y5
    dv_ydt5 = - G * m1 * (y5 - y1) / ((x5 - x1)**2 + (y5 - y1)**2)**1.5
    
    
    
    dxdt5 = v_x5
    dv_xdt5 = - G * m2 * (x5 - x2) / ((x5 - x2)**2 + (y5 - y2)**2)**1.5
    
    dydt5 = v_y5
    dv_ydt5 = - G * m2 * (y5 - y2) / ((x5 - x2)**2 + (y5 - y2)**2)**1.5
    
    
    dxdt5 = v_x5
    dv_xdt5 = - G * m3 * (x5 - x3) / ((x5 - x3)**2 + (y5 - y3)**2)**1.5
    
    dydt5 = v_y5
    dv_ydt5 = - G * m3 * (y5 - y3) / ((x5 - x3)**2 + (y5 - y3)**2)**1.5
    
    
    dxdt5= v_x5
    dv_xdt5 = - G * m4 * (x5 - x4) / ((x5 - x4)**2 + (y5 - y4)**2)**1.5
    
    dydt5 = v_y5
    dv_ydt5 = - G * m4 * (y5 - y4) / ((x5 - x4)**2 + (y5 - y4)**2)**1.5
    
    
    dxdt5 = v_x5
    dv_xdt5 = - G * m6 * (x5 - x6) / ((x5 - x6)**2 + (y5 - y6)**2)**1.5
    
    dydt5 = v_y5
    dv_ydt5 = - G * m6 * (y5 - y6) / ((x5 - x6)**2 + (y5 - y6)**2)**1.5
    
    
    dxdt5 = v_x5
    dv_xdt5 = - G * m7 * (x5 - x7) / ((x5 - x7)**2 + (y5 - y7)**2)**1.5
    
    dydt5 = v_y5
    dv_ydt5 = - G * m7 * (y5 - y7) / ((x5 - x7)**2 + (y5 - y7)**2)**1.5
    
    
    dxdt5 = v_x5
    dv_xdt5 = - G * m8 * (x5 - x8) / ((x5 - x8)**2 + (y5 - y8)**2)**1.5
    
    dydt5 = v_y5
    dv_ydt5 = - G * m8 * (y5 - y8) / ((x5 - x8)**2 + (y5 - y8)**2)**1.5
    
    
    dxdt5 = v_x5
    dv_xdt5 = - G * m9 * (x5 - x9) / ((x5 - x9)**2 + (y5 - y9)**2)**1.5
    
    dydt5 = v_y5
    dv_ydt5 = - G * m9 * (y5 - y9) / ((x5 - x9)**2 + (y5 - y9)**2)**1.5
    
    
    dxdt5 = v_x5
    dv_xdt5 = - G * m10 * (x5 - x10) / ((x5 - x10)**2 + (y5 - y10)**2)**1.5
    
    dydt5 = v_y5
    dv_ydt5 = - G * m10 * (y5 - y10) / ((x5 - x10)**2 + (y5 - y10)**2)**1.5
    
    #ggggg
    
    
    
    #ffffff
    #ddddd
    
    dxdt4 = v_x4
    dv_xdt4 = - G * m1 * (x4 - x1) / ((x4 - x1)**2 + (y4 - y1)**2)**1.5
    
    dydt4 = v_y4
    dv_ydt4 = - G * m1 * (y4 - y1) / ((x4 - x1)**2 + (y4 - y1)**2)**1.5
    
    
    
    dxdt4 = v_x4
    dv_xdt4 = - G * m2 * (x4 - x2) / ((x4 - x2)**2 + (y4 - y2)**2)**1.5
    
    dydt4 = v_y4
    dv_ydt4 = - G * m2 * (y4 - y2) / ((x4 - x2)**2 + (y4 - y2)**2)**1.5
    
    
    dxdt4 = v_x4
    dv_xdt4 = - G * m3 * (x4 - x3) / ((x4 - x3)**2 + (y4 - y3)**2)**1.5
    
    dydt4 = v_y4
    dv_ydt4 = - G * m3 * (y4 - y3) / ((x4 - x3)**2 + (y4 - y3)**2)**1.5
    
    
    dxdt4= v_x4
    dv_xdt4 = - G * m5 * (x4 - x5) / ((x4 - x5)**2 + (y4 - y5)**2)**1.5
    
    dydt4 = v_y4
    dv_ydt4 = - G * m5 * (y4 - y5) / ((x4 - x5)**2 + (y4 - y5)**2)**1.5
    
    
    dxdt4 = v_x4
    dv_xdt4 = - G * m6 * (x4 - x6) / ((x4 - x6)**2 + (y4 - y6)**2)**1.5
    
    dydt4 = v_y4
    dv_ydt4 = - G * m6 * (y4 - y6) / ((x4 - x6)**2 + (y4 - y6)**2)**1.5
    
    
    dxdt4 = v_x4
    dv_xdt4 = - G * m7 * (x4 - x7) / ((x4 - x7)**2 + (y4 - y7)**2)**1.5
    
    dydt4 = v_y4
    dv_ydt4 = - G * m7 * (y4 - y7) / ((x4 - x7)**2 + (y4 - y7)**2)**1.5
    
    
    dxdt4 = v_x4
    dv_xdt4 = - G * m8 * (x4 - x8) / ((x4 - x8)**2 + (y4 - y8)**2)**1.5
    
    dydt4 = v_y4
    dv_ydt4 = - G * m8 * (y4 - y8) / ((x4 - x8)**2 + (y4 - y8)**2)**1.5
    
    
    dxdt4 = v_x4
    dv_xdt4 = - G * m9 * (x4 - x9) / ((x4 - x9)**2 + (y4 - y9)**2)**1.5
    
    dydt4 = v_y4
    dv_ydt4 = - G * m9 * (y4 - y9) / ((x4 - x9)**2 + (y4 - y9)**2)**1.5
    
    
    dxdt3 = v_x3
    dv_xdt3 = - G * m10 * (x4 - x10) / ((x4 - x10)**2 + (y4 - y10)**2)**1.5
    
    dydt3 = v_y3
    dv_ydt3 = - G * m10 * (y4 - y10) / ((x4 - x10)**2 + (y4 - y10)**2)**1.5
    
    
    #hhhhhhhhhhhhhhh
    #h
    #hhhhhhhhhhhhhhhhhhhh#
    
    
    
    
    
    dxdt6 = v_x6
    dv_xdt6 = - G * m1 * (x6 - x1) / ((x6 - x1)**2 + (y6 - y1)**2)**1.5
    
    dydt6 = v_y6
    dv_ydt6 = - G * m1 * (y6 - y1) / ((x6 - x1)**2 + (y6 - y1)**2)**1.5
    
    
    
    dxdt6 = v_x6
    dv_xdt6 = - G * m2 * (x6 - x2) / ((x6 - x2)**2 + (y6 - y2)**2)**1.5
    
    dydt6 = v_y6
    dv_ydt6 = - G * m2 * (y6 - y2) / ((x6 - x2)**2 + (y6 - y2)**2)**1.5
    
    
    dxdt6 = v_x6
    dv_xdt6 = - G * m3 * (x6 - x3) / ((x6 - x3)**2 + (y6 - y3)**2)**1.5
    
    dydt6 = v_y6
    dv_ydt6 = - G * m3 * (y6 - y3) / ((x6 - x3)**2 + (y6 - y3)**2)**1.5
    
    
    dxdt6= v_x6
    dv_xdt6 = - G * m4 * (x6 - x4) / ((x6 - x4)**2 + (y6 - y4)**2)**1.5
    
    dydt6 = v_y6
    dv_ydt6 = - G * m4 * (y6 - y4) / ((x6 - x4)**2 + (y6 - y4)**2)**1.5
    
    
    dxdt6 = v_x6
    dv_xdt6 = - G * m5 * (x6 - x5) / ((x6 - x5)**2 + (y6 - y5)**2)**1.5
    
    dydt6 = v_y6
    dv_ydt6 = - G * m5 * (y6 - y5) / ((x6 - x5)**2 + (y6 - y5)**2)**1.5
    
    
    dxdt6 = v_x6
    dv_xdt6 = - G * m7 * (x6 - x7) / ((x6 - x7)**2 + (y6 - y7)**2)**1.5
    
    dydt6 = v_y6
    dv_ydt6 = - G * m7 * (y6 - y7) / ((x6 - x7)**2 + (y6 - y7)**2)**1.5
    
    
    dxdt6 = v_x6
    dv_xdt6 = - G * m8 * (x6 - x8) / ((x6 - x8)**2 + (y6 - y8)**2)**1.5
    
    dydt6 = v_y6
    dv_ydt6 = - G * m8 * (y6 - y8) / ((x6 - x8)**2 + (y6 - y8)**2)**1.5
    
    
    dxdt6 = v_x6
    dv_xdt6 = - G * m9 * (x6 - x9) / ((x6 - x9)**2 + (y6 - y9)**2)**1.5
    
    dydt6 = v_y6
    dv_ydt6 = - G * m9 * (y6 - y9) / ((x6 - x9)**2 + (y6 - y9)**2)**1.5
    
    
    dxdt6 = v_x6
    dv_xdt6 = - G * m10 * (x6 - x10) / ((x6 - x10)**2 + (y6 - y10)**2)**1.5
    
    dydt6 = v_y6
    dv_ydt6 = - G * m10 * (y6 - y10) / ((x6 - x10)**2 + (y6 - y10)**2)**1.5
    
    
    ###
    #ddddddddddddd
    #ddddddddddd
    #dddddddddd
    
    
    dxdt7 = v_x7
    dv_xdt7 = - G * m1 * (x7 - x1) / ((x7 - x1)**2 + (y7 - y1)**2)**1.5
    
    dydt7 = v_y7
    dv_ydt7 = - G * m1 * (y7 - y1) / ((x7 - x1)**2 + (y7 - y1)**2)**1.5
    
    
    
    dxdt7 = v_x7
    dv_xdt7 = - G * m2 * (x7 - x2) / ((x7 - x2)**2 + (y7 - y2)**2)**1.5
    
    dydt7 = v_y7
    dv_ydt7 = - G * m2 * (y7 - y2) / ((x7 - x2)**2 + (y7 - y2)**2)**1.5
    
    
    dxdt7 = v_x7
    dv_xdt7 = - G * m3 * (x7 - x3) / ((x7 - x3)**2 + (y7 - y3)**2)**1.5
    
    dydt7 = v_y7
    dv_ydt7 = - G * m3 * (y7 - y3) / ((x7 - x3)**2 + (y7 - y3)**2)**1.5
    
    
    dxdt7= v_x7
    dv_xdt7 = - G * m4 * (x7 - x4) / ((x7 - x4)**2 + (y7 - y4)**2)**1.5
    
    dydt7 = v_y7
    dv_ydt7 = - G * m4 * (y7 - y4) / ((x7 - x4)**2 + (y7 - y4)**2)**1.5
    
    
    dxdt7 = v_x7
    dv_xdt7 = - G * m5 * (x7 - x5) / ((x7 - x5)**2 + (y7 - y5)**2)**1.5
    
    dydt7 = v_y7
    dv_ydt7 = - G * m5 * (y7 - y5) / ((x7 - x5)**2 + (y7 - y5)**2)**1.5
    
    
    dxdt7 = v_x7
    dv_xdt7 = - G * m6 * (x7 - x6) / ((x7 - x6)**2 + (y7 - y6)**2)**1.5
    
    dydt7 = v_y7
    dv_ydt7 = - G * m6 * (y7 - y6) / ((x7 - x6)**2 + (y7 - y6)**2)**1.5
    
    
    dxdt7 = v_x7
    dv_xdt7 = - G * m8 * (x7 - x8) / ((x7 - x8)**2 + (y7 - y8)**2)**1.5
    
    dydt7 = v_y7
    dv_ydt7 = - G * m8 * (y7 - y8) / ((x7 - x8)**2 + (y7 - y8)**2)**1.5
    
    
    dxdt7 = v_x7
    dv_xdt7 = - G * m9 * (x7 - x9) / ((x7 - x9)**2 + (y6 - y9)**2)**1.5
    
    dydt7 = v_y7
    dv_ydt7 = - G * m9 * (y7 - y9) / ((x7 - x9)**2 + (y7 - y9)**2)**1.5
    
    
    dxdt7 = v_x7
    dv_xdt7 = - G * m10 * (x7 - x10) / ((x7 - x10)**2 + (y7 - y10)**2)**1.5
    
    dydt7 = v_y7
    dv_ydt7 = - G * m10 * (y7 - y10) / ((x7 - x10)**2 + (y7 - y10)**2)**1.5
    
    #ggggggggggggg
    #ggggggggggggg
    #fffffffffffff
    
    
    dxdt8 = v_x8
    dv_xdt8 = - G * m1 * (x8 - x1) / ((x8 - x1)**2 + (y8 - y1)**2)**1.5
    
    dydt8 = v_y8
    dv_ydt8 = - G * m1 * (y8 - y1) / ((x8 - x1)**2 + (y8 - y1)**2)**1.5
    
    
    
    dxdt8 = v_x8
    dv_xdt8 = - G * m2 * (x8 - x2) / ((x8 - x2)**2 + (y8 - y2)**2)**1.5
    
    dydt8 = v_y8
    dv_ydt8 = - G * m2 * (y8 - y2) / ((x8 - x2)**2 + (y8 - y2)**2)**1.5
    
    
    dxdt8 = v_x8
    dv_xdt8 = - G * m3 * (x8 - x3) / ((x8 - x3)**2 + (y8 - y3)**2)**1.5
    
    dydt8 = v_y8
    dv_ydt8 = - G * m3 * (y8 - y3) / ((x8 - x3)**2 + (y8 - y3)**2)**1.5
    
    
    dxdt8 = v_x8
    dv_xdt8 = - G * m4 * (x8 - x4) / ((x8 - x4)**2 + (y8 - y4)**2)**1.5
    
    dydt8 = v_y8
    dv_ydt8 = - G * m4 * (y8 - y4) / ((x8 - x4)**2 + (y8 - y4)**2)**1.5
    
    
    dxdt8 = v_x8
    dv_xdt8 = - G * m5 * (x8 - x5) / ((x8 - x5)**2 + (y8 - y5)**2)**1.5
    
    dydt8 = v_y8
    dv_ydt8 = - G * m5 * (y8 - y5) / ((x8 - x5)**2 + (y8 - y5)**2)**1.5
    
    
    dxdt8 = v_x8
    dv_xdt8 = - G * m6 * (x8 - x6) / ((x8 - x6)**2 + (y8 - y6)**2)**1.5
    
    dydt8 = v_y8
    dv_ydt8 = - G * m6 * (y8 - y6) / ((x8 - x6)**2 + (y8 - y6)**2)**1.5
    
    
    dxdt8 = v_x8
    dv_xdt8 = - G * m7 * (x8 - x7) / ((x8 - x7)**2 + (y8 - y7)**2)**1.5
    
    dydt8 = v_y8
    dv_ydt8 = - G * m7 * (y8 - y7) / ((x8 - x7)**2 + (y8 - y7)**2)**1.5
    
    
    dxdt8 = v_x8
    dv_xdt8 = - G * m9 * (x8 - x9) / ((x8 - x9)**2 + (y8 - y9)**2)**1.5
    
    dydt8 = v_y8
    dv_ydt8 = - G * m9 * (y8 - y9) / ((x8 - x9)**2 + (y8 - y9)**2)**1.5
    
    
    dxdt8 = v_x8
    dv_xdt8 = - G * m10 * (x8 - x10) / ((x8 - x10)**2 + (y8 - y10)**2)**1.5
    
    dydt8 = v_y8
    dv_ydt8 = - G * m10 * (y8 - y10) / ((x8 - x10)**2 + (y8 - y10)**2)**1.5
    ##dddd
    #dddddddd
    #ddddddddd
    
    
    dxdt9 = v_x9
    dv_xdt9 = - G * m1 * (x9 - x1) / ((x9 - x1)**2 + (y9 - y1)**2)**1.5
    
    dydt9 = v_y9
    dv_ydt9 = - G * m1 * (y9 - y1) / ((x9 - x1)**2 + (y9 - y1)**2)**1.5
    
    
    
    dxdt9 = v_x9
    dv_xdt9 = - G * m2 * (x9 - x2) / ((x9 - x2)**2 + (y9 - y2)**2)**1.5
    
    dydt9 = v_y9
    dv_ydt9 = - G * m2 * (y9 - y2) / ((x9 - x2)**2 + (y9 - y2)**2)**1.5
    
    
    dxdt9 = v_x9
    dv_xdt9 = - G * m3 * (x9 - x3) / ((x9 - x3)**2 + (y9 - y3)**2)**1.5
    
    dydt9 = v_y9
    dv_ydt9 = - G * m3 * (y9 - y3) / ((x9 - x3)**2 + (y9 - y3)**2)**1.5
    
    
    dxdt9 = v_x9
    dv_xdt9 = - G * m4 * (x9 - x4) / ((x9 - x4)**2 + (y9 - y4)**2)**1.5
    
    dydt9 = v_y9
    dv_ydt9 = - G * m4 * (y9 - y4) / ((x9 - x4)**2 + (y9 - y4)**2)**1.5
    
    
    dxdt9 = v_x9
    dv_xdt9 = - G * m5 * (x9 - x5) / ((x9 - x5)**2 + (y9 - y5)**2)**1.5
    
    dydt9 = v_y9
    dv_ydt9 = - G * m5 * (y9 - y5) / ((x9 - x5)**2 + (y9 - y5)**2)**1.5
    
    
    dxdt9 = v_x9
    dv_xdt9 = - G * m6 * (x9 - x6) / ((x9 - x6)**2 + (y9 - y6)**2)**1.5
    
    dydt9 = v_y9
    dv_ydt9 = - G * m6 * (y9 - y6) / ((x9 - x6)**2 + (y9 - y6)**2)**1.5
    
    
    dxdt9 = v_x9
    dv_xdt9 = - G * m7 * (x9 - x7) / ((x9 - x7)**2 + (y9 - y7)**2)**1.5
    
    dydt9 = v_y9
    dv_ydt9 = - G * m7 * (y9 - y7) / ((x9 - x7)**2 + (y9 - y7)**2)**1.5
    
    
    dxdt9 = v_x9
    dv_xdt9 = - G * m8 * (x9 - x8) / ((x9 - x8)**2 + (y9 - y8)**2)**1.5
    
    dydt9 = v_y9
    dv_ydt9 = - G * m8 * (y9 - y8) / ((x9 - x8)**2 + (y9 - y8)**2)**1.5
    
    
    dxdt9 = v_x9
    dv_xdt9 = - G * m10 * (x9 - x10) / ((x9 - x10)**2 + (y9 - y10)**2)**1.5
    
    dydt9 = v_y9
    dv_ydt9 = - G * m10 * (y9 - y10) / ((x9 - x10)**2 + (y9 - y10)**2)**1.5
    #dddddddddddddd
    #dddddddddddddd
    #dddddddddd
    
    
    
    dxdt10 = v_x10
    dv_xdt10 = - G * m1 * (x10 - x1) / ((x10 - x1)**2 + (y10 - y1)**2)**1.5
    
    dydt10 = v_y10
    dv_ydt10 = - G * m1 * (y10 - y1) / ((x10 - x1)**2 + (y10 - y1)**2)**1.5
    
    
    
    dxdt10= v_x10
    dv_xdt10 = - G * m2 * (x10 - x2) / ((x10 - x2)**2 + (y10 - y2)**2)**1.5
    
    dydt10 = v_y10
    dv_ydt10 = - G * m2 * (y10 - y2) / ((x10 - x2)**2 + (y10 - y2)**2)**1.5
    
    
    dxdt10= v_x10
    dv_xdt10 = - G * m3 * (x10 - x3) / ((x10 - x3)**2 + (y10 - y3)**2)**1.5
    
    dydt10= v_y10
    dv_ydt10 = - G * m3 * (y10 - y3) / ((x10 - x3)**2 + (y10 - y3)**2)**1.5
    
    
    dxdt10= v_x10
    dv_xdt10 = - G * m4 * (x10 - x4) / ((x10 - x4)**2 + (y10 - y4)**2)**1.5
    
    dydt10= v_y10
    dv_ydt10 = - G * m4 * (y10 - y4) / ((x10 - x4)**2 + (y10 - y4)**2)**1.5
    
    
    dxdt10= v_x10
    dv_xdt10 = - G * m5 * (x10 - x5) / ((x10 - x5)**2 + (y10 - y5)**2)**1.5
    
    dydt10= v_y10
    dv_ydt10 = - G * m5 * (y10 - y5) / ((x10 - x5)**2 + (y10 - y5)**2)**1.5

    
    dxdt10= v_x10
    dv_xdt10 = - G * m6 * (x10 - x6) / ((x10 - x6)**2 + (y10 - y6)**2)**1.5
    
    dydt10= v_y10
    dv_ydt10 = - G * m6 * (y10 - y6) / ((x10 - x6)**2 + (y10 - y6)**2)**1.5
    
    
    dxdt10= v_x10
    dv_xdt10 = - G * m7 * (x10 - x7) / ((x10 - x7)**2 + (y10 - y7)**2)**1.5
    
    dydt10= v_y10
    dv_ydt10 = - G * m7 * (y10 - y7) / ((x10 - x7)**2 + (y10 - y7)**2)**1.5
    
    
    dxdt10= v_x10
    dv_xdt10 = - G * m8 * (x10 - x8) / ((x10 - x8)**2 + (y10 - y8)**2)**1.5
    
    dydt10= v_y10
    dv_ydt10 = - G * m8 * (y10 - y8) / ((x10 - x8)**2 + (y10 - y8)**2)**1.5
    
    
    dxdt10= v_x9
    dv_xdt10 = - G * m9 * (x10 - x9) / ((x10 - x9)**2 + (y10 - y9)**2)**1.5
    
    dydt10 = v_y10
    dv_ydt10= - G * m9 * (y10 - y9) / ((x10 - x9)**2 + (y10 - y9)**2)**1.5


    
    

    return (dxdt1, dv_xdt1, dydt1, dv_ydt1,
            dxdt2, dv_xdt2, dydt2, dv_ydt2,
            dxdt3, dv_xdt3, dydt3, dv_ydt3,
            dxdt4, dv_xdt4, dydt4, dv_ydt4,
            dxdt5, dv_xdt5, dydt5, dv_ydt5,
            dxdt6, dv_xdt6, dydt6, dv_ydt6,
            dxdt7, dv_xdt7, dydt7, dv_ydt7,
            dxdt8, dv_xdt8, dydt8, dv_ydt8,
            dxdt9, dv_xdt9, dydt9, dv_ydt9,
            dxdt10, dv_xdt10, dydt10, dv_ydt10,)


# Определяем начальные значения и параметры
R1=2439000
R2=6051000
R3=6371000
R4=3390000
R5=69911000
R6=58232000
R7=25363000
R8=24634000
R9=8000000
R10=696000000


x10 = 0
v_x10 =0
y10 = 0
v_y10 = 0

x20 =1*10**11
v_x20 = 0
y20 = 0
v_y20 = 0

x30=2*10**11
v_x30=0
y30=0
v_y30=0

x40=3*10**12
v_x40=0
y40=0
v_y40=0

x50=4*10**11
v_x50=0
y50=0
v_y50=0

x60=5*10*11
v_x60=0
y60=0
v_y60=0

x70=6*10**11
v_x70=0
y70=0
v_y70=0

x80=7*10**11
v_x80=0
y80=0
v_y80=0

x90=8*10**11
v_x90=0
y90=0
v_y90=0

x100=9*10**11
v_x100=0
y100=0
v_y100=0

s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,
      x70, v_x70, y70, v_y70,
      x80, v_x80, y80, v_y80,
      x90, v_x90, y90, v_y90,
      x100, v_x100, y100, v_y100,)
      

m1 = 1.1 * 10**(28)
m2 = 1.1 * 10**(28)
m3 = 1.1 * 10**(28)
m4 = 1.1 * 10**(28)
m5 = 1.1 * 10**(28)
m6 = 1.1 * 10**(28)
m7 = 1.1 * 10**(28)
m8 = 1.1 * 10**(28)
m9 = 1.1 * 10**(28)
m10 = 2*10**30
G = 6.67 * 10**(-11)

# Проверка на условия столкновения
move_array = np.ndarray(shape=(len(t), 20)) # Массив для записи координат

for i in range(len(t)-1):

    # Разбиваем все время t на маленькие промежутки tau
    tau = [t[i], t[i+1]]

    # Решаем задачу в маленьком промежутке времени tau
    sol = odeint(move_func, s0, tau)

    # Записываем координаты новых положений в массив
    move_array[i, 0] = sol[1,0]
    move_array[i, 1] = sol[1,2]
    
    move_array[i, 2] = sol[1,4]
    move_array[i, 3] = sol[1,6]
    
    move_array[i, 4] = sol[1,8]
    move_array[i, 5] = sol[1,10]
    
    move_array[i, 6] = sol[1,12]
    move_array[i, 7] = sol[1,14]
    
    move_array[i, 8] = sol[1,16]
    move_array[i, 9] = sol[1,18]
    
    move_array[i, 10] = sol[1,20]
    move_array[i, 11] = sol[1,22]
    
    move_array[i, 12] = sol[1,24]
    move_array[i, 13] = sol[1,26]
    
    move_array[i, 14] = sol[1,28]
    move_array[i, 15] = sol[1,30]
    
    move_array[i, 16] = sol[1,32]
    move_array[i, 17] = sol[1,34]
    
    move_array[i, 18] = sol[1,36]
    move_array[i, 19] = sol[1,38]
    
    

    # Определенные положения и скорости становяться начальными условиями для
    # следующего маленького промежутка времени tau
    x10 = sol[1,0]
    v_x10 = sol[1,1]
    y10 = sol[1,2]
    v_y10 = sol[1,3]

    x20 = sol[1,4]
    v_x20 = sol[1,5]
    y20 = sol[1,6]
    v_y20 = sol[1,7]

    x30=sol[1,8]
    v_x30=sol[1,9]
    y30=sol[1,10]
    v_y30=sol[1,11]
    
    x40=sol[1,12]
    v_x40=sol[1,13]
    y40=sol[1,14]
    v_y40=sol[1,15]
    
    x50=sol[1,16]
    v_x50=sol[1,17]
    y50=sol[1,18]
    v_y50=sol[1,19]
    
    x60=sol[1,20]
    v_x60=sol[1,21]
    y60=sol[1,22]
    v_y60=sol[1,23]
    
    x70=sol[1,24]
    v_x70=sol[1,25]
    y70=sol[1,26]
    v_y70=sol[1,27]
    
    x80=sol[1,28]
    v_x80=sol[1,29]
    y80=sol[1,30]
    v_y80=sol[1,31]
    
    x90=sol[1,32]
    v_x90=sol[1,33]
    y90=sol[1,34]
    v_y90=sol[1,35]
    
    x100=sol[1,36]
    v_x100=sol[1,37]
    y100=sol[1,38]
    v_y10=sol[1,39]

    # Проверка на столкновение и пересчет условий
    r12 = np.sqrt((x10 - x20)**2 + (y10 - y20)**2)
    if r12 <= (R1+R2):
        V_x10 = (2 * m2 * v_x20 + v_x10 * (m1 - m2)) / (m1 + m2)
        V_x20 = (2 * m1 * v_x10 + v_x20 * (m2 - m1)) / (m1 + m2)
    else:
        V_x10 = v_x10
        V_x20 = v_x20

    s0 = (x10, V_x10, y10, v_y10,
      x20, V_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,
      x70, v_x70, y70, v_y70,
      x80, v_x80, y80, v_y80,
      x90, v_x90, y90, v_y90,
      x100, v_x100, y100, v_y100)
    
    


    r13 = np.sqrt((x10 - x30)**2 + (y10 - y30)**2)
    if r13 <= (R1+R3):
        V_x10 = (2 * m3 * v_x30 + v_x10 * (m1 - m3)) / (m1 + m3)
        V_x30 = (2 * m1 * v_x10 + v_x30 * (m3 - m1)) / (m1 + m3)
    else:
        V_x10 = v_x10
        V_x30 = v_x30

    s0 = (x10, V_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, V_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,
      x70, v_x70, y70, v_y70,
      x80, v_x80, y80, v_y80,
      x90, v_x90, y90, v_y90,
      x100, v_x100, y100, v_y100)
      
      
          

    
    r14 = np.sqrt((x10 - x40)**2 + (y10 - y40)**2)
    if r14 <= (R1+R4):
        V_x10 = (2 * m4 * v_x40 + v_x10 * (m1 - m4)) / (m1 + m4)
        V_x40 = (2 * m1 * v_x10 + v_x40 * (m4 - m1)) / (m1 + m4)
    else:
        V_x10 = v_x10
        V_x40 = v_x40

    s0 = (x10, V_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, V_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,
      x70, v_x70, y70, v_y70,
      x80, v_x80, y80, v_y80,
      x90, v_x90, y90, v_y90,
      x100, v_x100, y100, v_y100)
    
    
    
    
    r15 = np.sqrt((x10 - x50)**2 + (y10 - y50)**2)
    if r15 <= (R1+R5):
        V_x10 = (2 * m5 * v_x50 + v_x10 * (m1 - m5)) / (m1 + m5)
        V_x50 = (2 * m1 * v_x10 + v_x50 * (m5 - m1)) / (m1 + m5)
    else:
        V_x10 = v_x10
        V_x50 = v_x50

    s0 = (x10, V_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, V_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,
      x70, v_x70, y70, v_y70,
      x80, v_x80, y80, v_y80,
      x90, v_x90, y90, v_y90,
      x100, v_x100, y100, v_y100)
    
    
    
    
    r16 = np.sqrt((x10 - x60)**2 + (y10 - y60)**2)
    if r16 <= (R1+R6):
        V_x10 = (2 * m6 * v_x60 + v_x10 * (m1 - m6)) / (m1 + m6)
        V_x60 = (2 * m1 * v_x10 + v_x60 * (m6 - m1)) / (m1 + m6)
    else:
        V_x10 = v_x10
        V_x60 = v_x60

    s0 = (x10, V_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, V_x60, y60, v_y60,
      x70, v_x70, y70, v_y70,
      x80, v_x80, y80, v_y80,
      x90, v_x90, y90, v_y90,
      x100, v_x100, y100, v_y100)
    
    
    
    
    r17 = np.sqrt((x10 - x70)**2 + (y10 - y70)**2)
    if r17 <= (R1+R7):
        V_x10 = (2 * m7 * v_x70 + v_x10 * (m1 - m7)) / (m1 + m7)
        V_x70 = (2 * m1 * v_x10 + v_x70 * (m7 - m1)) / (m1 + m7)
    else:
        V_x10 = v_x10
        V_x70 = v_x70

    s0 = (x10, V_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,
      x70, V_x70, y70, v_y70,
      x80, v_x80, y80, v_y80,
      x90, v_x90, y90, v_y90,
      x100, v_x100, y100, v_y100)
    
    
    
    
    r18 = np.sqrt((x10 - x80)**2 + (y10 - y80)**2)
    if r18 <= (R1+R8):
        V_x10 = (2 * m8 * v_x80 + v_x10 * (m1 - m8)) / (m1 + m8)
        V_x80 = (2 * m1 * v_x10 + v_x80 * (m8 - m1)) / (m1 + m8)
    else:
        V_x10 = v_x10
        V_x80 = v_x80

    s0 = (x10, V_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,
      x70, v_x70, y70, v_y70,
      x80, V_x80, y80, v_y80,
      x90, v_x90, y90, v_y90,
      x100, v_x100, y100, v_y100)
    
    
    
    
    r19 = np.sqrt((x10 - x90)**2 + (y10 - y90)**2)
    if r19 <= (R1+R9):
        V_x10 = (2 * m9 * v_x90 + v_x10 * (m1 - m9)) / (m1 + m9)
        V_x90 = (2 * m1 * v_x10 + v_x90 * (m9 - m1)) / (m9 + m3)
    else:
        V_x10 = v_x10
        V_x90 = v_x90

    s0 = (x10, V_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,
      x70, v_x70, y70, v_y70,
      x80, v_x80, y80, v_y80,
      x90, V_x90, y90, v_y90,
      x100, v_x100, y100, v_y100)
    
    
    
    
    r110 = np.sqrt((x10 - x100)**2 + (y10 - y100)**2)
    if r110 <= (R1+R10):
        V_x10 = (2 * m10 * v_x100 + v_x10 * (m1 - m10)) / (m1 + m10)
        V_x100 = (2 * m1 * v_x10 + v_x100 * (m10 - m1)) / (m10 + m3)
    else:
        V_x10 = v_x10
        V_x100 = v_x100

    s0 = (x10, V_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,
      x70, v_x70, y70, v_y70,
      x80, v_x80, y80, v_y80,
      x90, v_x90, y90, v_y90,
      x100, V_x100, y100, v_y100)
    
    
    
    
    r23 = np.sqrt((x30 - x20)**2 + (y30 - y20)**2)
    if r23 <= (R2+R3):
        V_x30 = (2 * m2 * v_x20 + v_x30 * (m3 - m2)) / (m3 + m2)
        V_x20 = (2 * m3 * v_x30 + v_x20 * (m2 - m3)) / (m3 + m2)
    else:
        V_x30 = v_x30
        V_x20 = v_x20

    s0 = (x10, v_x10, y10, v_y10,
      x20, V_x20, y20, v_y20,
      x30, V_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,
      x70, v_x70, y70, v_y70,
      x80, v_x80, y80, v_y80,
      x90, v_x90, y90, v_y90,
      x100, v_x100, y100, v_y100)
    
    
    
    
    
    r24 = np.sqrt((x40 - x20)**2 + (y40 - y20)**2)
    if r24 <= (R2+R4):
        V_x40 = (2 * m2 * v_x20 + v_x30 * (m4 - m2)) / (m4 + m2)
        V_x20 = (2 * m4 * v_x40 + v_x20 * (m2 - m4)) / (m4 + m2)
    else:
        V_x40 = v_x40
        V_x20 = v_x20

    s0 = (x10, v_x10, y10, v_y10,
      x20, V_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, V_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,
      x70, v_x70, y70, v_y70,
      x80, v_x80, y80, v_y80,
      x90, v_x90, y90, v_y90,
      x100, v_x100, y100, v_y100)
    
    
    
    r25 = np.sqrt((x50 - x20)**2 + (y50 - y20)**2)
    if r25 <= (R2+R5):
        V_x50 = (2 * m2 * v_x20 + v_x50 * (m5 - m2)) / (m5 + m2)
        V_x20 = (2 * m5 * v_x50 + v_x20 * (m2 - m5)) / (m5 + m2)
    else:
        V_x50 = v_x50
        V_x20 = v_x20

    s0 = (x10, v_x10, y10, v_y10,
      x20, V_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, V_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,
      x70, v_x70, y70, v_y70,
      x80, v_x80, y80, v_y80,
      x90, v_x90, y90, v_y90,
      x100, v_x100, y100, v_y100)
    
    
    
    r26 = np.sqrt((x60 - x20)**2 + (y60 - y20)**2)
    if r26 <= (R2+R6):
        V_x60 = (2 * m2 * v_x20 + v_x60 * (m6 - m2)) / (m6 + m2)
        V_x20 = (2 * m6 * v_x60 + v_x20 * (m2 - m6)) / (m6 + m2)
    else:
        V_x60 = v_x60
        V_x20 = v_x20

    s0 = (x10, v_x10, y10, v_y10,
      x20, V_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, V_x60, y60, v_y60,
      x70, v_x70, y70, v_y70,
      x80, v_x80, y80, v_y80,
      x90, v_x90, y90, v_y90,
      x100, v_x100, y100, v_y100)
    
    
    
    r27 = np.sqrt((x70 - x20)**2 + (y70 - y20)**2)
    if r27 <= (R2+R7):
        V_x70 = (2 * m2 * v_x20 + v_x70 * (m7 - m2)) / (m7 + m2)
        V_x20 = (2 * m7 * v_x70 + v_x20 * (m2 - m7)) / (m7 + m2)
    else:
        V_x70 = v_x70
        V_x20 = v_x20

    s0 = (x10, v_x10, y10, v_y10,
      x20, V_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,
      x70, V_x70, y70, v_y70,
      x80, v_x80, y80, v_y80,
      x90, v_x90, y90, v_y90,
      x100, v_x100, y100, v_y100)
    
    
    
    r28 = np.sqrt((x80 - x20)**2 + (y80 - y20)**2)
    if r28 <= (R2+R8):
        V_x80 = (2 * m2 * v_x20 + v_x80 * (m8 - m2)) / (m8 + m2)
        V_x20 = (2 * m8 * v_x80 + v_x20 * (m2 - m8)) / (m8 + m2)
    else:
        V_x80 = v_x80
        V_x20 = v_x20

    s0 = (x10, v_x10, y10, v_y10,
      x20, V_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,
      x70, v_x70, y70, v_y70,
      x80, V_x80, y80, v_y80,
      x90, v_x90, y90, v_y90,
      x100, v_x100, y100, v_y100)
    
    
    
    r29 = np.sqrt((x90 - x20)**2 + (y90 - y20)**2)
    if r29<= (R2+R9):
        V_x90 = (2 * m2 * v_x20 + v_x90 * (m9 - m2)) / (m9 + m2)
        V_x20 = (2 * m9 * v_x90 + v_x20 * (m2 - m9)) / (m9 + m2)
    else:
        V_x90 = v_x90
        V_x20 = v_x20

    s0 = (x10, v_x10, y10, v_y10,
      x20, V_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,
      x70, v_x70, y70, v_y70,
      x80, v_x80, y80, v_y80,
      x90, V_x90, y90, v_y90,
      x100, v_x100, y100, v_y100)
    
    
    
    r210 = np.sqrt((x100 - x20)**2 + (y100 - y20)**2)
    if r210 <= (R2+R10):
        V_x100 = (2 * m2 * v_x20 + v_x100 * (m10- m2)) / (m10 + m2)
        V_x20 = (2 * m10 * v_x100 + v_x20 * (m2 - m10)) / (m10 + m2)
    else:
        V_x100 = v_x100
        V_x20 = v_x20

    s0 = (x10, v_x10, y10, v_y10,
      x20, V_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,
      x70, v_x70, y70, v_y70,
      x80, v_x80, y80, v_y80,
      x90, v_x90, y90, v_y90,
      x100, V_x100, y100, v_y100)
    
    
    
    r34 = np.sqrt((x40 - x30)**2 + (y40 - y30)**2)
    if 34 <= (R3+R4):
        V_x40 = (2 * m3 * v_x30 + v_x30 * (m4 - m3)) / (m4 + m3)
        V_x30 = (2 * m4 * v_x40 + v_x30 * (m3 - m4)) / (m4 + m3)
    else:
        V_x40 = v_x40
        V_x30 = v_x30

    s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, V_x30, y30, v_y30,
      x40, V_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,
      x70, v_x70, y70, v_y70,
      x80, v_x80, y80, v_y80,
      x90, v_x90, y90, v_y90,
      x100, v_x100, y100, v_y100)
    
    
    
    r35 = np.sqrt((x50 - x30)**2 + (y50 - y30)**2)
    if r35 <= (R3+R5):
        V_x50 = (2 * m3 * v_x30 + v_x50 * (m5 - m3)) / (m5 + m3)
        V_x30 = (2 * m5 * v_x50 + v_x30 * (m3 - m5)) / (m5 + m3)
    else:
        V_x50 = v_x50
        V_x30 = v_x30

    s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, V_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, V_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,
      x70, v_x70, y70, v_y70,
      x80, v_x80, y80, v_y80,
      x90, v_x90, y90, v_y90,
      x100, v_x100, y100, v_y100)
    
    
    
    r36 = np.sqrt((x60 - x30)**2 + (y60 - y30)**2)
    if r36 <= (R3+R6):
        V_x60 = (2 * m3 * v_x30 + v_x60 * (m6 - m3)) / (m6 + m3)
        V_x30 = (2 * m6 * v_x60 + v_x30 * (m3 - m6)) / (m6 + m3)
    else:
        V_x60 = v_x60
        V_x30 = v_x30

    s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, V_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, V_x60, y60, v_y60,
      x70, v_x70, y70, v_y70,
      x80, v_x80, y80, v_y80,
      x90, v_x90, y90, v_y90,
      x100, v_x100, y100, v_y100)
    
    
    
    r37 = np.sqrt((x70 - x30)**2 + (y70 - y30)**2)
    if r37 <= (R3+R7):
        V_x70 = (2 * m3 * v_x30 + v_x70 * (m7 - m3)) / (m7 + m3)
        V_x30 = (2 * m7 * v_x70 + v_x30 * (m3 - m7)) / (m7 + m3)
    else:
        V_x70 = v_x70
        V_x30 = v_x30

    s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, V_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,
      x70, V_x70, y70, v_y70,
      x80, v_x80, y80, v_y80,
      x90, v_x90, y90, v_y90,
      x100, v_x100, y100, v_y100)
    
    
    
    r38 = np.sqrt((x80 - x30)**2 + (y80 - y30)**2)
    if r38 <= (R3+R8):
        V_x80 = (2 * m3 * v_x30 + v_x80 * (m8 - m3)) / (m8 + m3)
        V_x30 = (2 * m8 * v_x80 + v_x30 * (m3 - m8)) / (m8 + m3)
    else:
        V_x80 = v_x80
        V_x30 = v_x30

    s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, V_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,
      x70, v_x70, y70, v_y70,
      x80, V_x80, y80, v_y80,
      x90, v_x90, y90, v_y90,
      x100, v_x100, y100, v_y100)
    
    
    
    r39 = np.sqrt((x90 - x30)**2 + (y90 - y30)**2)
    if r39<= (R3+R9):
        V_x90 = (2 * m3 * v_x30 + v_x90 * (m9 - m3)) / (m9 + m3)
        V_x30 = (2 * m9 * v_x90 + v_x30 * (m3 - m9)) / (m9 + m3)
    else:
        V_x90 = v_x90
        V_x30 = v_x30

    s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, V_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,
      x70, v_x70, y70, v_y70,
      x80, v_x80, y80, v_y80,
      x90, V_x90, y90, v_y90,
      x100, v_x100, y100, v_y100)
    
    
    
    r310 = np.sqrt((x100 - x30)**2 + (y100 - y30)**2)
    if r310 <= (R3+R10):
        V_x100 = (2 * m3 * v_x30 + v_x100 * (m10- m3)) / (m10 + m3)
        V_x30 = (2 * m10 * v_x100 + v_x30 * (m3 - m10)) / (m10 + m3)
    else:
        V_x100 = v_x100
        V_x30 = v_x30

    s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, V_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,
      x70, v_x70, y70, v_y70,
      x80, v_x80, y80, v_y80,
      x90, v_x90, y90, v_y90,
      x100, V_x100, y100, v_y100)
    
    
    
    r45 = np.sqrt((x50 - x40)**2 + (y50 - y30)**2)
    if r45 <= (R4+R5):
        V_x50 = (2 * m4 * v_x40 + v_x50 * (m5 - m4)) / (m5 + m4)
        V_x40 = (2 * m5 * v_x50 + v_x40 * (m4 - m5)) / (m5 + m4)
    else:
        V_x50 = v_x50
        V_x40 = v_x40

    s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, V_x40, y40, v_y40,
      x50, V_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,
      x70, v_x70, y70, v_y70,
      x80, v_x80, y80, v_y80,
      x90, v_x90, y90, v_y90,
      x100, v_x100, y100, v_y100)
    
    
    
    r46 = np.sqrt((x60 - x40)**2 + (y60 - y40)**2)
    if r46 <= (R4+R6):
        V_x60 = (2 * m4 * v_x40 + v_x60 * (m6 - m4)) / (m6 + m4)
        V_x40 = (2 * m6 * v_x60 + v_x40 * (m4 - m6)) / (m6 + m4)
    else:
        V_x60 = v_x60
        V_x40 = v_x40

    s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, V_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, V_x60, y60, v_y60,
      x70, v_x70, y70, v_y70,
      x80, v_x80, y80, v_y80,
      x90, v_x90, y90, v_y90,
      x100, v_x100, y100, v_y100)
    
    
    
    r47 = np.sqrt((x70 - x40)**2 + (y70 - y40)**2)
    if r47 <= (R4+R7):
        V_x70 = (2 * m4 * v_x40 + v_x70 * (m7 - m4)) / (m7 + m4)
        V_x30 = (2 * m7 * v_x70 + v_x40 * (m4 - m7)) / (m7 + m4)
    else:
        V_x70 = v_x70
        V_x40 = v_x40

    s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, V_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,
      x70, V_x70, y70, v_y70,
      x80, v_x80, y80, v_y80,
      x90, v_x90, y90, v_y90,
      x100, v_x100, y100, v_y100)
    
    
    
    r48 = np.sqrt((x80 - x40)**2 + (y80 - y40)**2)
    if r48 <= (R4+R8):
        V_x80 = (2 * m4 * v_x40 + v_x80 * (m8 - m4)) / (m8 + m4)
        V_x40 = (2 * m8 * v_x80 + v_x40 * (m4 - m8)) / (m8 + m4)
    else:
        V_x80 = v_x80
        V_x40 = v_x40

    s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, V_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,
      x70, v_x70, y70, v_y70,
      x80, V_x80, y80, v_y80,
      x90, v_x90, y90, v_y90,
      x100, v_x100, y100, v_y100)
    
    
    
    r49 = np.sqrt((x90 - x40)**2 + (y90 - y40)**2)
    if r49<= (R4+R9):
        V_x90 = (2 * m4 * v_x40 + v_x90 * (m9 - m4)) / (m9 + m4)
        V_x40 = (2 * m9 * v_x90 + v_x40 * (m4 - m9)) / (m9 + m4)
    else:
        V_x90 = v_x90
        V_x40 = v_x40

    s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, V_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,
      x70, v_x70, y70, v_y70,
      x80, v_x80, y80, v_y80,
      x90, V_x90, y90, v_y90,
      x100, v_x100, y100, v_y100)
    
    
    
    r410 = np.sqrt((x100 - x40)**2 + (y100 - y40)**2)
    if r410 <= (R4+R10):
        V_x100 = (2 * m4 * v_x40 + v_x100 * (m10- m4)) / (m10 + m4)
        V_40 = (2 * m10 * v_x100 + v_x40 * (m4 - m10)) / (m10 + m4)
    else:
        V_x100 = v_x100
        V_x40 = v_x40

    s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, V_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,
      x70, v_x70, y70, v_y70,
      x80, v_x80, y80, v_y80,
      x90, v_x90, y90, v_y90,
      x100, V_x100, y100, v_y100)
    
    
    
    r56 = np.sqrt((x60 - x50)**2 + (y60 - y50)**2)
    if r56 <= (R5+R6):
        V_x60 = (2 * m5 * v_x50 + v_x60 * (m6 - m5)) / (m6 + m5)
        V_x50 = (2 * m6 * v_x60 + v_x50 * (m5 - m6)) / (m6 + m5)
    else:
        V_x60 = v_x60
        V_50 = v_x50

    s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, V_x50, y50, v_y50,
      x60, V_x60, y60, v_y60,
      x70, v_x70, y70, v_y70,
      x80, v_x80, y80, v_y80,
      x90, v_x90, y90, v_y90,
      x100, v_x100, y100, v_y100)
    
    
    
    r57 = np.sqrt((x70 - x50)**2 + (y70 - y50)**2)
    if r57 <= (R5+R7):
        V_x70 = (2 * m5 * v_x50 + v_x70 * (m7 - m5)) / (m7 + m5)
        V_x50 = (2 * m7 * v_x70 + v_x50 * (m5 - m7)) / (m7 + m5)
    else:
        V_x70 = v_x70
        V_x50 = v_x50

    s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, V_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,
      x70, V_x70, y70, v_y70,
      x80, v_x80, y80, v_y80,
      x90, v_x90, y90, v_y90,
      x100, v_x100, y100, v_y100)
    
    
    
    r58 = np.sqrt((x80 - x50)**2 + (y80 - y50)**2)
    if r58 <= (R5+R8):
        V_x80 = (2 * m5 * v_x50 + v_x80 * (m8 - m5)) / (m8 + m5)
        V_x50 = (2 * m8 * v_x80 + v_x50 * (m5 - m8)) / (m8 + m5)
    else:
        V_x80 = v_x80
        V_x50 = v_x50

    s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, V_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,
      x70, v_x70, y70, v_y70,
      x80, V_x80, y80, v_y80,
      x90, v_x90, y90, v_y90,
      x100, v_x100, y100, v_y100)
    
    
    
    r59 = np.sqrt((x90 - x50)**2 + (y90 - y50)**2)
    if r59<= (R5+R9):
        V_x90 = (2 * m5 * v_x50 + v_x90 * (m9 - m5)) / (m9 + m5)
        V_x50 = (2 * m9 * v_x90 + v_x50 * (m5 - m9)) / (m9 + m5)
    else:
        V_x90 = v_x90
        V_x50 = v_x50

    s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, V_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,
      x70, v_x70, y70, v_y70,
      x80, v_x80, y80, v_y80,
      x90, V_x90, y90, v_y90,
      x100, v_x100, y100, v_y100)
    
    
    
    r510 = np.sqrt((x100 - x50)**2 + (y100 - y50)**2)
    if r510 <= (R5+R10):
        V_x100 = (2 * m5 * v_x50 + v_x100 * (m10- m5)) / (m10 + m5)
        V_50 = (2 * m10 * v_x100 + v_x50 * (m5 - m10)) / (m10 + m5)
    else:
        V_x100 = v_x100
        V_x50 = v_x50

    s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, V_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,
      x70, v_x70, y70, v_y70,
      x80, v_x80, y80, v_y80,
      x90, v_x90, y90, v_y90,
      x100, V_x100, y100, v_y100)
    
    
    
    r67 = np.sqrt((x70 - x60)**2 + (y70 - y60)**2)
    if r67 <= (R6+R7):
        V_x70 = (2 * m6 * v_x60 + v_x70 * (m7 - m6)) / (m7 + m6)
        V_x60 = (2 * m7 * v_x70 + v_x60 * (m6 - m7)) / (m7 + m6)
    else:
        V_x70 = v_x70
        V_x60 = v_x60

    s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, V_x60, y60, v_y60,
      x70, V_x70, y70, v_y70,
      x80, v_x80, y80, v_y80,
      x90, v_x90, y90, v_y90,
      x100, v_x100, y100, v_y100)
    
    
    
    r68 = np.sqrt((x80 - x60)**2 + (y80 - y60)**2)
    if r68 <= (R6+R8):
        V_x80 = (2 * m6 * v_x60 + v_x80 * (m8 - m6)) / (m8 + m6)
        V_x60 = (2 * m8 * v_x80 + v_x60 * (m6 - m8)) / (m8 + m6)
    else:
        V_x80 = v_x80
        V_x60 = v_x60

    s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, V_x60, y60, v_y60,
      x70, v_x70, y70, v_y70,
      x80, V_x80, y80, v_y80,
      x90, v_x90, y90, v_y90,
      x100, v_x100, y100, v_y100)
    
    
    
    r69 = np.sqrt((x90 - x60)**2 + (y90 - y60)**2)
    if r69<= (R6+R9):
        V_x90 = (2 * m6 * v_x60 + v_x90 * (m9 - m6)) / (m9 + m6)
        V_x60 = (2 * m9 * v_x90 + v_x60 * (m6 - m9)) / (m9 + m6)
    else:
        V_x90 = v_x90
        V_x60 = v_x60

    s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, V_x60, y60, v_y60,
      x70, v_x70, y70, v_y70,
      x80, v_x80, y80, v_y80,
      x90, V_x90, y90, v_y90,
      x100, v_x100, y100, v_y100)
    
    
    
    r610 = np.sqrt((x100 - x60)**2 + (y100 - y60)**2)
    if r610 <= (R6+R10):
        V_x100 = (2 * m6 * v_x60 + v_x100 * (m10- m6)) / (m10 + m6)
        V_60 = (2 * m10 * v_x100 + v_x60 * (m6 - m10)) / (m10 + m6)
    else:
        V_x100 = v_x100
        V_x60 = v_x60

    s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, V_x60, y60, v_y60,
      x70, v_x70, y70, v_y70,
      x80, v_x80, y80, v_y80,
      x90, v_x90, y90, v_y90,
      x100, V_x100, y100, v_y100)
    
    
    
    r78 = np.sqrt((x80 - x70)**2 + (y80 - y70)**2)
    if r78 <= (R7+R8):
        V_x80 = (2 * m7 * v_x70 + v_x80 * (m8 - m7)) / (m8 + m7)
        V_x70 = (2 * m8 * v_x80 + v_x70 * (m7 - m8)) / (m8 + m7)
    else:
        V_x80 = v_x80
        V_x70 = v_x70

    s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,
      x70, V_x70, y70, v_y70,
      x80, V_x80, y80, v_y80,
      x90, v_x90, y90, v_y90,
      x100, v_x100, y100, v_y100)
    
    
    
    r79 = np.sqrt((x90 - x70)**2 + (y90 - y70)**2)
    if r79<= (R7+R9):
        V_x90 = (2 * m7 * v_x70 + v_x90 * (m9 - m7)) / (m9 + m7)
        V_x70 = (2 * m9 * v_x90 + v_x70 * (m7 - m9)) / (m9 + m7)
    else:
        V_x90 = v_x90
        V_x70 = v_x70

    s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,
      x70, V_x70, y70, v_y70,
      x80, v_x80, y80, v_y80,
      x90, V_x90, y90, v_y90,
      x100, v_x100, y100, v_y100)
    
    
    
    r710 = np.sqrt((x100 - x70)**2 + (y100 - y70)**2)
    if r710 <= (R7+R10):
        V_x100 = (2 * m7 * v_x70 + v_x100 * (m10- m7)) / (m10 + m7)
        V_70 = (2 * m10 * v_x100 + v_x70 * (m7 - m10)) / (m10 + m7)
    else:
        V_x100 = v_x100
        V_x70 = v_x70

    s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,
      x70, V_x70, y70, v_y70,
      x80, v_x80, y80, v_y80,
      x90, v_x90, y90, v_y90,
      x100, V_x100, y100, v_y100)
    
    
    
    r89 = np.sqrt((x90 - x80)**2 + (y90 - y80)**2)
    if r89<= (R8+R9):
        V_x90 = (2 * m8 * v_x80 + v_x90 * (m9 - m8)) / (m9 + m8)
        V_x80 = (2 * m9 * v_x90 + v_x80 * (m8 - m9)) / (m9 + m8)
    else:
        V_x90 = v_x90
        V_x80 = v_x80

    s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,
      x70, v_x70, y70, v_y70,
      x80, V_x80, y80, v_y80,
      x90, V_x90, y90, v_y90,
      x100, v_x100, y100, v_y100)
    
    
    
    r810 = np.sqrt((x100 - x80)**2 + (y100 - y80)**2)
    if r810 <= (R8+R10):
        V_x100 = (2 * m8 * v_x80 + v_x100 * (m10- m8)) / (m10 + m8)
        V_80 = (2 * m10 * v_x100 + v_x80 * (m8 - m10)) / (m10 + m8)
    else:
        V_x100 = v_x100
        V_x80 = v_x80

    s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,
      x70, v_x70, y70, v_y70,
      x80, V_x80, y80, v_y80,
      x90, v_x90, y90, v_y90,
      x100, V_x100, y100, v_y100)
    
    
    
    r910 = np.sqrt((x100 - x90)**2 + (y100 - y90)**2)
    if r810 <= (R9+R10):
        V_x100 = (2 * m9 * v_x90 + v_x100 * (m10- m9)) / (m10 + m9)
        V_90 = (2 * m10 * v_x100 + v_x90 * (m9 - m10)) / (m10 + m9)
    else:
        V_x100 = v_x100
        V_x90 = v_x90

    s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,
      x70, v_x70, y70, v_y70,
      x80, v_x80, y80, v_y80,
      x90, V_x90, y90, v_y90,
      x100, V_x100, y100, v_y100)
    
    
    




# Строим решение в виде графика и анимируем
fig = plt.figure()

bodys = []

for i in range(0, len(t)-1, 1):
    body1, = plt.plot(move_array[i, 0], move_array[i, 1], 'o', color='r', ms=3)
    # body1_line, = plt.plot(move_array[:i, 0], move_array[:i, 1], '-', color='r')

    body2, = plt.plot(move_array[i, 2], move_array[i, 3], 'o', color='g', ms=3)
    # body2_line, = plt.plot(move_array[:i, 2], move_array[:i, 3], '-', color='g')

    body3, = plt.plot(move_array[i, 4], move_array[i, 5], 'o', color='k', ms=3)
    # body2_line, = plt.plot(move_array[:i, 2], move_array[:i, 3], '-', color='g')
    
    body4, = plt.plot(move_array[i, 6], move_array[i, 7], 'o', color='r', ms=3)
                      
                      
    body5, = plt.plot(move_array[i, 8], move_array[i, 9], 'o', color='r', ms=3)
    
    
    body6, = plt.plot(move_array[i, 10], move_array[i, 11], 'o', color='r', ms=3)
    
    
    body7, = plt.plot(move_array[i, 12], move_array[i, 13], 'o', color='r', ms=3)
    
    
    body8, = plt.plot(move_array[i, 14], move_array[i, 15], 'o', color='r', ms=3)
    
    
    body9, = plt.plot(move_array[i, 16], move_array[i, 17], 'o', color='r', ms=3)
    
    
    body10, = plt.plot(move_array[i, 18], move_array[i, 19], 'o', color='r', ms=3)
                      

    bodys.append([body1, body2, body3, body4, body5, body6, body7, body8, body9, body10])

ani = ArtistAnimation(fig, bodys, interval=1)


ani.save('Конец Начал.gif')
plt.show()
