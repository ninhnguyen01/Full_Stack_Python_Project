#  Turtle Graphics: Using Loops to Draw Designs

# This program draws a design using repeated circles.
import turtle
turtle.showturtle()
# Named constants
NUM_CIRCLES = 36
RADIUS = 100
ANGLE = 10
ANIMATION_SPEED = 0
# Set the animation Speed.
turtle.speed(ANIMATION_SPEED)
# Draw 36 circles, with the turtle tilted by 10 degrees after
# each circle is drawn.
for x in range (NUM_CIRCLES):
    turtle.circle(RADIUS)
    turtle.left(ANGLE)

turtle.done()