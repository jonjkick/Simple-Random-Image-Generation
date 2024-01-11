# import libraries
import numpy as np
import random
import cv2

# I want to create a purely random image

# create random matrix
# using https://www.geeksforgeeks.org/how-to-create-a-matrix-of-random-integers-in-python/ 
matrix = np.random.randint(256, size=(720,720,3))


# turn matrix into image
# using https://stackoverflow.com/questions/47242918/how-to-create-an-image-from-a-matrix-using-opencv-python 
array = np.array(matrix, dtype=np.uint8)
cv2.imshow('i', array)
cv2.waitKey(0)
cv2.destroyWindow('i')