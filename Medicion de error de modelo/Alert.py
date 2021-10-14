#from twilio.rest import Client
from datetime import datetime
import cv2
from pathlib import Path
import pywhatkit

"""def Alert1(texto):
    account_sid = 'AC1c5692cfc9751a2fa7a7140edcbba0c7' 
    auth_token = 'cf1d6295995e2d218d957e9e54d9e0e6'  
    client = Client(account_sid, auth_token) 
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body=texto,
                              #media_url=''      
                              to='whatsapp:+5492392537311') """
def SaveImage(img):
    date = datetime.now()
    year_month = date.strftime('%Y-%m-%d,%H-%M-%S')
    cv2.imwrite('detect_model/'+year_month+'.png',img)
    img_path= Path('detect_model/'+year_month+'.png')
    return img_path

def SaveImageModel2(img):
    date = datetime.now()
    year_month = date.strftime('%Y-%m-%d,%H-%M-%S')
    cv2.imwrite('detect_model2/'+year_month+'_model2'+'.png',img)
    img_path= Path('detect_model2/'+year_month+'_model2'+'.png')
    return img_path

def send_msj1(t, img_path):
    pywhatkit.sendwhats_image(#phone_no='+5492392611662',
                        phone_no='+5492396575139',
                        img_path= img_path,
                        caption= t,
                        tab_close=True)
"""def send_msj2(t, img_path):
    pywhatkit.sendwhats_image(phone_no='+5492392524855',
                        img_path= img_path,
                        caption= t,
                        tab_close=True)
def send_msj3(t, img_path):
    pywhatkit.sendwhats_image(phone_no='+5492396575139',
                        img_path= img_path,
                        caption= t,
                        tab_close=True)"""