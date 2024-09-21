
import pandas as pd
import flask 
import numpy
import cv2
import matplotlib.pyplot    

img = cv2.imread('image.jpg')

# Display the image
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()