import turtle

"""def draw_square(turtle1):
    turtle1 = turtle.Turtle()
    count = 0
    for count in range(0,4):
        turtle1.forward(100)
        turtle1.right(90)"""


"""def draw_circle():
    window = turtle.Screen()
    window.bgcolor("yellow")
    turtle1 = turtle.Turtle
    for count in range(0,37):
        draw_square(turtle1)
        turtle1.right(10)
draw_circle()"""

#main code starts from here

def draw_circle_square():
    window = turtle.Screen()
    window.bgcolor("yellow")
    turtle1 = turtle.Turtle()
    for i in range(0,37):
        for count in range(0,4):
            turtle1.forward(100)
            turtle1.right(90)
        turtle1.right(10)

draw_circle_square()
