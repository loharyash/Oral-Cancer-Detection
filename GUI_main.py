from tkinter import *
import tkinter as tk


import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np
import time
import sqlite3
# import tfModel_test as tf_test

root = tk.Tk()

root.title("ORAL CANCER DETECTION")
root.geometry("1600x900")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()


bg = Image.open("MRQ3.jpg")
# bg.resize((1366,500),Image.ANTIALIAS)
# print(w,h)
bg_img = ImageTk.PhotoImage(bg)
bg_lbl = tk.Label(root, image=bg_img)
bg_lbl.place(x=0, y=93, relwidth=1, relheight=1)

######################################################################################################

image_paths = [
    "MRQ1.jpg",
    "MRQ5.jpg",
    "MRQ2.jpg",
    "MRQ3.jpg",
    "MRQ4.jpg",
    # Add more image paths as needed
]


frame = ttk.Frame(root)
frame.place(x=0,y=160)


current_image_index = 0

def update_image():
    global current_image_index
    image_path = image_paths[current_image_index]
    img = Image.open(image_path)
    img = img.resize((1580,600), Image.LANCZOS)  # Adjust the size as needed
    img = ImageTk.PhotoImage(img)
    
    label.config(image=img)
    label.image = img
    current_image_index = (current_image_index + 1) % len(image_paths)
    root.after(2000, update_image)  # Change image every 2000 milliseconds (2 seconds)

label = ttk.Label(frame)
label.pack()

update_image()  # Start the slideshow

def prev_image():
    global current_image_index
    current_image_index = (current_image_index - 1) % len(image_paths)
    update_image()

def next_image():
    global current_image_index
    current_image_index = (current_image_index + 1) % len(image_paths)
    update_image()
##########################################################################################

def scroll_text():
    global text_id, text_x
    
    # Move the text horizontally
    canvas.move(text_id, -3, 0)  # Change the '-1' to adjust the scrolling speed
    
    # If the text moves out of the window, reset its position
    if canvas.bbox(text_id)[2] <= 0:
        text_x = canvas.winfo_width()
        canvas.coords(text_id, text_x, 30)  # Adjust '50' to change the vertical position
    
    # Call the scroll_text function again after 30 milliseconds
    root.after(30, scroll_text)
    
   
#marquee
def shift():
    x1,y1,x2,y2 = canvas.bbox("marquee")
    if(x2<0 or y1<0): #reset the coordinates
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height()//2
        canvas.coords("marquee",x1,y1)
    else:
        canvas.move("marquee", -2, 0)
    canvas.after(1000//fps,shift)

canvas=Canvas(root,bg="black")
canvas.pack()
text_var="ORAL CANCER DETECTION"
text=canvas.create_text(0,-2000,text=text_var,font=('Raleway',25,'bold'),fill='white',tags=("marquee",),anchor='w')
x1,y1,x2,y2 = canvas.bbox("marquee")
width = 1600
height = 100
canvas['width']=width
canvas['height']=height
fps=40    #Change the fps to make the animation faster/slower
shift()   #Function Calling


from tkinter import messagebox as ms


def Login():
    from subprocess import call
    call(["python","login.py"])
def Register():
    from subprocess import call
    call(["python","registration.py"])



d2=tk.Button(root,text="Login",command=Login,width=12,height=1,background="#17202A",foreground="white",font=("times new roman",14,"bold"))
d2.place(x=1200,y=110)


d3=tk.Button(root,text="Register",command=Register,width=12,height=1,background="#17202A",foreground="white",font=("times new roman",14,"bold"))
d3.place(x=1380,y=110)




root.mainloop()
