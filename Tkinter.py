from tkinter import *
import turtle

# Function for Red Button - Expanding Spiral
def draw_red_pattern():
    a = turtle.Turtle()
    a.speed(0)
    a.pencolor("red")

    for i in range(100):  # Creates a swirling effect
        a.circle(i * 2, 180)  # Draws a half-circle with increasing radius
        a.right(60)  # Slight rotation to create a spiral effect
        
# Function for Blue Button - Square with Hexagons
def draw_blue_pattern():
    a = turtle.Turtle()
    a.speed(0)
    a.pencolor("blue")

    for i in range(200):  # Creates a swirling effect
        a.circle(i * 1, 180)  # Draws a half-circle with increasing radius
        a.right(60)  # Slight rotation to create a spiral effect
        
# Function for Green Button - Star Pattern
def draw_green_pattern():
    a = turtle.Turtle()
    a.speed(0)
    a.pencolor("green")

    for i in range(75):  # Creates a swirling effect
        a.circle(i * 3, 180)  # Draws a half-circle with increasing radius
        a.right(60)  # Slight rotation to create a spiral effect


# Function for Black Button - Circular Flower
def draw_black_pattern():
    a = turtle.Turtle()
    a.speed(0)
    a.pencolor("black")

    for i in range(400):  # Creates a swirling effect
        a.circle(i * 0.5, 180)
        a.dot(50)# Draws a half-circle with increasing radius
        a.right(60)  # Slight rotation to create a spiral effect
        a.dot(100)
    a.hideturtle()

# Create Tkinter window
parent = Tk()

# Buttons with commands linked to respective functions
redbutton = Button(parent, text="Red", fg="red", command=draw_red_pattern)
redbutton.pack(side=LEFT)

greenbutton = Button(parent, text="Green", fg="green", command=draw_green_pattern)
greenbutton.pack(side=RIGHT)

bluebutton = Button(parent, text="Blue", fg="blue", command=draw_blue_pattern)
bluebutton.pack(side=TOP)

blackbutton = Button(parent, text="Black", fg="black", command=draw_black_pattern)
blackbutton.pack(side=BOTTOM)

parent.mainloop()
