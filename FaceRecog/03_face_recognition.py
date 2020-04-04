# IMPORTANCE !!!!! this Restrict to jump id cant run !!!!! -> Use database to fix <-
 
import cv2
import numpy as np
import os 
 
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
 
font = cv2.FONT_HERSHEY_SIMPLEX

# Array of user floor and name
user_floor_id = ["None"]
user_name_id = ["None"]

# Confidence time check
confidencetime = 0

# Delay read data
delay = 0
rounddelay = 0

# LineCounter for read data
count = 0
 
# Read userdata from file
with open("user_data.txt","r") as file1:
    while True:
        count += 1
        line = file1.readline()
        x = line.strip()

        # separate id and name,floor
        keyword = '.'
        before_keyword, keyword, after_keyword = x.partition(keyword) 
        
        y = after_keyword
        keyword2 = '_'
        before_keyword2, keyword2, after_keyword2 = y.partition(keyword2)
        
        # store data to variable
        user_id = before_keyword
        user_name = before_keyword2
        user_floor = after_keyword2

        # store name and floor to array
        user_floor_id.append(user_floor)
        user_name_id.append(user_name)

        # checking is working (Delete after debug)
        print(user_floor_id[count])
        print(user_name_id[count])

        if not line: 
            break

# iniciate id counter
id = 0
 
# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height
 
# Define min window size to be recognized as a face
minW = 0.15*cam.get(3)
minH = 0.15*cam.get(4)
 
while True:
 
    ret, img =cam.read()
    img = cv2.flip(img, 1)
 
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 
    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )
 
    for(x,y,w,h) in faces:
 
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,255), 2)
 
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
 
        # Check if confidence is less them 100 ==> "0" is perfect match 
        if (confidence < 100):
            idnum = id
            id = user_name_id[id]
            confidencepercent = "  {0}%".format(round(100 - confidence))
            confidence = "  {0}".format(round(100 - confidence))
            confidence2 = int(confidence)

            if (delay == rounddelay):

                print(confidence) # Check confidence (Delete after debug)

                # Start store user match with data [if confidence more than 55 percent for 10 times]
                if (confidence2 > 35):
                    print("working now!") #Check working 1 time (Delete after debug)
                    confidencetime += 1
                else: 
                    print("not working") #Check not working 1 time (Delete after debug)
                
                delay += 10
        
        else:
            id = "unknown"
            confidencepercent = "  {0}%".format(round(100 - confidence))

        if (confidencetime > 10):
            print("Go to floor ",user_floor_id[idnum]) # Change to send data to elevator
            confidencetime = 0 # Reset confidencetime
        rounddelay += 1

    cv2.imshow('camera',img) 
 
    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
 
# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()