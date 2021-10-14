import cv2

cap1= cv2.VideoCapture('rtsp://contralor:Villegas555@192.168.102.98/cgi-bin/main.cgi')


while(True):
    ret,frame= cap1.read()
    img= cv2.resize(frame, (0,0), fx= 0.6, fy=0.6)
    cv2.imshow('camera', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
