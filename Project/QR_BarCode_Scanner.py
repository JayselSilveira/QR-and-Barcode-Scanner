# QR and Bar Code Scanner

import cv2 # since we're dealing with images
import numpy as np # since we're working with arrays
from pyzbar.pyzbar import decode # to detect and localize barcodes and QR code

cap = cv2.VideoCapture(0) # for webcam, 0 is the id
cap.set(3, 640) # defines width, first value is width id
cap.set(4, 480) # defines height, first value is height id

while True:
    success, img = cap.read()

    for code in decode(img): # for detection, location and decoding the message of QR and barcode.
        myData = code.data.decode('utf-8') # from all the information, we select only the data part
        
        print(myData) # prints the decoded data

        pts = np.array([code.polygon],np.int32) # making a polygon instead of a rectangle, so even if the QR code is rotated it can detect properly and converting the polygon to an array
        
        pts = pts.reshape((-1, 1, 2)) # reshaping the array and sending it to polygon function

        cv2.polylines(img, [pts], True, (255, 0, 255), 5) # True since we want a closed figure, (255,0,255) is magenta i.e. the color we have specified, 5 is the thickness
        
        pts2 = code.rect # since we don't want the data to rotate
        
        cv2.putText(img, myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2) # 0.9 is the scale, 2 is the thickness
    
    cv2.imshow('Result', img)
    cv2.waitKey(1)