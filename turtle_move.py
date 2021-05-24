import turtle
import random
import sys

# initialization of game settings
animal = turtle.Turtle()
turtle.shape('turtle')
turtle.bgcolor("yellow")
turtle.color("black")
turtle.pensize('5')
#  turtle.screensize(2000,1500) 

# game events
def up():
    turtle.forward(100)
def left():
    turtle.left(30)
def right():
    turtle.right(30)
def bye():
    turtle.bye()

turtle.onkey(up,'Up')
turtle.onkey(left,'Left')
turtle.onkey(right,'Right')
turtle.onkey(bye,'q')

# to moving turtle way
turtle.listen()
turtle.mainloop()

# exit with [x]
turtle.exitonclick()
