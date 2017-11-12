import turtle

def rectangle(turtle, horizontal, vertical, color):
    turtle.pendown()
    turtle.pensize(1)
    turtle.color(color)
    turtle.begin_fill()
    for counter in range(1, 3):
        turtle.forward(horizontal)
        turtle.right(90)
        turtle.forward(vertical)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()

def main():
    t = turtle.Turtle()
    wn = turtle.Screen()
    t.penup()
    t.speed(0)
    wn.bgcolor('Dodger blue')

    # feet
    t.goto(-100, -150)
    rectangle(t, 50, 20, 'blue')
    t.goto(-30, -150)
    rectangle(t, 50, 20, 'blue')

    # legs
    t.goto(-25, -49)
    rectangle(t, 15, 100, 'grey')
    t.goto(-55, -49)
    rectangle(t, -15, 100, 'grey')

    # body
    t.goto(-90, 100)
    rectangle(t, 100, 150, 'red')

    # arms
    t.goto(-151, 70)
    rectangle(t, 60, 15, 'grey')
    t.goto(-151, 110)
    rectangle(t, 15, 40, 'grey')

    t.goto(11, 70)
    rectangle(t, 60, 15, 'grey')
    t.goto(56, 110)
    rectangle(t, 15, 40, 'grey')
    
    # neck
    t.goto(-50, 121)
    rectangle(t, 15, 20, 'grey')

    # head
    t.goto(-85, 171)
    rectangle(t, 80, 50, 'red')

    # eyes
    t.goto(-60, 160)
    rectangle(t, 30, 10, 'white')
    t.goto(-55, 157)
    rectangle(t, 5, 5, 'black')
    t.goto(-40, 157)
    rectangle(t, 5, 5, 'black')

    # mouth
    t.goto(-65, 136)
    rectangle(t, 40, 5, 'black')

    t.hideturtle()

if __name__ == "__main__":
    main()
