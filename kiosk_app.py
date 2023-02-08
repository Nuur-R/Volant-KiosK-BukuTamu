import time
import base64

import eel
import cv2

import faceRec as fr
import projectTime as pt
import dataManagemen as dm


def rImgName():
    with open('data/active/imageName.csv', 'r') as f:
        data = f.readline()
        return data

@eel.expose
def name():
    print("Hello from Python")

@eel.expose
def datang():
    eel.imgName(rImgName())
    eel.pythonTime(pt.realTime())
    eel.pythonDate(pt.realDate())
    eel.pythonStatus("Datang")
    dm.log(rImgName(),pt.realTime(),pt.realDate(),"DATANG")
    print("Name : " + rImgName() + " Datang")
@eel.expose
def pulang():
    eel.imgName(rImgName())
    eel.pythonTime(pt.realTime())
    eel.pythonDate(pt.realDate())
    eel.pythonStatus("Pulang")
    dm.log(rImgName(),pt.realTime(),pt.realDate(),"PULANG")
    print("Name : " + rImgName() + " Pulang")
eel.init('web')
eel.start('main.html',mode='chrome',cmdline_args=['--start-fullscreen'],block=False)



def main():
    while True:
        start_time = time.time()
        eel.sleep(0.01)

        frame=fr.video()
        
        # print(imgName+"tess")
        _, imencode_image = cv2.imencode('.jpg', frame)
        base64_image = base64.b64encode(imencode_image)
        eel.set_base64image("data:image/jpg;base64," + base64_image.decode("ascii"))
        
        # cv2.waitKey(1)

        elapsed_time = round((time.time() - start_time), 3)
        eel.set_elapsedtime(elapsed_time)
        
        # stream Name
        

main()