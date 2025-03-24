from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk, ImageOps
import turtle

# Load and apply grayscale filter to the image
def process_image():
    try:
        image = Image.open("/Users/apple/Downloads/backiee-282952-landscape.jpg")  # Load an image
        grayscale_image = ImageOps.grayscale(image)  # Convert to grayscale
        grayscale_image.show()  # Display processed image
    except Exception as e:
        messagebox.showerror("Error", f"Image Processing Failed: {e}")

def draw_pattern(selected_languages):
    screen = turtle.Screen()
    screen.clear()
    t = turtle.Turtle()
    t.speed(0)

    # Pattern for C
    if "C" in selected_languages:
        t.pencolor("red")
        for i in range(100):
            t.circle(i * 2, 180)
            t.right(45)

    # Pattern for C++
    if "C++" in selected_languages:
        t.pencolor("blue")
        for i in range(36):  
            t.circle(50)
            t.right(10)

    # Pattern for Java
    if "Java" in selected_languages:
        t.pencolor("green")
        for i in range(36):
            t.forward(100)
            t.backward(100)
            t.right(10)

    # If multiple languages are selected, add a flower effect
    if len(selected_languages) > 1:
        t.pencolor("black")
        for i in range(12):
            for _ in range(6):
                t.forward(50)
                t.right(60)
            t.right(30)

def generate_pattern():
    selected_languages = []
    if checkvar1.get():
        selected_languages.append("C")
    if checkvar2.get():
        selected_languages.append("C++")
    if checkvar3.get():
        selected_languages.append("Java")

    if not selected_languages:
        pattern_label.config(text="No selection made.")
        return

    # Process the image before asking confirmation
    process_image()

    # Show confirmation message box
    confirm = messagebox.askyesno("Confirmation", "Are you sure you want to generate this pattern?")
    
    if confirm:
        pattern_label.config(text=f"Pattern for: {', '.join(selected_languages)}")
        draw_pattern(selected_languages)

# Tkinter UI
top = Tk()
top.geometry("300x300")
top.title("Pattern & Image Processing")

checkvar1 = IntVar()
checkvar2 = IntVar()
checkvar3 = IntVar()

chkbtn1 = Checkbutton(top, text="C", variable=checkvar1, onvalue=1, offvalue=0)
chkbtn2 = Checkbutton(top, text="C++", variable=checkvar2, onvalue=1, offvalue=0)
chkbtn3 = Checkbutton(top, text="Java", variable=checkvar3, onvalue=1, offvalue=0)

chkbtn1.pack()
chkbtn2.pack()
chkbtn3.pack()

submit_btn = Button(top, text="Generate Pattern", command=generate_pattern)
submit_btn.pack()

pattern_label = Label(top, text="", font=("Arial", 12))
pattern_label.pack()

top.mainloop()
