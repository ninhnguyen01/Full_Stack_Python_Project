# Turtle Graphics: Modularizing Code with Functions

# Reading

import turtle

turtle.fillcolor('blue')
turtle.begin_fill()
for count in range (4):
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()

# This line is needed so program doesn't close upon complete program execution.
turtle.done()
