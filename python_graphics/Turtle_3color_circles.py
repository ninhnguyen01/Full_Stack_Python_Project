# This program draws a pattern of 3 color circles.

import turtle
turtle.setup(600,600)
turtle.showturtle()
turtle.penup()
turtle.speed(0)

def main():
    # top
    circle(-250,250,50,'red')
    circle(-150,250,50,'green')
    circle(-50,250,50,'blue')

    circle(50,250,50,'red')
    circle(150,250,50,'green')
    circle(250,250,50,'blue') 
           
    # top mid
    circle(-250,150,50,'red')
    circle(-150,150,50,'green')
    circle(-50,150,50,'blue')

    circle(50,150,50,'red')
    circle(150,150,50,'green')
    circle(250,150,50,'blue')

    # center top
    circle(-250,50,50,'red')
    circle(-150,50,50,'green')
    circle(-50,50,50,'blue')

    circle(50,50,50,'red')
    circle(150,50,50,'green')
    circle(250,50,50,'blue') 
    
    # center bottom

    circle(-250,-50,50,'red')
    circle(-150,-50,50,'green')
    circle(-50,-50,50,'blue')

    circle(50,-50,50,'red')
    circle(150,-50,50,'green')
    circle(250,-50,50,'blue')
    
    # mid bottom

    circle(-250,-150,50,'red')
    circle(-150,-150,50,'green')
    circle(-50,-150,50,'blue')

    circle(50,-150,50,'red')
    circle(150,-150,50,'green')
    circle(250,-150,50,'blue')
    
    # bottom
    circle(-250,-250,50,'red')
    circle(-150,-250,50,'green')
    circle(-50,-250,50,'blue')

    circle(50,-250,50,'red')
    circle(150,-250,50,'green')
    circle(250,-250,50,'blue')

def circle (x,y,radius,color):
    turtle.penup()
    turtle.goto(x,y - radius)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()  
    turtle.hideturtle()

main()

turtle.done()

# End