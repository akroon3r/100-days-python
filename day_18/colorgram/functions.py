import random

def draw_dotted_line(number_of_dots, color_list, turtle):
    for number in range(number_of_dots):
        choice = random.choice(color_list)
        turtle.dot(20, choice)
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()

def return_home(turtle, number_of_lines):
    turtle.penup()
    turtle.home()
    turtle.sety(50 * number_of_lines)
    turtle.position()
