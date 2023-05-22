import numpy as np
from Point import Point
from painter import draw

inverse_matrix = [[1/3, -1/6],
                  [-1/3, 2/3]]

def f1(point: Point) -> float:
    '''Первое уравнение системы'''
    return point.x**2 + (point.y**2)/4 - 1


def f2(point: Point, a, b, R) -> float:
    '''Второе уравнение системы'''
    return (point.x - a)**2 + (point.y-b)**2 - R**2


def main():
    x_start = float(input('x>'))
    y_start = float(input('y>'))
    a = float(input('a>'))
    b = float(input('b>'))
    R = float(input('R>'))
    eps = float(input('eps>'))

    points = []
    points.append(Point(x=x_start, y=y_start))

    # Метод Ньютона
    system = [0.0, 0.0]
    counter = 0
    while True:
        counter = counter + 1

        # вычисление системы на текущем шаге
        system[0] = f1(points[-1])
        system[1] = f2(points[-1], a, b, R)

        # новое приближение
        points.append(Point(x=points[-1].x-inverse_matrix[0][0]*system[0] - 
                            inverse_matrix[0][1]*system[1],

                            y=points[-1].y-inverse_matrix[1][0]*system[0] -
                            inverse_matrix[1][1]*system[1]))

        # проверка достижения точности 
        if max(abs(points[-1].x - points[-2].x), abs(points[-1].y - points[-2].y)) < eps:
            break

    x = points[-1].x
    y = points[-1].y
    print(f'Результат x = {x}, y = {y} при точности {eps} достигнут после {counter} шагов')
    #draw(points)

        


if __name__ == '__main__':
    main()
