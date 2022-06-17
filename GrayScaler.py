import tkinter as tk
from tkinter import filedialog
import numpy as np
import os

# Open File dialogue
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

from PIL import Image
img = Image.open(file_path)

# Get color palette
colors = img.convert('RGB').getcolors(maxcolors=256) #this converts the mode to RGB

# Sort color palette
def myFunc(e):
    return e[1][0] + e[1][1] + e[1][2]
colors.sort(reverse=False, key=myFunc)

# Swap colors
data = np.array(img)
red, green, blue, alpha = data.T
index = 0
for c in colors:
    color = c[1]
    desired = (red == color[0]) & (green == color[1]) & (blue == color[2])
    val = index*256.0/len(colors)
    data[..., :-1][desired.T] = (val, val, val)
    index += 1

im2 = Image.fromarray(data)
im2.show()

# Rename
name, ext = os.path.splitext(file_path)

# Save
im2.save( name + '_grey' + ext)

# Save palette 
img_palette = Image.new(mode="RGB", size=(len(colors), 1))
index = 0
for c in colors:
    img_palette.putpixel((index, 0), c[1])
    index += 1

img_palette.show()
img_palette.save( name + '_palette' + ext)