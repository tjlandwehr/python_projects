import turtle
from itertools import cycle

colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])

def draw_circle(size):
    turtle.pencolor(next(colors))
    turtle.circle(size)
    draw_circle(size + 5)

def main():
    turtle.bgcolor('black')
    turtle.speed(10)
    turtle.pensize(4)

    turtle.pencolor('red')
    draw_circle(30)

if __name__ == "__main__":
    main()