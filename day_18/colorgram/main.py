from turtle import Turtle
import colorgram
from turtle import Screen
import random
from functions import draw_dotted_line, return_home

if __name__ == '__main__':
    colors = colorgram.extract('/Users/adamkroon/Desktop/github/100-days-python/day_18/colorgram/damien-hirst-the-currency-2.jpg', 30)

    color_list = []

    for color in colors:
        r = int(color.rgb.r)
        g = int(color.rgb.g)
        b = int(color.rgb.b)
        new_color = (r,g,b)
        color_list.append(new_color)

    turty = Turtle()
    screen = Screen()
    screen.colormode(255)

    for number in range(10):
        draw_dotted_line(number_of_dots=10, color_list=color_list, turtle=turty)
        return_home(turty, number)

    screen.exitonclick()