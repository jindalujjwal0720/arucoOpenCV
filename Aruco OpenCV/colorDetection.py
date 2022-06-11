# color detection

import cv2
import numpy as np

Colors = [
    [[32, 10, 20], [161, 255, 255]], # Green
    [[14, 185, 185], [173, 255, 255]], # Orange
    [[0, 0, 0], [179, 255, 184]], # Black
    [[0, 0, 205], [179, 40, 233]] # Peach-pink
]

i = 3

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            perimeter = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*perimeter, True)
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            if objCor == 4:
                aspRatio = w/float(h)
                if aspRatio > 0.95 and aspRatio < 1.05:
                    print(approx)
                    print("square")
                    cv2.drawContours(imgResult, cnt, -1, (0, 0, 0), 2)
                    cv2.circle(imgResult, approx[0][0], 5, (0, 255, 0), cv2.FILLED)
                    cv2.circle(imgResult, approx[1][0], 5, (0, 255, 0), cv2.FILLED)
                    cv2.circle(imgResult, approx[2][0], 5, (0, 255, 0), cv2.FILLED)
                    cv2.circle(imgResult, approx[3][0], 5, (0, 255, 0), cv2.FILLED)
                    # print(cnt)


img = cv2.imread("CVtask.jpg")
img = cv2.resize(img, (440, 310))
imgResult = img.copy()
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
for i in range(4):
    lower = np.array(Colors[i][0])
    upper = np.array(Colors[i][1])
    mask = cv2.inRange(imgHSV, lower, upper)
    # imgResult = cv2.bitwise_and(img, img, mask=mask)
    getContours(mask)

# cv2.imshow("mask", mask)
cv2.imshow("Result", imgResult)

cv2.waitKey(0)