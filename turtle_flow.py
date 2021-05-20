import turtle

def first_move(name,length,times,way):

    size = int(length / 2)

    for element in range(times):
        name.forward(size)
        name.left(way)

def main():
   turtles = turtle.Turtle()

   # place to show draw exercises: 
    
   turtles.speed(2)
   first_move(turtles,50,50,10)

   ###############################

   screen_turtle = turtles.Screen()
   screen_turtle.exitonclick()
main()