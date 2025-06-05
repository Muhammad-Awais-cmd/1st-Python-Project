import cv2
import mediapipe as mp
import time


class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5, modelComp=1):
        self.mode = mode 
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.modelComp = modelComp

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=self.mode,
                max_num_hands=self.maxHands,
                model_complexity=self.modelComp,
                min_detection_confidence=self.detectionCon,
                min_tracking_confidence=self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        #print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:   
                    self.mpDraw.draw_landmarks(img, handLms, 
                                self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw = True ):

        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                # print(id,lm)
                h, w, c= img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                #print(id, cx, cy)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx,cy), 5, (26,26,26), cv2.FILLED)

        return lmList
    
    def fingersUp(self, lmList):

        fingers = []
        tipIds = [4, 8, 12, 16, 20]

        if len(lmList) != 0:
            # Thumb (check x direction)
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # Fingers (check y direction)
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

        return fingers
    

def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        if len(lmList) != 0:   
            fingers = detector.fingersUp(lmList)
            print(fingers)

        cTime =time.time()
        fps = 1 / (cTime-pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10,70), 
                    cv2.FONT_HERSHEY_SIMPLEX, 3, (255,0,0), 3)

        cv2.imshow("image", img)
        cv2.waitKey(1)

if __name__ == "__main__":
   main()