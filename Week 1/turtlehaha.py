import turtle

def draw_branch(length):
    if length < 10:
        return

    turtle.forward(length)
    turtle.left(30)
    draw_branch(length - 10)
    turtle.right(60)
    draw_branch(length - 10)
    turtle.left(30)
    turtle.backward(length)

# Setup
screen = turtle.Screen()
screen.bgcolor("black")

turtle.speed(0)  # Fastest
turtle.left(90)  # Point up
turtle.penup()
turtle.goto(0, -250)  # Move to bottom center
turtle.pendown()
turtle.color("lime")

# Start drawing
draw_branch(100)

# Keep window open
turtle.done()
