import turtle

# animal.forward(100)           # forward + px 
# animal.left(90)               # left + deg
# animal.forward(100)
# animal.left(90)
# animal.forward(100)
# animal.left(90)

def super_turtle(name,size,deg):
    for i in range(300):
        name.speed(5)
        name.forward(size)
        name.left(deg)
        
def main():
    animal = turtle.Turtle()     # turtle init to draw
    super_turtle(animal,100,90)
    turtle.exitonclick()         # exit with [X]
main()

# .pencolor( 'blue' )
# .prensize( 10 )