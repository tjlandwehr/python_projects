import turtle
from itertools import cycle

colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])

def draw_circle(size, angle, shift):
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size + 5, angle + 1, shift + 1)

def main():
    turtle.bgcolor('black')
    turtle.speed(10)
    turtle.pensize(4)

    turtle.pencolor('red')
    draw_circle(30, 0, 1)

if __name__ == "__main__":
    main()