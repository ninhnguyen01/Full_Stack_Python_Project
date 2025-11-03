# Turtle Graphics Hypnotic Pattern
import turtle
turtle.showturtle()
turtle.pendown()
turtle.setheading(90)
turtle.speed(10)

move = 5

for x in range (12):
    for y in range (4):
        turtle.forward(move)
        turtle.left(90)
        turtle.hideturtle()
        move += 5

turtle.exitonclick()

# End