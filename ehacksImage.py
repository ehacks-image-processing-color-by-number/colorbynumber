import tkinter as tk
from PIL import ImageGrab
import turtle
from turtle import *
import random
from pathlib import Path
import os
import time

screen = turtle.Screen()
root = tk.Tk()
canvas = tk.Canvas(root, width=525, height=525)
canvas.pack()
t = turtle.RawTurtle(canvas)

t.screen.colormode(255)
t.hideturtle()

bgcolor('white')
t.speed("fastest")


"""
takes a png screenshot of a tkinter window, and saves it on in cwd
"""
print('...dumping gui window to png')
root.geometry("525x525+0+0")
x0 = root.winfo_rootx()
y0 = root.winfo_rooty()
x1 = x0 + root.winfo_width()
y1 = y0 + root.winfo_height()

#if the file is there, delete it
file_path = Path('eHacksRandImage.png')

    # Check if the file exists before attempting to delete
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"File '{file_path}' has been deleted.")
else:
    print(f"File '{file_path}' does not exist.")

def take_ss():
    screenshot = ImageGrab.grab().crop((x0-50, y0-50, x1+150, y1+150))
    screenshot.save("eHacksRandImage.png")

def rand():
    rand_num = random.randrange(0,255)
    return rand_num

def rand_signed():
    rand_num = random.randrange(-300,300)
    return rand_num
def draw_regular_polygon(length,numSides,color_R, color_G, color_B):
    t.color(color_R, color_G, color_B)
    t.fillcolor(color_R, color_G, color_B)
    t.pendown()
    t.begin_fill()
    for i in range(numSides):
        t.forward(length)
        t.left(360/numSides)
    t.penup()
    t.end_fill()

def draw_circle(radius,color_R, color_G, color_B):
    t.color(color_R, color_G, color_B)
    t.fillcolor(color_R, color_G, color_B)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.penup()
    t.end_fill()

for i in range(100):
    t.penup()
    t.goto(rand_signed(), rand_signed())
    t.left(rand())
    if rand() % 6 == 0:
        draw_circle(rand() % 50 + 50, rand() % 255, rand() % 255, rand() % 255 )
    else:
        draw_regular_polygon(rand() % 60 + 50, rand() % 4 + 3, rand() % 255, rand() % 255, rand() % 255)

time.sleep(1)
take_ss()
root.mainloop()