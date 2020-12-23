import cv2
import os
import sys
import shutil
import socket
from flask_opencv_streamer.streamer import Streamer
streamer=Streamer(8080,False)
port_getcommand = 9999
port_filesend = 7777
ss = socket.socket()
print('Data_Gathering initiating')
print('[+] Server socket is created.')
receiveno = 0
ss.bind(('', port_getcommand))
print('[+] Socket is binded to {}'.format(port_getcommand))
minW=100
minH=100

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
font = cv2.FONT_HERSHEY_SIMPLEX
while True: #socket listen loop start
    ss.listen(3)
    receiveno=receiveno+1
    print('[+] Waiting for connection no.{}'.format(receiveno))
    con, addr = ss.accept()
    print('[+] Got connection from {}'.format(addr[0]))
    data = con.recv(1024)
    face_id=int(str(data,'utf8'))
    print("\n [INFO] Initializing face capture. Look the camera and wait ...")
    count = 0
    con.close()
    
    cam = cv2.VideoCapture(0) #cam initialize
    cam.set(3, 640) # set video width
    cam.set(4, 480) # set video height
    while(True): #capture start
        ret, img = cam.read()
        img = cv2.flip(img, -1) # flip video image vertically
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, scaleFactor = 1.3, minNeighbors = 5, minSize = (int(minW), int(minH)))

        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
            count += 1
            # Save the captured image into the datasets folder
            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
            cv2.putText(img, str(count)+" of "+ str(30), (x+5,y+h-5), font, 1, (255,255,0), 1)  
        streamer.update_frame(img)
        if not streamer.is_streaming:
            streamer.start_streaming()
     
        k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
        elif count >= 30: # Take 30 face sample and stop video
             img=cv2.imread("done.jpg",1)
             cv2.imshow('image', img)
             streamer.update_frame(img)
             break;
    # Do a bit of cleanup
    print("\n [+]Shutting down Cam")
    cam.release()
    cv2.destroyAllWindows()

    if (k!=27):
        shutil.make_archive('./dataset','zip','./dataset')
        print("[+] Zip made")
        shutil.rmtree('./dataset')
        os.mkdir('./dataset')
        print("[+] Pictures deleted")
        s = socket.socket()
        s.connect(("192.168.0.28",port_filesend))
        if(os.path.exists("dataset.zip")):
            f = open ("dataset.zip", "rb")
            l = f.read(1024)
            while (l):
                s.send(l)
                l = f.read(1024)
        else:
            print("zip file doesn't exist")
        s.close()
        print("[+] Zip send!")
        os.remove('./dataset.zip')
ss.close()