# This turtle program draws 3 circles on a grid.

import turtle
turtle.showturtle()
turtle.heading()

turtle.forward(250)
turtle.setheading(180)
turtle.forward(500)
turtle.home()
turtle.setheading(90)
turtle.forward(250)
turtle.setheading(270)
turtle.forward(500)

turtle.penup()
turtle.goto(-60,0)
turtle.pendown()
turtle.pencolor('red')
turtle.circle(60)

turtle.penup()
turtle.goto(-120,0)
turtle.pendown()
turtle.pencolor('green')
turtle.circle(120)

turtle.penup()
turtle.goto(-180,0)
turtle.pendown()
turtle.pencolor('blue')
turtle.circle(180)
turtle.hideturtle()

turtle.done()