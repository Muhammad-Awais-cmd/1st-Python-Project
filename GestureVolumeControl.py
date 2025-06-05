import cv2
import time
import numpy as np
import HandTrackingminModule as htm
import math

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

#########################
wCam, hCam = 640, 480
#########################

cap = cv2.VideoCapture(0)

cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon=0.7)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_,
                        CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
scalar_vol = 0
scalar_volPer = 0
miniBar = 150
maxBar = 400
scalar_volBar = maxBar

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) !=0:
       #print(lmList[4], lmList[8])

        x1, y1 = lmList[4][1],lmList[4][2]
        x2, y2 = lmList[8][1],lmList[8][2]
        cx, cy = (x1+x2)//2, (y1+y2)//2

        cv2.circle(img, (x1,y1), 10, (0,255,255), cv2.FILLED)
        cv2.circle(img, (x2,y2), 10, (0,255,255), cv2.FILLED)
        cv2.circle(img, (cx,cy), 10, (255,255,255), cv2.FILLED)
        cv2.line(img, (x1,y1), (x2,y2),(128,0,128), 3)

        length = math.hypot(x2-x1, y2-y1)
        # print(length)

        # Hand Range 20 - 200
        # Volume Range -95 - 0

        scalar_vol = np.interp(length, [30, 270], [0.0, 1.0])
        scalar_volBar = int(np.interp(length, [30, 270], [maxBar, miniBar]))
        scalar_volBar = np.clip(scalar_volBar, miniBar, maxBar)
        scalar_volPer = int(np.interp(length, [30, 270], [0, 100]))
        scalar_vol = np.clip(scalar_vol, 0.0, 1.0)

        print(int(length), int(scalar_vol))
        volume.SetMasterVolumeLevelScalar(scalar_vol, None)

        if length<50:
            cv2.circle(img, (cx,cy), 10, (255,255,0), cv2.FILLED)       
        if length>250:
            cv2.circle(img, (cx,cy), 10, (0,0,255), cv2.FILLED)

    cv2.rectangle(img, (50,miniBar),(85,maxBar), 3)
    cv2.rectangle(img, (50, int(scalar_volBar)),(85,maxBar),
                   (0, 255, 0), cv2.FILLED)
    cv2. putText(img, f'{int(scalar_volPer)} %',(35,maxBar+30),
                  cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,255), 2)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2. putText(img, f'FPS: {int(fps)}',(40,50), cv2.FONT_HERSHEY_COMPLEX,
                 1, (255,255,0), 4)

    cv2.imshow("img", img)
    cv2.waitKey(1)