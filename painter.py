from matplotlib.collections import EllipseCollection
from matplotlib.patches import Ellipse
import numpy as np
import matplotlib.pyplot as plt
from Point import Point
from Interval import Interval

#from main import f1, f2

STEP_X = 0.001
DOT_COLOR = '#c9007a'
DOT_COLOR_2 = '#000dc9'

def draw(points: list[Point]) -> None:
    '''Отрисовка фукнции и точек'''
    # настройка поля для рисования
    plt.ylabel('y')
    plt.xlabel('x')

    # получение интервала и его разбиение с шагом STEP_X
    interval = get_interval(points)
    #x_range = np.arange(interval.left, interval.right, STEP_X)

    # отрисовка эллипсов и точек
    plt.gca().set_aspect('equal')
    #, adjustable='box'
    ax = plt.gca()
    ax.add_patch(Ellipse(xy=(0.0, 0.0), width=2, height=4, fill=False))
    ax.add_patch(Ellipse(xy=(1.0, 1.0), width=1, height=1, fill=False))

    for i in range(1, len(points)):
        plt.plot([points[i].x, points[i].y], 
                 [points[i-1].x, points[i-1].y])
    plt.legend()
    plt.show()
    plt.grid(True)


def get_interval(points: list[Point]) -> Interval:
    '''Возвращает границы интервала расположения точек points'''
    left = points[0].x
    right = points[0].x
    for point in points:
        x = point.x
        if x < left:
            left = x
        if x > right:
            right = x
    return Interval(left=left, right=right)
