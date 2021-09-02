#!/usr/bin/env python
# coding: utf-8

# In[1]:

#librerias
import cv2
import torch
import numpy as np
from datetime import datetime
from pathlib import Path 
import time
from twilio.rest import Client

# In[14]:
model= torch.hub.load('ultralytics/yolov5', 'yolov5l6')# modelo

# In[15]:
#configuración del modelo
model.conf = 0.66#confidence threshold (0-1)
model.classes= [0]# detección de personas


# In[4]:


cap = cv2.VideoCapture('rtsp://contralor:Villegas555@192.168.103.149/cgi-bin/main.cgi')


# In[5]:


w=int(cap.get(3)/2)
h=int(cap.get(4)/2)
fourcc = cv2.VideoWriter_fourcc(*'XVID')


# In[6]:


def video():
    date = datetime.now()
    year_month = date.strftime('%Y-%m-%d,%H-%M-%S')
    out = cv2.VideoWriter('detect/videos/'+year_month+'.avi', fourcc, 20.0, (w,h))
    t1 = datetime.now()
    while (datetime.now()-t1).seconds <= 10:
        ret, frame = cap.read()
        img = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
        out.write(img)
        


# In[7]:


def alert(img):
    date = datetime.now()
    year_month = date.strftime('%Y-%m-%d,%H-%M-%S')
    img_path= Path('detect/'+year_month+'.png')
    cv2.imwrite('detect/'+year_month+'.png',img)
    time.sleep(15)
    account_sid = 'AC1c5692cfc9751a2fa7a7140edcbba0c7' 
    auth_token = '1c268915b19aefbd8e0817aa20c3b443'  
    client = Client(account_sid, auth_token) 
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Hay una persona en la camara',      
                              to='whatsapp:+5492392537311') 


while(True):
    ret, frame= cap.read()
    date = datetime.now()
    hour= int(date.strftime('%H'))
    if hour>=19 or hour<=7:
        if frame is None:
            cap = cv2.VideoCapture('rtsp://contralor:Villegas555@192.168.103.149/cgi-bin/main.cgi')
        else:
            img = cv2.resize(frame,(0,0),fx=0.5, fy=0.5)
            result= model(img)
            result.render()
            labels = result.xyxyn[0][:, -1].numpy()
            if (labels.all() == 0):
                alert(img)
                video()
                time.sleep(11)
                cap = cv2.VideoCapture('rtsp://contralor:Villegas555@192.168.103.149/cgi-bin/main.cgi')
    #cv2.imshow('Camera',img)
     
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#cv2.destroyAllWindows()


