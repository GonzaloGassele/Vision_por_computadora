
#Librerias
import cv2

import torch
from datetime import datetime
import time
import funtions as f
from Alert import SaveImageModel2 #, send_msj2,send_msj3


def detect():


    model= torch.hub.load('ultralytics/yolov5', 'yolov5l6')# modelo

#configuración del modelo
    model.conf = 0.55#confidence threshold (0-1)
    model.classes= [0]# detección de personas

    cap=f.active_cam()


    while(True):
        frame=f.read_camera(cap)
        if None is frame:
            frame=f.read_camera(cap)
        else:
            for i in frame:
                img= cv2.resize(i[0] ,(0,0),fx=0.3,fy=0.3)
                texto= i[1]
                result= model(img)
                labels = result.xyxyn[0][:, -1].numpy()
                if (labels.all()==0):
                    print("Modelo 2")
                    print(texto)
                    print("******************************")
                    img_path= SaveImageModel2(img)
                    t=str(texto[0])
                    #send_msj1(t, img_path)
                    #send_msj2(t, img_path)
                    #send_msj3(t, img_path)
                    labels=1
detect()