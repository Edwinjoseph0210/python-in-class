import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
for x in range(500):
 t.pencolor(colors[x%6])
 t.forward(x)
 t.left(59)
