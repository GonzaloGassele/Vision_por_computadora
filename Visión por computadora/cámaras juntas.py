
from vidgear.gears import CamGear
import cv2
import numpy as np


stream1 = CamGear(source='rtsp://contralor:Villegas555@100.100.34.179/cgi-bin/main.cgi').start() 
stream2 = CamGear(source='rtsp://contralor:Villegas555@100.100.34.183/cgi-bin/main.cgi').start()
stream3 = CamGear(source='rtsp://contralor:Villegas555@100.100.34.184/cgi-bin/main.cgi').start()
stream4 = CamGear(source='rtsp://contralor:Villegas555@192.168.103.149/cgi-bin/main.cgi').start()
stream5 = CamGear(source='rtsp://contralor:Villegas555@192.168.103.233/cgi-bin/main.cgi').start()
stream6 = CamGear(source='rtsp://contralor:Villegas555@192.168.103.234/cgi-bin/main.cgi').start()
stream7 = CamGear(source='rtsp://contralor:Villegas555@192.168.102.105/cgi-bin/main.cgi').start()
stream8 = CamGear(source='rtsp://contralor:Villegas555@192.168.102.98/cgi-bin/main.cgi').start()


while True:

    frame1 = stream1.read()
    frame2= stream2.read()
    frame3= stream3.read()
    frame4= stream4.read()
    frame5= stream5.read()
    frame6= stream6.read()
    frame7= stream7.read()
    frame8= stream8.read()
    frame1= cv2.resize(frame1,(300,300))
    frame2= cv2.resize(frame2,(300,300))
    frame3= cv2.resize(frame3,(300,300))
    frame4= cv2.resize(frame4,(300,300))
    frame5= cv2.resize(frame5,(300,300))
    frame6= cv2.resize(frame6,(300,300))
    frame7= cv2.resize(frame7,(300,300))
    frame8= cv2.resize(frame8,(300,300))

    output_frame1 = np.concatenate((frame1, frame2, frame3, frame4), axis=1)
    output_frame2 = np.concatenate((frame5, frame6, frame7, frame8), axis=1)
    output_final = np.concatenate((output_frame1,output_frame2),axis=0)

    cv2.imshow("Output", output_final)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv2.destroyAllWindows()

stream1.stop()
stream2.stop()
stream3.stop()
stream4.stop()
stream5.stop()
stream6.stop()
stream7.stop()
stream8.stop()



