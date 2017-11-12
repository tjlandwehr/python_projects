import turtle

def main():
    t = turtle.Turtle()

    size = 300
    points = 5
    angle = 144

    for i in range(points):
        t.forward(size)
        t.right(angle)

if __name__ == "__main__":
    main()