
import subprocess as sp
from datetime import datetime

#base de tiempo
date = datetime.now()
hour= int(date.strftime('%H'))
minute=int(date.strftime('%M'))
fecha=date.strftime('%A')
extProc = sp.Popen(['python3','model.py']) # ejecuta myPyScript.py 

#status = sp.Popen.poll(extProc) # status debería ser 'None' al correr

def tiempo():
    global date, hour, minute, fecha
    date = datetime.now()
    hour= int(date.strftime('%H'))
    minute=int(date.strftime('%M'))
    fecha=date.strftime('%A')

while True:
    tiempo()
    #intervalo de ejecucion
    if fecha == "Saturday" or fecha == "Sunday":
        if sp.Popen.poll(extProc) != None:
            extProc = sp.Popen(['python','model.py'])
    
    else:
        if hour>=7: #or hour<=10:
            if sp.Popen.poll(extProc) != None:
                extProc = sp.Popen(['python','model.py'])

        #intervalo de detencion        
        if sp.Popen.poll(extProc) == None:    
            if hour<19:    
                sp.Popen.terminate(extProc)# cierre del proceso
