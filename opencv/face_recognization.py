#!/usr/bin/python

# face_detect.py

# Face Detection using OpenCV. Based on sample code from:
# http://python.pastebin.com/m76db1d6b

# Usage: python face_detect.py <image_file>

import sys, os
from cv2.cv import *
from cv2 import *
#from cv2.highgui import *

def detectObjects(image):
  """Converts an image to grayscale and prints the locations of any 
     faces found"""
  grayscale = CreateImage((image.width, image.height), 8, 1)
  CvtColor(image, grayscale, CV_BGR2GRAY)

  storage = CreateMemStorage(0)
  #ClearMemStorage(storage)
  EqualizeHist(grayscale, grayscale)
  cascade = Load( '/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml')
  faces = HaarDetectObjects(grayscale, cascade, storage, 1.2, 2, CV_HAAR_DO_CANNY_PRUNING, (50,50))

  if faces:
    for f in faces:
        x, y , width, height = f[0]
        print("[(%d,%d) -> (%d,%d)]" % (x, y, x+width, y+height))

def main():
  image = LoadImage(sys.argv[1]);
  detectObjects(image)

if __name__ == "__main__":
  main()
