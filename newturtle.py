import turtle
a=turtle.Turtle()
a.speed(0)
for i in range(1000):
    a.forward(4+i*0.4)
    a.right(60+i*0.1)
    a.pencolor("red")
