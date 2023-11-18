import cv2
import numpy as numpy

path = 'center.jpg' 
image = cv2.imread(path)
grayImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
