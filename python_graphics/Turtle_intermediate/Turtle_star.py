# Turtle Graphics: Star Pattern
import turtle
turtle.showturtle()
turtle.penup()
turtle.goto(250,-100)
turtle.pendown()
turtle.speed(5)

for x in range (8):
        turtle.goto(-250,-100)
        turtle.goto(100,250)
        turtle.goto(100,-250)
        turtle.goto(-250,100)
        turtle.goto(250,100)
        turtle.goto(-100,-250)
        turtle.goto(-100,250)
        turtle.goto(250,-100)
        turtle.penup()
        turtle.hideturtle()

turtle.exitonclick()

# End