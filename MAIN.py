from imutils import build_montages
from datetime import datetime
import numpy as np
import imagezmq.imagezmq.imagezmq as imagezmq
import imutils
import csv
import socket
import sys
import cv2

imageHub = imagezmq.ImageHub()
frameDict = {}
lastActive = {}
lastActiveCheck = datetime.now()
frame_number = 0
plate_name = ''
   while True:
    ret, frame = cap.read()
    frame_number += 1
    if ret:
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = tfnet.return_predict(img)
        
        for (i, result) in enumerate(results):
            x = result['topleft']['x']
            w = result['bottomright']['x']-result['topleft']['x']
            y = result['topleft']['y']
            h = result['bottomright']['y']-result['topleft']['y']
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            
            #capture roi from the image to process
            roi_color = frame[y:y + h, x:x + w]
            if roi_color.any():
                resize_frame = cv2.resize(roi_color,(800,200))
                results2 = tfnet1.return_predict(resize_frame)
                for (j, result1) in enumerate(results2):
                    x1 = result1['topleft']['x']
                    w1 = result1['bottomright']['x']-result1['topleft']['x']
                    y1 = result1['topleft']['y']
                    h1 = result1['bottomright']['y']-result1['topleft']['y']
                    cv2.rectangle(resize_frame,(x1,y1),(x1+w1,y1+h1),(0,255,0),2)
                    label_position1 = (x1 + int(w1/2)), abs(y1 - 10)
                    cv2.putText(resize_frame, result1['label'], label_position1 , cv2.FONT_HERSHEY_SIMPLEX,1, (255,255,255), 3)
                cv2.imshow("License Plate",resize_frame)
            
            label_position = (x + int(w/2)), abs(y - 10)
            cv2.putText(frame, result['label'], label_position , cv2.FONT_HERSHEY_SIMPLEX,1, (255,255,255), 3)
        cv2.imshow("Objet Detection YOLO", frame)
        
        if cv2.waitKey(1) == 32:#32 for space
            print("[INFO] Plate found. Saving locally.")
            img_name = str(w) + str(h) + '_plates.jpg'
            cv2.imwrite(img_name, resize_frame)
            file_name = './'+ img_name
            img1 = cv2.imread(file_name)
            img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
            results3 = tfnet1.return_predict(img1)
            img1 = cv2.cvtColor(img1, cv2.COLOR_RGB2BGR)
            for (k, result2) in enumerate(results3):
                x2 = result2['topleft']['x']
                w2 = result2['bottomright']['x']-result['topleft']['x']
                y2 = result2['topleft']['y']
                h2 = result2['bottomright']['y']-result['topleft']['y']
                cv2.rectangle(img,(x2,y2),(x2+w2,y2+h2),(0,255,0),2)
                plate_name += result2['label']
            
            print(plate_name)
            cv2.imshow("Recognized License Plate",resize_frame)
            with open('employee_file2.csv', mode='a', newline='') as csv_file:
                fieldnames = ['License Plates']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                writer.writerow({'License Plates': str(plate_name)})
            print("[INFO] Plate Saved locally.")
            search_plate = plate_name
            plate_name = ''
#         if frame_number == 240:
#             break
        if cv2.waitKey(1) == 99:
            print(search_plate)
            with open('employee_file2.csv') as f:
                reader = csv.reader(f) 
                for row in reader:
                    if search_plate in row[0]:
                        break
                    else:
                        print("Plate not found")
            print("Plate found in file")
            print("[INFO]Connecting to Pi...")
        if cv2.waitKey(1) == 13: #13 is the Enter Key
            break
        
print("[INFO] Plate found. Saving locally.")            
cv2.imwrite(str(w) + str(h) + '_plates.jpg', roi_color)
cap.release()
cv2.destroyAllWindows()
