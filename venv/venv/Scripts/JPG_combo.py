#!/usr/bin/python3
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
from tkinter.filedialog import askopenfilename

def fname():
    filename = askopenfilename()
    print (filename)

#GUI Dimensions
HEIGHT = 500
WIDTH = 700

root = tk.Tk()

#GUI NAME AND SIZE
root.title("MEWTIFY")
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='yaj.png')
background_label = tk.Label(root, image=background_image)
background_label.image= background_image
background_label.place(relwidth=1,relheight=1)

root.resizable(False,False)

#GUI HEADER
frame = tk.Frame(root, bg='#80C1FF' , bd=5)
frame.place(relx=0.5, rely=0.05, relwidth=1, relheight=0.2, anchor='n')
label=tk.Label(frame,text = "Welcome to Mewtify!", font=("-weight bold",27),bg='#80C1FF')
label.place(relx=0.3, rely=0, relwidth=.5, relheight=1)

#INPUT 1
label2=tk.Label(root, text="Malicious malware with full path:", anchor='w', font =('fira code', 15))
label2.place(relx=0, rely=0.35, relwidth=0.47, relheight=0.15)
filebutton = tk.Button(root, text="Select" ,font=40,command=fname)
filebutton.place(relx=.5, rely=0.35, relwidth=0.45, relheight=0.09)

#INPUT 2
label3=tk.Label(root, text="Name your payload:", anchor='w', font =('fira code', 15))
label3.place(relx=0, rely=0.5, relwidth=0.45, relheight=0.15)
entry3 = tk.Entry(root, font=40)
entry3.place(relx=.5, rely=0.5, relwidth=0.45, relheight=0.09)


#GRABBING INPUTS/ERRORS
def x():
    error_label2 = tk.Label(root, text="Please give a valid python file with the full path",fg = 'red')
    error_label2.place(relx=0.5, rely=0.7, relwidth=0.45, relheight=0.05)

#button mashing
button=tk.Button(root, text="MEWTIFY", bg= "purple", font =40,command=x)
button.place(relx=0.3, rely=0.8, relwidth=0.45, relheight=0.15)

r = IntVar()

rbutton_frame = tk.Frame(root , width= 50, relief= RIDGE, bd=4)
rbutton_frame.place(relx=0.5, rely=0.26, relwidth=0.45, relheight=0.06)
rbutton1=tk.Radiobutton(rbutton_frame, text="JPG", variable=r, value=1)
rbutton1.pack(anchor=W, side=LEFT, ipadx=10)
rbutton2=tk.Radiobutton(rbutton_frame, text="Python", variable=r, value=2)
rbutton2.pack(anchor=W, side=LEFT, ipadx=10)
rbutton3=tk.Radiobutton(rbutton_frame, text="JAYIFY <-- special", variable=r, value=3)
rbutton3.pack(anchor=W, side=LEFT, ipadx=10)

# label6=tk.Label(root, text="MEWTIFIED! Please check the same folder for the file.",fg = 'green')
# label6.place(relx=0.3, rely=0.6, relwidth=0.45, relheight=0.15)

# label4 = tk.Label(root, text="Please give a valid python file with the full path",fg = 'red')
# label4.place(relx=0.5, rely=0.7, relwidth=0.45, relheight=0.05)

# label5 = tk.Label(root, text="Please give a valid name", fg='red')
# label5.place(relx=0.5, rely=0.6, relwidth=0.45, relheight=0.05)

root.mainloop()

