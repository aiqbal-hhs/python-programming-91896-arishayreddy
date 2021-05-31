# You can edit this code and run it right here in the browser!
# First we'll import some turtles and shapes: 
from turtle import *
from shapes import *

# Create a turtle named Tommy:
tommy = Turtle()
tommy.shape("turtle")
tommy.speed(5)

# Draw three Stars:
draw_star(tommy, "silver", 50, 25, 0)
draw_star(tommy, "gold", 50, 0, 0)
draw_star(tommy, "bronze", 50, -25, 0)

# Write a little message:
tommy.penup()
tommy.goto(0,-50)
tommy.color("black")
tommy.write("Stars!", None, "center", "16pt bold")
tommy.goto(0,-80)
