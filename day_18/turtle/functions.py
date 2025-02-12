def draw_shape(turtle, number_of_sides):
    angle = 360 / number_of_sides
    for number in range(number_of_sides):
        turtle.right(angle)
        turtle.forward(100)

def draw_spirograph(turtle, offset, number_of_circles):
    for number in range(number_of_circles):
        turtle.setheading(turtle.heading() + offset)
        turtle.circle(100)
