from turtle import Turtle, Screen
from functions import draw_shape, draw_spirograph
from random import choice

if __name__ == '__main__':
    # Define turtle characteristics
    turty = Turtle()
    turty.shape("turtle")
    turty.color("coral")
    color_palette = ["blue", "spring green", "firebrick", "magenta", "blue violet"]

    # draw 10 shapes
    #for number in range(3,11):
    #    turty.pencolor(choice(color_palette))
    #    draw_shape(turty, number)

    # draw a random walk
    #turty.pensize(10)
    #headings = [ 0, 90, 180 , 270]\
    #    turty.pencolor(choice(color_palette))
    #    turty.setheading(direction)
    #    turty.forward(50)

    # draw a Spirograph
    turty.speed("fastest")
    draw_spirograph(turty, 23, 30)

    screen = Screen()
    screen.exitonclick()