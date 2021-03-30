#!/usr/bin/env python3

WIDTH = 30
HEIGHT = 60

def line(matrix, x1, y1, x2, y2):
    if y1 > y2:
       x1, x2 = x2, x1
       y1, y2 = y2, y1

    dx = x2 - x1
    dy = y2 - y1

    if dx > dy:
        for x in range(x1, x2):
            y = y1 + dy * (x - x1) / dx
            matrix[round(y)][round(x)] = 1
    else:
        for y in range(y1, y2):
            x = x1 + dx * (y - y1) / dy
            matrix[round(y)][round(x)] = 1
    matrix[y2][x2] = 1

def house(matrix):
    DOOR_WIDTH = 5
    EAVES_WIDTH = 4
    WINDOW_HEIGHT = 9
    WINDOW_WIDTH = 5

    Y_CHIMNEY_TOP = 3
    Y_CHIMNEY_DOWN_L = 10
    Y_CHIMNEY_DOWN_R = 8
    Y_DOOR_TOP = 42
    Y_GROUND = 59
    Y_ROOF = 20
    Y_TOP = 0
    Y_WINDOW_TOP = 27

    X_CHIMNEY_LEFT = 6
    X_CHIMNEY_RIGHT = X_CHIMNEY_LEFT + 2
    X_DOOR_LEFT = 15
    X_DOOR_RIGHT = X_DOOR_LEFT + DOOR_WIDTH
    X_LEFT = 0
    X_RIGHT = 29
    X_WALL_LEFT = X_LEFT + EAVES_WIDTH
    X_WALL_RIGHT = X_RIGHT - EAVES_WIDTH
    X_MID = round((X_RIGHT - X_LEFT) / 2)
    X_WINDOW_LEFT = 8

    line(matrix, X_WALL_LEFT,  Y_GROUND, X_WALL_LEFT,  Y_ROOF)
    line(matrix, X_WALL_RIGHT, Y_GROUND, X_WALL_RIGHT, Y_ROOF)
    line(matrix, X_LEFT,       Y_ROOF,   X_RIGHT,      Y_ROOF)
    line(matrix, X_LEFT,       Y_ROOF,   X_MID,        Y_TOP)
    line(matrix, X_RIGHT,      Y_ROOF,   X_MID,        Y_TOP)

    line(matrix, X_CHIMNEY_LEFT,  Y_CHIMNEY_TOP,    X_CHIMNEY_RIGHT, Y_CHIMNEY_TOP)
    line(matrix, X_CHIMNEY_LEFT,  Y_CHIMNEY_DOWN_L, X_CHIMNEY_LEFT, Y_CHIMNEY_TOP)
    line(matrix, X_CHIMNEY_RIGHT, Y_CHIMNEY_DOWN_R, X_CHIMNEY_RIGHT, Y_CHIMNEY_TOP)

    for x in [0, WINDOW_WIDTH + 3]:
        right = X_WINDOW_LEFT + WINDOW_WIDTH + x
        top   = Y_WINDOW_TOP + WINDOW_HEIGHT
        x_mid = right - int(WINDOW_WIDTH / 2)
        line(matrix, X_WINDOW_LEFT + x, top,           X_WINDOW_LEFT + x, Y_WINDOW_TOP)
        line(matrix, X_WINDOW_LEFT + x, top,           right,             top)
        line(matrix, X_WINDOW_LEFT + x, Y_WINDOW_TOP,  right,             Y_WINDOW_TOP)
        line(matrix, right,             Y_WINDOW_TOP,  right,             top)
        line(matrix, x_mid,             Y_WINDOW_TOP,  x_mid,             top)

    line(matrix, X_DOOR_LEFT,  Y_GROUND,   X_DOOR_LEFT,  Y_DOOR_TOP)
    line(matrix, X_DOOR_RIGHT, Y_GROUND,   X_DOOR_RIGHT, Y_DOOR_TOP)
    line(matrix, X_DOOR_LEFT,  Y_DOOR_TOP, X_DOOR_RIGHT, Y_DOOR_TOP)
    line(matrix, X_DOOR_RIGHT - 2, int((Y_GROUND + Y_DOOR_TOP) / 2),
                 X_DOOR_RIGHT,     int((Y_GROUND + Y_DOOR_TOP) / 2))

def draw_matrix(matrix):
    for row in matrix:
        print(''.join(['###' if value else '   ' for value in row]))

if __name__ == '__main__':
    matrix = [[0] * WIDTH for i in range(HEIGHT)]
    house(matrix)
    draw_matrix(matrix)
