import turtle
import math
t=turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("dark red")

t.speed(0)
t.penup()
t.pencolor("yellow")
angle = 0
radius = 2
t.right(90)
t.forward(100)
t.goto(-100, -radius)
t.pendown()

for _ in range(500):
    x = radius * math.cos(math.radians(angle))
    y = radius * math.sin(math.radians(angle)) + radius  # Ensures upward movement
    t.goto(x, y)
    t.pendown()
    angle += 10
    radius += 1

turtle.done()
