import tkinter as tk
from tkinter import *
from tkinter import filedialog, Text
import os
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import matplotlib.image as mpimg
import cv2
import scipy
import numpy as np
from tkinter.font import Font
import csv
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from skimage import io
import pandas as pd
from matplotlib import patches
from tkinter.messagebox import *
import time

def destroy_widget(widget):
    widget.destroy()

image1=''
main = Tk()
dir_path = os.path.dirname(os.path.realpath(__file__))
cwd = os.getcwd()
print(cwd)
os.chdir(dir_path)
main.bold_font = Font(family="Helvetica", size=14, weight="bold")
main.title("Image Encrypt Decrypt")
main.minsize(400, 300)
main.maxsize(400, 300)
main.labelFrame = Label(main, text = "Open File:", font=('Impact', -20), bg='#000', fg='#000')
main.labelFrame.grid(column = 0, row = 2, padx = 20, pady = 20)
main.configure(background='#dfdddd')
main.labelFrame.configure(background='#dfdddd')

Label(main, text = "Enter Encryption Number:").grid(column= 0, row = 4)
Label(main, text = "Enter Decryption Number:").grid(column= 0, row = 6)
num1 = Entry(main)
num1.grid(column= 1, row = 4)
num2 = Entry(main)
num2.grid(column= 1, row = 6)

if(num2 != num1):
    label=Label(main, text = "Key didnt match !! Try Again")
    label.grid(column= 0, row = 5)
    # run clear_label after 2000ms (2s)
    main.after(5000,destroy_widget, label)


def button_pressed():
    # put text
    label=Label(main, text = "Encryption Done!")
    label.grid(column= 0, row = 5)
    # run clear_label after 2000ms (2s)
    main.after(5000,destroy_widget, label)

def button_pressed1():
    # put text
    label=Label(main, text = "Decryption Done!")
    label.grid(column= 0, row = 7)
    # run clear_label after 2000ms (2s)
    main.after(5000,destroy_widget, label)

def button_pressed2():
    label=Label(main, text = "Loading...")
    label.grid(column= 0, row = 8)
    main.after(32000,destroy_widget, label)


def fileDialog():
    main.filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =
    (("jpeg files","*.jpg"),("all files","*.*")) )
    #main.label = ttk.Label(main.labelFrame, text = "")

    #main.label.configure(text = main.filename)
    img = Image.open(main.filename)
    file="original_image.csv"
    with open(file, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([main.filename])
    img2 = io.imread(main.filename, plugin='matplotlib')


def encryption():

    image1=""
    file="original_image.csv"
    with open(file, 'r',) as file:
        reader = csv.reader(file, delimiter = '\t')
        for row in reader:
            image1=row[0]
            break
    image = mpimg.imread(image1)
    #os.remove("imagewrite.csv");
    # reshaping the array from 3D
    # matrice to 2D matrice.
    from PIL import Image
    im = Image.open(image1)
    im.save('original_image.png')
    image = mpimg.imread('original_image.png')
    imageshape=np.asarray(image.shape)
    np.savetxt("shape1.csv", imageshape, delimiter=",",fmt='%.3e')
    x = image.reshape(image.shape[0], -1)
    Ans = int(num1.get())
    x=x*Ans
    # encrypted_show()

    np.savetxt("open_for_decryption.csv", x)
    # File to be opened
    
    # saving reshaped array to file.

    command = button_pressed()


def decryption():
    filename = filedialog.askopenfilename()
    loaded_arr = np.loadtxt(filename).astype(float)
    shape1 = np.loadtxt("shape1.csv").astype(int)
    Ans = int(num2.get())
    loaded_arr=loaded_arr/Ans
    load_original_arr = loaded_arr.reshape(loaded_arr.shape[0], loaded_arr.shape[1] // shape1[2], shape1[2])
    # This loadedArr is a 2D array, therefore
    # we need to convert it to the original
    # array shape.reshaping to get original
    # matrice with original shape.
    dpi = 80
    image2=load_original_arr
    im_data = load_original_arr
    height, width, nbands = im_data.shape
    figsize = width / float(dpi), height / float(dpi)
    fig = plt.figure(figsize=figsize)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    ax.imshow(image2, interpolation='nearest')
    ax.set(xlim=[-0.5, width - 0.5], ylim=[height - 0.5, -0.5], aspect=1)
    fig.savefig("decrypted_image.png", dpi=dpi,transparent=True)
    os.remove("open_for_decryption.csv")
    os.remove("shape1.csv")
    os.remove("original_image.csv")
    command = button_pressed1()


def original():
    image1=""
    file="original_image.csv"
    with open(file, 'r',) as file:
        reader = csv.reader(file, delimiter = '\t')
        for row in reader:
            image1=row[0]
            break
    image = cv2.imread(image1)
    image = mpimg.imread(image1)
    dpi = 80
    im_data = plt.imread(image1)
    height, width, nbands = im_data.shape
    figsize = width / float(dpi), height / float(dpi)
    fig = plt.figure(figsize=figsize)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    ax.imshow(image, interpolation='nearest')
    ax.set(xlim=[-0.5, width - 0.5], ylim=[height - 0.5, -0.5], aspect=1)
    fig.show()

def button():
        main.button = Button(main, text = "Browse for image",font=('Impact', -10),command = fileDialog)
        main.button.grid(column=1, row = 2)


def showoriginal():
        main.showoriginal = Button(main, text = "Original",command = original)
        main.showoriginal.configure(background='#e28743')
        main.showoriginal.grid(column= 0, row = 3)

def encrypt():
        #command = lambda:[encryption(),button_pressed2()]
        main.showoriginal = Button(main, text = "Encrypt",command = lambda:[encryption()])
        main.showoriginal.configure(background='#e28743')
        main.showoriginal.grid(column= 2, row = 4)

def decrypt():
        main.showoriginal = Button(main, text = "Decrypt",command = decryption)
        main.showoriginal.configure(background='#e28743')
        main.showoriginal.grid(column= 2, row = 6)


button()
showoriginal()
encrypt()
decrypt()

matplotlib.use('TkAgg')


mainloop()
