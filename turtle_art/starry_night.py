import turtle
from random import randint, random

def draw_planet(col, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(col)
    t.begin_fill()
    t.circle(50)
    t.end_fill()

def draw_star(t, points, size, col, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    angle = 180 - (180 / points)
    t.color(col)
    t.begin_fill()
    for i in range(points):
        t.forward(size)
        t.right(angle)
    t.end_fill()

def main():
    t = turtle.Turtle()
    wn = turtle.Screen()
    t.speed(0)
    t.hideturtle()
    wn.bgcolor('dark blue')
    while True:
        ranPts = randint(2, 5) * 2 + 1
        ranSize = randint(10, 50)
        ranCol = (random(), random(), random())
        ranX = randint(-350, 300)
        ranY = randint(-250, 250)

        draw_star(t, ranPts, ranSize, ranCol, ranX, ranY)

if __name__ == "__main__":
    main()
