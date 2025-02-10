from turtle import Turtle, Screen


if __name__ == '__main__':
    timmy = Turtle()
    print(timmy)
    timmy.shape("turtle")
    timmy.color("coral")
    timmy.forward(100)

    screen = Screen()
    print(screen.canvheight)
    screen.exitonclick()