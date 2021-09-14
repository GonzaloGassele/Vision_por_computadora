
#Librerias
import time

import cv2
import numpy as np
import torch
from vidgear.gears import CamGear

model= torch.hub.load('ultralytics/yolov5', 'yolov5l6')# modelo

#configuración del modelo
model.conf = 0.66#confidence threshold (0-1)
model.classes= [0]# detección de personas
options = {"CAP_PROP_BUFFERSIZE": 0}
cap= CamGear(source='rtsp://contralor:Villegas555@100.100.34.184/cgi-bin/main.cgi',logging=True,**options).start()


while(True):
    frame=cap.read()
    img= cv2.resize(frame ,(640,640))
    result= model(img)
    result.render()
    labels = result.xyxyn[0][:, -1].numpy()
    if (labels.all()==0):
        print('pp')
    cv2.imshow('camera', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.stop()
        break
