import turtle
import random
import sys

# initialization of game settings
animal = turtle.Turtle()
turtle.shape('turtle')

# cosmetics additionally
turtle.bgcolor("lightblue")
turtle.pensize('5')
turtle.speed(5)
turtle.color(random.choice(["blue","red","yellow","brown","purple","white","black"]))

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

# to moving turtle way +add
turtle.listen()
turtle.mainloop()

# exit with [x]
turtle.exitonclick()
