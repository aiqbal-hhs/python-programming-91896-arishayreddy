#Create turtle
import turtle
tina = turtle.Turtle()
tina.color("lightGreen")
tina.pensize(8)

#Draw a light green square with yellow fill
tina.fillcolor("yellow")
tina.begin_fill()
tina.forward(200)
tina.left(90)
tina.forward(200)
tina.left(90)
tina.forward(200)
tina.left(90)
tina.forward(200)
tina.left(90)
tina.end_fill()
