
#Librerias
import cv2
import torch
import numpy as np
import time
from funtions import active_cam, read_camera, stop_cam, all_cam
from PIL import Image


model= torch.hub.load('ultralytics/yolov5', 'yolov5l6')# modelo

#configuración del modelo
model.conf = 0.66#confidence threshold (0-1)
model.classes= [0]# detección de personas
cap=active_cam()
        
while(True):
    frame=read_camera(cap)
    for i in frame:
        img= cv2.resize(i[0] ,(640,640))
        texto= i[1]
        result= model(img)
        result.render()
        labels = result.xyxyn[0][:, -1].numpy()
        cameras= all_cam(frame)
        if (labels.all()==0):
            print(texto)
        #cv2.imshow('camera', cameras)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
     #   stop_cam(cap)
      #  break