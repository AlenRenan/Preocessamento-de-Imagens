from tkinter import *  # Import from GUI api
from tkinter import filedialog as fd # Import api to open file dialog
import cv2.cv2
import numpy as np
from PIL import Image
from PIL.ImageFilter import EMBOSS, FIND_EDGES  # Image Filters
import cv2
from matplotlib import pyplot as plt

"""
histogram logic - Create a histogram from an image
"""


def histogram_logic():
    filename = fd .askopenfilename()
    print(filename)
    img = cv2.imread(filename, 0)
    cv2.imshow("Histogram", img)

    plt.hist(img.ravel(), 256, [0, 256])
    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()


"""
binaryGrey logic - Turn an image into black and white
"""


def binary_logic():
    img = Image.open(fd.askopenfilename())  # Open file dialog and select the image
    imgBinary = img.convert('L')  # Convert the image to 1 bit
    imgBinary.save('gray.jpg')  # Save the Grey image
    imgBinary.show()  # Open the file


"""
filters logic - Add filters at the image
"""


def filters_logic():
    img = Image.open(fd.askopenfilename())  # Open file dialog and select the image
    img1 = img.filter(EMBOSS)  # Applying the blur filter
    img1.save('filter1.jpg')  # Save the blurred image
    img1.show()  # Open the file
    img2 = img.filter(FIND_EDGES)  # Applying the filter
    img2.save('filter2.jpg')  # Save the image
    img2.show()  # Open the file
