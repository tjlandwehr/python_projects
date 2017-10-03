import random
import turtle


def which_quadrant(turtle):
    if turtle.xcor() >= 0:
        if turtle.ycor() >= 0:
            return "q1"
        else:
            return "q4"
    else:
        if turtle.ycor() >= 0:
            return "q2"
        else:
            return "q3"


def which_direction(turtle):
    if 0 <= turtle.heading() < 90:
        return "q1"
    elif 90 <= turtle.heading() < 180:
        return "q2"
    elif 180 <= turtle.heading() < 270:
        return "q3"
    else:
        return "q4"


def find_distance(turtle, quadrant, angle_direction):
    return True


def move_distance(screen, turtle):
    left_bound = -screen.window_width() / 2
    right_bound = screen.window_width() / 2
    upper_bound = screen.window_height() / 2
    lower_bound = -screen.window_height() / 2

    turtle_x = turtle.xcor()
    turtle_y = turtle.ycor()
    turtle_angle = turtle.heading()

    x_left_remaining = abs(left_bound - turtle_x)
    x_right_remaining = abs(right_bound - turtle_x)
    y_up_remaining = abs(upper_bound - turtle_y)
    y_down_remaining = abs(lower_bound - turtle_y)

    left_hypotenuse = x_left_remaining / math.cos(turtle_angle)
    right_hypotenuse = x_right_remaining / math.cos(turtle_angle)
    up_adjacent = y_up_remaining / math.tan(turtle_angle)
    down_adjacent = y_down_remaining / math.tan(turtle_angle)
    left_opposite = math.tan(turtle_angle) * x_left_remaining
    right_opposite = math.tan(turtle_angle) * x_right_remaining

    # which quadrant is the turtle in?
    quadrant = which_quadrant(turtle)

    # which quadrant is it facing?
    angle_direction = which_direction(turtle)

    # if x is closet
    # once you have those two you know the math you need to do
    # corners will be the most concern
    # which corner closer? function
    turtle.forward(find_distance(turtle, quadrant, angle_direction)

    """
    if turtle_x >= 0 and turtle_y >=0:
        if 180 < turtle_angle < 270:
            turtle.forward(50)
        else:
            if 90 < turtle_angle < 180:
                if y_up_remaining > 50:
                    turtle.forward(50)
                else:
    """ \
    """
    if x_left_remaining < 50:
        if 90 < turtle_angle < 270:
            if turtle_y > 0:
                if y_up_remaining < 50 and y_up_remaining - opposite > 0:
                    print()
                """


def is_in_screen(screen, turtle):
    left_bound = -screen.window_width() / 2
    right_bound = screen.window_width() / 2
    upper_bound = screen.window_height() / 2
    lower_bound = -screen.window_height() / 2

    turtle_x = turtle.xcor()
    turtle_y = turtle.ycor()

    still_in = True

    if turtle_x > right_bound or turtle_x < left_bound:
        still_in = False
    if turtle_y > upper_bound or turtle_y < lower_bound:
        still_in = False
    return still_in


def random_move(turtle):
    coin = random.randrange(0, 2)
    if coin == 0:
        turtle.left(random.randrange(0, 180))
    else:
        turtle.right(random.randrange(0, 180))

    turtle.forward(50)


def main():
    mildred = turtle.Turtle()
    jeb = turtle.Turtle()
    wn = turtle.Screen()

    mildred.shape("turtle")
    jeb.shape("turtle")

    mildred.hideturtle()
    mildred.up()
    jeb.hideturtle()
    jeb.up()

    mildred.setpos(random.randrange(-wn.window_width() / 2, wn.window_width() / 2),
                   random.randrange(-wn.window_width() / 2, wn.window_height() / 2))
    jeb.setpos(random.randrange(-wn.window_width() / 2, wn.window_width() / 2),
               random.randrange(-wn.window_width() / 2, wn.window_height() / 2))

    mildred.showturtle()
    mildred.down()
    jeb.showturtle()
    jeb.down()

    while is_in_screen(wn, mildred):
        if not is_in_screen(wn, jeb):
            break
        random_move(mildred)
        random_move(jeb)

    wn.exitonclick()


if __name__ == "__main__":
    main()