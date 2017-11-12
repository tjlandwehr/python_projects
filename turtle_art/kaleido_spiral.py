import turtle
from itertools import cycle

colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])

# def draw_circle(size, angle, shift):
#     turtle.bgcolor(next(colors))
#     turtle.pencolor(next(colors))
#     turtle.circle(size)
#     turtle.right(angle)
#     turtle.forward(shift)
#     draw_circle(size + 5, angle + 1, shift + 1)

def draw_shape(size, angle, shift, shape):
    turtle.pencolor(next(colors))
    next_shape = ''
    if shape == 'circle':
        turtle.circle(size)
        next_shape = 'square'
    elif shape == 'square':
        for i in range(4):
            turtle.forward(size * 2)
            turtle.left(90)
        next_shape = 'circle'
    turtle.right(angle)
    turtle.forward(shift)
    draw_shape(size + 5, angle + 1, shift + 1, next_shape)

def main():
    turtle.bgcolor('black')
    turtle.speed(10)
    turtle.pensize(4)

    turtle.pencolor('red')
    draw_shape(30, 0, 1, 'circle')

if __name__ == "__main__":
    main()
