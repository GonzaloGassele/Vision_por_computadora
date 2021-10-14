import  cv2
import numpy as np
from vidgear.gears import CamGear

options = {"CAP_PROP_BUFFERSIZE": 0,'THREADED_QUEUE_MODE': False}

def active_cam():
    cap=[[0,1,0],[1,1,0],[2,1,0],[3,1,0],[4,1,0],[5,1,0],[6,1,0],[7,1,0]]
    cap[0][1]=CamGear(source='rtsp://contralor:Villegas555@192.168.103.149/cgi-bin/main.cgi',**options).start()# Galpon motos
    cap[1][1]=CamGear(source='rtsp://contralor:Villegas555@100.100.34.179/cgi-bin/main.cgi',**options).start()# Polo lateral
    cap[2][1]=CamGear(source='rtsp://contralor:Villegas555@100.100.34.183/cgi-bin/main.cgi',**options).start()# Atras del polo
    cap[3][1]=CamGear(source='rtsp://contralor:Villegas555@100.100.34.184/cgi-bin/main.cgi',**options).start()# Polo frente
    cap[4][1]=CamGear(source='rtsp://contralor:Villegas555@192.168.103.233/cgi-bin/main.cgi',**options).start()# Estacionamiento emision
    cap[5][1]=CamGear(source='rtsp://contralor:Villegas555@192.168.103.234/cgi-bin/main.cgi',**options).start()# Baños
    cap[6][1]=CamGear(source='rtsp://contralor:Villegas555@192.168.102.105/cgi-bin/main.cgi',**options).start()# Entrada de pacheco
    cap[7][1]=CamGear(source='rtsp://contralor:Villegas555@192.168.102.98/cgi-bin/main.cgi',**options).start()# Entrada de pacheco 2
    cap[0][2]= 'Hay una persona en el galpon de las motos'
    cap[1][2]='Hay una persona en el costado del polo'
    cap[2][2]='Hay una persona atras del polo'
    cap[3][2]='Hay una persona en la entrada del polo'
    cap[4][2]='Hay una persona en el estacionamiento de emision'
    cap[5][2]='Hay una persona en el sector de baños'
    cap[6][2]='Hay una persona en la entrada de pacheco'
    cap[7][2]='Hay una persona en la entrada de pacheco 2'
    
    return cap

def read_camera (cap):
    frames=[[0,3],[1,3],[2,3],[3,3],[4,3],[5,3],[6,3],[7,3]]
    for j ,i ,t in cap: 
        frames[j][0]=i.read()
        frames[j][1]= [t]
    return frames

def stop_cam(cap):
    cap[0][1].stop()
    cap[1][1].stop()
    cap[2][1].stop()
    cap[3][1].stop()
    cap[4][1].stop()
    cap[5][1].stop()
    cap[6][1].stop()
    cap[7][1].stop()

def all_cam(frame):

    frame1= cv2.resize(frame[0][0],(300,300))
    frame2= cv2.resize(frame[1][0],(300,300))
    frame3= cv2.resize(frame[2][0],(300,300))
    frame4= cv2.resize(frame[3][0],(300,300))
    frame5= cv2.resize(frame[4][0],(300,300))
    frame6= cv2.resize(frame[5][0],(300,300))
    frame7= cv2.resize(frame[6][0],(300,300))
    frame8= cv2.resize(frame[7][0],(300,300))

    output_frame1 = np.concatenate((frame1, frame2, frame3, frame4), axis=1)
    output_frame2 = np.concatenate((frame5, frame6, frame7, frame8), axis=1)
    output_final = np.concatenate((output_frame1,output_frame2),axis=0)

    return output_final



