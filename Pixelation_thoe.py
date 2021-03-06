'''
Allen Thoe: Change pixels in an image.
'''
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
import os.path
import numpy as np  # "as" lets us use standard abbreviations
   
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
#filename = os.path.join(directory, 'chrysler-top-bw1.jpg')
filename = os.path.join(directory, 'basketball.JPG')
# Read the image data into an array
img = plt.imread(filename)
fig, ax = plt.subplots(1, 1)

height = len(img)
width = len(img[0])

print ('width= ',width)
print ('height= ',height)


def changeBG(im):
    
    for row in range(height):
        for col in range(width):
            if (sum(img[row][col]))%5 == 0:
                im[row][col] = [row, col, 125,]  
    '''
    for row in range(height):
        for col in range(width):
            if sum(img[row][col])>500:
                img[row][col] = [100, 100, 255,]  
    '''
changeBG(img)
        
# Show the image data in a subplot
ax.imshow(img, interpolation='none')

# Show the figure on the screen
fig.show()

        

print(type(img))