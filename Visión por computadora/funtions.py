import  cv2
from PIL import Image
from vidgear.gears import CamGear

def active_cam():
    cap=[[0,1],[1,1],[2,1],[3,1],[4,1],[5,1],[6,1],[7,1]]
    cap[0][1]=CamGear(source='rtsp://contralor:Villegas555@192.168.103.149/cgi-bin/main.cgi').start()
    cap[1][1]=CamGear(source='rtsp://contralor:Villegas555@100.100.34.179/cgi-bin/main.cgi').start()
    cap[2][1]=CamGear(source='rtsp://contralor:Villegas555@100.100.34.183/cgi-bin/main.cgi').start()
    cap[3][1]=CamGear(source='rtsp://contralor:Villegas555@100.100.34.184/cgi-bin/main.cgi').start()
    cap[4][1]=CamGear(source='rtsp://contralor:Villegas555@192.168.103.233/cgi-bin/main.cgi').start()
    cap[5][1]=CamGear(source='rtsp://contralor:Villegas555@192.168.103.234/cgi-bin/main.cgi').start()
    cap[6][1]=CamGear(source='rtsp://contralor:Villegas555@192.168.102.105/cgi-bin/main.cgi').start()
    cap[7][1]=CamGear(source='rtsp://contralor:Villegas555@192.168.102.98/cgi-bin/main.cgi').start()
    return cap
def read_camera (cap):
    frames=[0,1,2,3,4,5,6,7]
    for j ,i in cap: 
        frames[j]=i.read()
    return frames
