# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 15:49:44 2018

@author: an
"""

#import cv2 
import numpy as np

cap = cv2.VideoCapture('video.mkv')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()