import turtle
def draw_square():
    window = turtle.Screen() #defining a screen for output
    #more than one output windows can also be defined in same script
    window.bgcolor("red")
    count = 0
    ashish = turtle.Turtle() #instance of class Turtle
    #shape and color or turtle can also be changed by using:
    #ashish.shape("turtle")
    #ashish.color("yellow")

    #first rectangle using for loop
    for count in range(0, 4) :
        ashish.forward(100)
        ashish.right(90)
        count = count + 1

    #second rectangle using for loop
    turtle2 = turtle.Turtle()
    for count in range(0, 4):
        turtle2.forward(200)
        turtle2.left(90)

    # a circle
    turtle3 = turtle.Turtle()
    turtle3.circle(100)

    #triangle
    turtle4 = turtle.Turtle()
    for count in range(0,3):
        turtle4.forward(100)
        turtle4.left(120)


    window.exitonclick()

draw_square()
