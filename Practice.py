import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
           for id, lm in enumerate(handLms.landmark):
           # print(id,lm)
            h, w, c= img.shape
            cx, cy = int(lm.x*w), int(lm.y*h)
            print(id, cx, cy)
            if id ==0:
               cv2.circle(img, (cx,cy), 15, (232,34,453), cv2.FILLED)

            if id ==4:
               cv2.circle(img, (cx,cy), 10, (6,44,6), cv2.FILLED)   

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            if id ==8:
               cv2.circle(img, (cx,cy), 10, (6,44,6), cv2.FILLED)   

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            if id ==12:
               cv2.circle(img, (cx,cy), 10, (6,44,6), cv2.FILLED)   

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            if id ==16:
               cv2.circle(img, (cx,cy), 10, (6,44,6), cv2.FILLED)   

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            if id ==20:
               cv2.circle(img, (cx,cy), 10, (6,44,6), cv2.FILLED)   

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)


    cTime =time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10,70), cv2.FACE_RECOGNIZER_SF_FR_COSINE,3,
(0,0,0), 3)

    cv2.imshow("image", img)
    cv2.waitKey(1)