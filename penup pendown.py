import turtle

# Initialize turtle
t = turtle.Turtle()

# Move forward and draw
t.fd(100)
t.rt(90)

# Move without drawing
t.penup()
t.fd(100)
t.rt(90)
t.pendown()

# Draw again
t.fd(100)
t.rt(90)

# Move without drawing
t.penup()
t.fd(100)
t.pendown()

t.penup()
t.fd(100)
t.rt(80)
t.pendown()
t.forward(50)
# Finish
turtle.done()
