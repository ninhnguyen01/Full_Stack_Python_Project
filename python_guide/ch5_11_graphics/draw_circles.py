# draw circles

import turtle

def main():
    turtle.hideturtle()
    circle(0,0,100,'red')
    circle(-150,-75,50,'blue')
    circle(-200,150,75,'green')

def circle (x,y,radius,color):
    turtle.penup()
    turtle.goto(x,y - radius)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()  

# Call the main function.
if __name__ == '__main__':
    main()

# This line is needed so program doesn't close upon complete program execution.
turtle.done()