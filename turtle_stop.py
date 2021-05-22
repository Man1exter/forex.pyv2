import turtle
import random

# init
tur = turtle.Turtle()

# settings
turtle.bgcolor('black')

# drawing loop
for it in range(50,300):
  tur.color(random.choice(["blue","red","yellow","brown","purple"]))
  tur.forward(it)
  tur.right(91)

# exit
tur.exitonclick()