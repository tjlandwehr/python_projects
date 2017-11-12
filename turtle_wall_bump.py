import turtle
import random
import math


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


def corner_distance(turtle, screen, quadrant, heading):
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

    if quadrant == "q1":
        if x_right_remaining < 50 and y_up_remaining >= 50:
            distance = (x_right_remaining / math.cos(math.radians(turtle_angle))) - 0.01
            if distance < 50:
                return distance
            else:
                return 50
        elif x_right_remaining >= 50 and y_up_remaining < 50:
            distance = (y_up_remaining / math.sin(math.radians(turtle_angle))) - 0.01
            if distance < 50:
                return distance
            else:
                return 50
        elif x_right_remaining < 50 and y_up_remaining < 50:
            x_hypotenuse = x_right_remaining / math.cos(math.radians(turtle_angle))
            y_hypotenuse = y_up_remaining / math.sin(math.radians(turtle_angle))
            x_add = math.cos(math.radians(turtle_angle)) * y_hypotenuse
            y_add = math.sin(math.radians(turtle_angle)) * x_hypotenuse
            if turtle_x + x_add <= right_bound and turtle_y + y_add <= upper_bound:
                if x_hypotenuse > 50:
                    return 50
                else:
                    return x_hypotenuse - 0.01
            elif turtle_x + x_add > right_bound:
                x_diff = x_add - ((turtle_x + x_add) - right_bound)
                hypotenuse = x_diff / math.cos(math.radians(turtle_angle))
                return hypotenuse - 0.01
            elif turtle_y + y_add > upper_bound:
                y_diff = y_add - ((turtle_y + y_add) - upper_bound)
                hypotenuse = y_diff / math.sin(math.radians(turtle_angle))
                return hypotenuse - 0.01
        else:
            return 50
    elif quadrant == "q2":
        if x_left_remaining < 50 and y_up_remaining >= 50:
            distance = (x_left_remaining / math.cos(math.radians(abs(turtle_angle - 180)))) - 0.01
            if distance < 50:
                return distance
            else:
                return 50
        elif x_left_remaining >= 50 and y_up_remaining < 50:
            distance = (y_up_remaining / math.sin(math.radians(abs(turtle_angle - 180)))) - 0.01
            if distance < 50:
                return distance
            else:
                return 50
        elif x_left_remaining < 50 and y_up_remaining < 50:
            x_hypotenuse = x_left_remaining / math.cos(math.radians(abs(turtle_angle - 180)))
            y_hypotenuse = y_up_remaining / math.sin(math.radians(abs(turtle_angle - 180)))
            x_add = math.cos(math.radians(abs(turtle_angle - 180))) * y_hypotenuse
            y_add = math.sin(math.radians(abs(turtle_angle - 180))) * x_hypotenuse
            if turtle_x - x_add >= left_bound and turtle_y + y_add <= upper_bound:
                if x_hypotenuse > 50:
                    return 50
                else:
                    return x_hypotenuse - 0.01
            elif turtle_x - x_add < left_bound:
                x_diff = x_add - (abs((turtle_x - x_add) - left_bound))
                hypotenuse = x_diff / math.cos(math.radians(abs(turtle_angle - 180)))
                return hypotenuse - 0.01
            elif turtle_y + y_add > upper_bound:
                y_diff = y_add - ((turtle_y + y_add) - upper_bound)
                hypotenuse = y_diff / math.sin(math.radians(abs(turtle_angle - 180)))
                return hypotenuse - 0.01
        else:
            return 50
    elif quadrant == "q3":
        if x_left_remaining < 50 and y_down_remaining >= 50:
            distance = (x_left_remaining / math.cos(math.radians(turtle_angle - 180))) - 0.01
            if distance < 50:
                return distance
            else:
                return 50
        elif x_left_remaining >= 50 and y_down_remaining < 50:
            distance = (y_down_remaining / math.sin(math.radians(turtle_angle - 180))) - 0.01
            if distance < 50:
                return distance
            else:
                return 50
        elif x_left_remaining < 50 and y_down_remaining < 50:
            x_hypotenuse = x_left_remaining / math.cos(math.radians(turtle_angle - 180))
            y_hypotenuse = y_down_remaining / math.sin(math.radians(turtle_angle - 180))
            x_add = math.cos(math.radians(turtle_angle - 180)) * y_hypotenuse
            y_add = math.sin(math.radians(turtle_angle - 180)) * x_hypotenuse
            if turtle_x - x_add >= left_bound and turtle_y - y_add >= lower_bound:
                if x_hypotenuse > 50:
                    return 50
                else:
                    return x_hypotenuse - 0.01
            elif turtle_x - x_add < left_bound:
                x_diff = x_add - (abs((turtle_x - x_add) - left_bound))
                hypotenuse = x_diff / math.cos(math.radians(turtle_angle - 180))
                return hypotenuse - 0.01
            elif turtle_y - y_add < lower_bound:
                y_diff = y_add - (abs((turtle_y - y_add) - lower_bound))
                hypotenuse = y_diff / math.sin(math.radians(turtle_angle - 180))
                return hypotenuse - 0.01
        else:
            return 50
    else:
        if x_right_remaining < 50 and y_down_remaining >= 50:
            distance = (x_right_remaining / math.cos(math.radians(abs(turtle_angle - 360)))) - 0.01
            if distance < 50:
                return distance
            else:
                return 50
        elif x_right_remaining >= 50 and y_down_remaining < 50:
            distance = (y_down_remaining / math.sin(math.radians(abs(turtle_angle - 360)))) - 0.01
            if distance < 50:
                return distance
            else:
                return 50
        elif x_right_remaining < 50 and y_down_remaining < 50:
            x_hypotenuse = x_right_remaining / math.cos(math.radians(abs(turtle_angle - 360)))
            y_hypotenuse = y_down_remaining / math.sin(math.radians(abs(turtle_angle - 360)))
            x_add = math.cos(math.radians(abs(turtle_angle - 360))) * y_hypotenuse
            y_add = math.sin(math.radians(abs(turtle_angle - 360))) * x_hypotenuse
            if turtle_x + x_add <= right_bound and turtle_y - y_add >= lower_bound:
                if x_hypotenuse > 50:
                    return 50
                else:
                    return x_hypotenuse - 0.01
            elif turtle_x + x_add > right_bound:
                x_diff = x_add - ((turtle_x + x_add) - right_bound)
                hypotenuse = x_diff / math.cos(math.radians(abs(turtle_angle - 360)))
                return hypotenuse - 0.01
            elif turtle_y - y_add < lower_bound:
                y_diff = y_add - (abs((turtle_y - y_add) - lower_bound))
                hypotenuse = y_diff / math.sin(math.radians(abs(turtle_angle - 360)))
                return hypotenuse - 0.01
        else:
            return 50


def find_distance(turtle, screen, quadrant, heading):
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

    if quadrant == "q1":
        if heading == "q1":
            return (corner_distance(turtle, screen, quadrant, heading))
        elif heading == "q2":
            if y_up_remaining >= 50:
                return 50
            else:
                distance = (y_up_remaining / math.sin(math.radians(abs(turtle_angle - 180)))) - 0.01
                if distance < 50:
                    return distance
                else:
                    return 50
        elif heading == "q3":
            return 50
        else:
            if x_right_remaining >= 50:
                return 50
            else:
                distance = (x_right_remaining / math.cos(math.radians(abs(turtle_angle - 360)))) - 0.01
                if distance < 50:
                    return distance
                else:
                    return 50
    elif quadrant == "q2":
        if heading == "q1":
            if y_up_remaining >= 50:
                return 50
            else:
                distance = (y_up_remaining / math.sin(math.radians(turtle_angle))) - 0.01
                if distance < 50:
                    return distance
                else:
                    return 50
        elif heading == "q2":
            return (corner_distance(turtle, screen, quadrant, heading))
        elif heading == "q3":
            if x_left_remaining >= 50:
                return 50
            else:
                distance = (x_left_remaining / math.cos(math.radians(turtle_angle - 180))) - 0.01
                if distance < 50:
                    return distance
                else:
                    return 50
        else:
            return 50
    elif quadrant == "q3":
        if heading == "q1":
            return 50
        elif heading == "q2":
            if x_left_remaining >= 50:
                return 50
            else:
                distance = (x_left_remaining / math.cos(math.radians(abs(turtle_angle - 180)))) - 0.01
                if distance < 50:
                    return distance
                else:
                    return 50
        elif heading == "q3":
            return (corner_distance(turtle, screen, quadrant, heading))
        else:
            if y_down_remaining >= 50:
                return 50
            else:
                distance = (y_down_remaining / math.sin(math.radians(abs(turtle_angle - 360)))) - 0.01
                if distance < 50:
                    return distance
                else:
                    return 50
    else:
        if heading == "q1":
            if x_right_remaining >= 50:
                return 50
            else:
                distance = (x_right_remaining / math.cos(math.radians(turtle_angle))) - 0.01
                if distance < 50:
                    return distance
                else:
                    return 50
        elif heading == "q2":
            return 50
        elif heading == "q3":
            if y_down_remaining >= 50:
                return 50
            else:
                distance = (y_down_remaining / math.sin(math.radians(turtle_angle - 180))) - 0.01
                if distance < 50:
                    return distance
                else:
                    return 50
        else:
            return (corner_distance(turtle, screen, quadrant, heading))


def move_distance(screen, turtle):
    # which quadrant is the turtle in?
    quadrant = which_quadrant(turtle)

    # which quadrant is it facing?
    angle_direction = which_direction(turtle)

    return find_distance(turtle, screen, quadrant, angle_direction)


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


def random_move(screen, turtle):
    coin = random.randrange(0, 2)
    if coin == 0:
        turtle.left(random.randrange(0, 180))
    else:
        turtle.right(random.randrange(0, 180))

    distance = move_distance(screen, turtle)
    turtle.forward(distance)
    if distance < 50:
        turtle.right(180)
        turtle.forward(50 - distance)


def main():
    mildred = turtle.Turtle()
    jeb = turtle.Turtle()
    wn = turtle.Screen()

    mildred.shape("turtle")
    mildred.color("red")
    jeb.shape("turtle")
    jeb.color("blue")

    mildred.hideturtle()
    mildred.up()
    jeb.hideturtle()
    jeb.up()

    mildred.setpos(random.randrange(int(-wn.window_width() / 2), int(wn.window_width() / 2)),
                   random.randrange(int(-wn.window_width() / 2), int(wn.window_height() / 2)))
    jeb.setpos(random.randrange(int(-wn.window_width() / 2), int(wn.window_width() / 2)),
               random.randrange(int(-wn.window_width() / 2), int(wn.window_height() / 2)))
    
    # mildred.setpos(random.randrange(-200, 200), random.randrange(-200, 200))
    # jeb.setpos(random.randrange(-200, 200), random.randrange(-200, 200))

    mildred.showturtle()
    mildred.down()
    jeb.showturtle()
    jeb.down()

    while is_in_screen(wn, mildred):
        if not is_in_screen(wn, jeb):
            break
        random_move(wn, mildred)
        random_move(wn, jeb)

    wn.exitonclick()


if __name__ == "__main__":
    main()