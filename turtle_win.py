import turtle
import random

# init + settings
animal = turtle.Turtle()
animal.shape("turtle")
animal.speed(20)
animal.pensize(5)

# sett with turtle
turtle.bgcolor("black")

# about drawing set
for it in range(50,500):
  animal.color(random.choice(["blue","red","yellow","brown","purple","white"]))
  animal.forward(it + 5)
  animal.right(120)

turtle.exitonclick()