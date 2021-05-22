import turtle
import random

turtle_zoo = turtle.Turtle()

for ele in range(50,300):
  turtle_zoo(random.choice(["blue"]))
  turtle_zoo.forward(ele)
  turtle_zoo.right(91)