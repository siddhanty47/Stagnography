from tkinter import *
import stegano_encrypt as se
import stegano_decrypt as sd
import cv2
import numpy as np
import RSA

# loading Python Imaging Library 
from PIL import ImageTk, Image 

# To get the dialog box to open when required 
from tkinter import filedialog 
# Create a windoe 
def open_img_encryption(): 
	# Select the Imagename from a folder 
	x = openfilename() 
	# opens the image 
	global img
	img = Image.open(x) 
	img1 = img
	# resize the image and apply a high-quality down sampling filter 
	img1 = img1.resize((200, 200), Image.ANTIALIAS) 

	# PhotoImage class is used to add image to widgets, icons etc 
	img1 = ImageTk.PhotoImage(img1) 

	# create a label 
	panel.configure(image = img1) 
	
	# set the image as img 
	panel.image = img1 
	panel.pack()
	if(global_text != ""):
		btn4.pack(side='bottom')

def open_img_decryption(): 
	# Select the Imagename from a folder 
	x = openfilename() 
	# opens the image 
	global img
	img = Image.open(x) 
	img1 = img
	# resize the image and apply a high-quality down sampling filter 
	img1 = img1.resize((200, 200), Image.ANTIALIAS) 

	# PhotoImage class is used to add image to widgets, icons etc 
	img1 = ImageTk.PhotoImage(img1) 

	# create a label 
	panel.configure(image = img1) 
	
	# set the image as img 
	panel.image = img1 
	panel.pack()
	btn5.pack(side='bottom')

#Perform steganography here and save the resulting image
def encrypt_and_save():
	image=cv2.imread(file_n)
	cipher=RSA.RSA_encrypt(global_text)
	se.encode_text(image,cipher)
	print("Encypt and save to a path here")
	pass

def decrypt_and_save():
	image=cv2.imread('encrypted_image.png')

	text=sd.decode_text(image)
	print("Decrypt and return the text file here")
	print(RSA.RSA_decrypt(text))
	pass

def openfilename(): 

	# open file dialog box to select image 
	# The dialogue box has a title "Open" 
	filename = filedialog.askopenfilename(title ='Select File') 
	global file_n
	file_n=filename
	return filename 

def open_file():
	x = openfilename()
	file = open(x)
	text = file.read()
	global global_text
	global_text = text
	#ENCRYPT THE TEXT HERE

def selection():
	val = str(var.get())
	if(val == "encrypt"):
		btn5.pack_forget()
		btn2.pack_forget()
		panel.pack_forget()
		btn3.pack(side='top')
		btn1.pack(side='top')
	else:
		btn1.pack_forget()
		btn3.pack_forget()
		panel.pack_forget()
		btn4.pack_forget()
		btn2.pack()

root = Tk()
global_text = "Nothing"

mode = 'RGB'
size=(640, 480)
color = (73,109,137)
img = Image.new(mode, size, color)
# Set Title as Image Loader 
root.title("Image Loader") 

# Set the resolution of window 
root.geometry("650x400+300+150") 

# Allow Window to be resizable 
root.resizable(width = True, height = True)

var = StringVar()
frm = Frame(root, bd=10, pady = 15)
frm.pack()
r1 = Radiobutton(frm, text="Encrypt", bd=2, width=20)
r1.config(indicatoron=0, variable=var, value="encrypt", command=selection)
r1.pack(side='right')
r2 = Radiobutton(frm, text="Decrypt", bd=2, width=20)
r2.config(indicatoron=0, variable=var, value="decrypt", command=selection)
r2.pack(side='right')

btn1 = Button(root, text='open image', command=open_img_encryption, pady=5)
btn2 = Button(root, text='upload image', command=open_img_decryption, pady=5)
btn3 = Button(root, text='upload text file', command=open_file, pady=5)
btn4 = Button(root, text='encrypt text into image', command=encrypt_and_save)
btn5 = Button(root, text='decrypt text from image', command=decrypt_and_save)
panel = Label(root)

# Create a button and place it into the window using grid layout 
#btn = Button(root, text ='open image', command=open_img).grid(row = 1, columnspan = 10)
root.mainloop()