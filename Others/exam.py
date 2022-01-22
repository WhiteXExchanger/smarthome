import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
root=Tk()

"""root = tk.Tk()
canvas_image = tk.PhotoImage("house.jpg")
#Resizing
#canvas_image = canvas_image.subsample(2, 2) #See below for more:
                                            #Shrinks the image by a factor of 2 effectively"""
"""
from tkinter import *

#insert the resize function here
def resizeImage(img, newWidth, newHeight):
    oldWidth = img.width()
    oldHeight = img.height()
    newPhotoImage = PhotoImage(width=newWidth, height=newHeight)
    for x in range(newWidth):
        for y in range(newHeight):
            xOld = int(x*oldWidth/newWidth)
            yOld = int(y*oldHeight/newHeight)
            rgb = '#%02x%02x%02x' % img.get(xOld, yOld)
            newPhotoImage.put(rgb, (x, y))
    return newPhotoImage

root = Tk()

myCanvas = Canvas(root, width=300, height=300)
myCanvas.pack()

puppyImage = PhotoImage(file="house.jpg")  # a 200px x 200px image
puppyImage = resizeImage(puppyImage, 150, 150)  # resized to 150px x 150px

myCanvas.create_image(50, 50, anchor=NW, image=puppyImage)
myCanvas.create_text(0, 0, anchor=NW, text="original 200x200\nnow150x150")

root.mainloop()


resizeImage(canvas_image, 100, 100)

button = tk.Button(root,image = canvas_image, anchor = "nw", height=100,width=100)
button.pack()
root.mainloop()"""

image = Image.open('house.jpg')
# The (450, 350) is (height, width)
image = image.resize((450, 350), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(image)
my_img = Label(root,image = my_img)
my_img.pack()

root.mainloop()