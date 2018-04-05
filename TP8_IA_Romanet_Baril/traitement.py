# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 16:17:00 2018

@author: PaulHochon_Laptop
"""
import cv2
import numpy as np

# RGB(242,139,174)~~
boundary = np.array(([180,100,130],[256,180,220]))
 
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture('videoplayback.mp4')
 
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
 
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
    
    
    
    # Display the original frame
    cv2.imshow('Original Frame',frame)
    
    # Display the frame with edges only (Not very convincing)
    cv2.imshow('Modified Frame (Laplacian)',cv2.Laplacian(frame,cv2.CV_64F,7))
    
    # Sobel
    #frame = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize = 3)+cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize = 3) 
    cv2.imshow('Modified Frame (Sobel)', cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize = 3)+cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize = 3))
    
    # Color
    mask = cv2.inRange(frame, boundary[0], boundary[1])
    output = cv2.bitwise_and(frame, frame, mask = mask)
    cv2.imshow('Modified Frame (Color)',output)
    
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
 
  # Break the loop
  else: 
    break
 
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()