import turtle

def first_move(name,length,times,way):
    size = int(length / 2)
    for element in range(times):
        name.forward(size)
        name.left(way)

def main():
   turtles = turtle.Turtle()

   # place to show draw exercises: 

   first_move(turtles,100,2,10)

   ###############################

   turtles.exitonclick()
main()