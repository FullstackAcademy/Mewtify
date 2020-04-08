#123
#!/usr/bin/python3
import tkinter as tk
from tkinter import *
from tkinter.font import Font
#GUI Dimensions
HEIGHT = 500
WIDTH = 700
root = tk.Tk()
#GUI NAME AND SIZE
root.title("MEWTIFY")
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
root.resizable(False,False)
#GUI HEADER
frame = tk.Frame(root, bg='#80C1FF' , bd=5)
frame.place(relx=0.5, rely=0.05, relwidth=1, relheight=0.2, anchor='n')
label=tk.Label(frame,text = "Welcome to Mewtify!", font=("-weight bold",27),bg='#80C1FF')
label.place(relx=0.3, rely=0, relwidth=.5, relheight=1)
#INPUT 1
label2=tk.Label(root, text="Malicous Software with full path:", anchor='w', font =('fira code', 15))
label2.place(relx=0, rely=0.35, relwidth=0.47, relheight=0.15)
entry2 = tk.Entry(root, font=40)
entry2.place(relx=.5, rely=0.35, relwidth=0.45, relheight=0.09)
#INPUT2
label3=tk.Label(root, text="Name of Mutated Software:", anchor='w', font =('fira code', 15))
label3.place(relx=0, rely=0.5, relwidth=0.45, relheight=0.15)
entry3 = tk.Entry(root, font=40)
entry3.place(relx=.5, rely=0.5, relwidth=0.45, relheight=0.09)
#GRABBING INPUTS
entry2.get()
entry3.get()
def x():
    label4 = tk.Label(root, text="Please give a valid python file with the full path",fg = 'red')
    label4.place(relx=0.5, rely=0.7, relwidth=0.45, relheight=0.05)

#button mashing
button=tk.Button(root, text="MEWTIFY", bg= "purple", font =40,command=x())
button.place(relx=0.3, rely=0.8, relwidth=0.45, relheight=0.15)
r = IntVar()
rbutton=tk.Radiobutton(root, text="option 2", variable=r, value=1).pack(side="right")
rbutton2=tk.Radiobutton(root, text="option 1", variable=r, value=2).pack(side="right")



# label6=tk.Label(root, text="MEWTIFIED! Please check the same folder for the file.",fg = 'green')
# label6.place(relx=0.3, rely=0.6, relwidth=0.45, relheight=0.15)

# label4 = tk.Label(root, text="Please give a valid python file with the full path",fg = 'red')
# label4.place(relx=0.5, rely=0.7, relwidth=0.45, relheight=0.05)

# label5 = tk.Label(root, text="Please give a valid name", fg='red')
# label5.place(relx=0.5, rely=0.6, relwidth=0.45, relheight=0.05)

root.mainloop()

