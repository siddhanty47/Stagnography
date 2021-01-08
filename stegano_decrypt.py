import cv2
import numpy as np
import types
from stegano_encrypt import messageToBinary

def showData(image):
    binary_data = ""
    for values in image:
        for pixel in values:
            r, g, b = messageToBinary(pixel) #convert the red,green and blue values into binary format
            binary_data += r[-1] #extracting data from the least significant bit of red pixel
            binary_data += g[-1] #extracting data from the least significant bit of red pixel
            binary_data += b[-1] #extracting data from the least significant bit of red pixel
    # split by 8-bits
    all_bytes = [ binary_data[i: i+8] for i in range(0, len(binary_data), 8) ]
    # convert from bits to characters
    decoded_data = ""
    for byte in all_bytes:
        decoded_data += chr(int(byte, 2))
        if decoded_data[-5:] == "#####": #check if we have reached the delimeter which is "#####"
            break
    #print(decoded_data)
    return decoded_data[:-5] #remove the delimeter to show the original hidden message



  # Decode the data in the image 
def decode_text(image):
    print("The Steganographed image is as shown below: ")
    #resized_image = cv2.resize(image, (500, 500))  #resize the original image as per your requirement
    #cv2_imshow(resized_image) #display the Steganographed image
    #cv2_imshow(image) #display the Steganographed image  
    text = showData(image)
    return text