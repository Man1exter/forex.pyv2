import turtle

# animal.forward(100)           # forward + px 
# animal.left(90)               # left + deg
# animal.forward(100)
# animal.left(90)
# animal.forward(100)
# animal.left(90)

def super_turtle(name,size,deg):

    for element in range(5):
        name.speed(5)
        name.forward(size)
        name.left(deg)
        name.pensize(5)

def super_turtle_exp(name,size,deg):

    for element in range(5):
        name.speed(5)
        name.forward(size)
        name.right(deg)
        name.pencolor('blue')
        name.pensize(10)

def super_turtle_exp_ten(name,size,deg):

      for element in range(5):
        name.speed(5)
        name.forward(size)
        name.left(deg)
        name.pencolor('brown')
        name.pensize(5)

def step_turtle(): # star
    print(" ")
    pass

def step_turtle_second(): # rectangle with rectangle
    print(" ")
    pass

def main():

    animal = turtle.Turtle()     # turtle init to draw on panel

    super_turtle(animal,100,90)
    super_turtle_exp(animal,150,90)
    super_turtle_exp_ten(animal,100,90)

    step_turtle()
    step_turtle_second()

    turtle.exitonclick()         # exit with [X] on right top corner 
    #error with unknown word/words -> ,,exitonclick,,

main() # all function in one main 

# .pencolor( 'blue' )
# .prensize( 10 )