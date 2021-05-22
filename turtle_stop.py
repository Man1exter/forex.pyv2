import turtle
import random

# init
tur = turtle.Turtle()
tur.shape('turtle')

# settings
turtle.bgcolor('black')
tur.speed(10)

# drawing loop
for it in range(50,500):
  tur.color(random.choice(["blue","red","yellow","brown","purple"]))
  tur.forward(it)
  tur.right(92)

# for it in range(50,500):
# tur.color(random.choice(["blue","red","yellow","brown","purple"]))
# tur.forward(it)
# tur.right(120)

# exit
tur.exitonclick()