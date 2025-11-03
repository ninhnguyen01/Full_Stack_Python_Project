# This turtle program draws a 2 color M. 

import turtle
turtle.showturtle()

turtle.penup()
turtle.isdown()
turtle.goto(100,0)
turtle.pendown()
turtle.setheading(45)
turtle.pencolor('blue')
turtle.goto(150,50)
turtle.setheading(120)
turtle.goto(50,150)
turtle.goto(0,120)
turtle.pencolor('red')
turtle.goto(-50,150)
turtle.goto(-150,50)
turtle.goto(-100,0)

turtle.hideturtle()
turtle.done()
