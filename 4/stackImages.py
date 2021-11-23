# Importing necessary modules.
import cv2
import numpy as np


# Defining a function to stack input images.
def stackImages(scale,imgArray):
    # Using 'len()' to return the number of items in the 'imgArray' object which is used to store 1-D and 2-D images as an array.
    rows = len(imgArray)
    cols = len(imgArray[0])
    # Returning the number of rows.
    print(rows)
    # Returning the number of columns.
    print(cols)
    # Returning the image array in literal format.
    print(imgArray)
    # Checking if we have a multilayer image.
    # The 'isinstance()' function returns true or false.
    # It takes the the columns and the list as an argument.
    rowsAvailable = isinstance(imgArray[0], list)

    # Storing the width and height of the image array.
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    # Returning the width and height of the image array.
    print (width)
    print (height)
    # If 'rowsAvailable' evaluates to True:
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows

        # Horizontally stacking the image.
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        # Vertically stacking the image.
        ver = np.vstack(hor)

    # If 'rowsAvailable' evaluates to False:
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)

        # Horizontally stacking the image.
        hor = np.hstack(imgArray)
        # Vertically stacking the image.
        ver = hor
    return ver