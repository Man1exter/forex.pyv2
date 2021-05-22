import turtle
import random

# init + settings
animal = turtle.Turtle()
animal.shape("turtle")

# sett with turtle
turtle.bgcolor("black")
turtle.exitonclick()

# about drawing set
for it in range(50,500):
  animal.color(random.choice(["blue","red","yellow","brown","purple","white"]))
  animal.forward(it)
  animal.right(120)