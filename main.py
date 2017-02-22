import cv2 as cv
import numpy as np


kernel = np.ones((10,10), np.uint8)
def mouse_callback(event, x, y, flags, param):

    if(event == cv.EVENT_LBUTTONDOWN):
        maxx = (hsv[y, x])
        low_h = (maxx[0] - 5)
        low_s = (maxx[1] - 5)
        low_v = (maxx[2] - 5)
        top_h = (maxx[0] + 10)
        top_s = (maxx[1] + 10)
        top_v = (maxx[2] + 10)

        cv.setTrackbarPos("HH", "Regular", top_h)
        cv.setTrackbarPos("HS", "Regular", top_s)
        cv.setTrackbarPos("HV", "Regular", top_v)
        cv.setTrackbarPos("LH", "Regular", low_h)
        cv.setTrackbarPos("LS", "Regular", low_s)
        cv.setTrackbarPos("LV", "Regular", low_v)
        minS = np.array([low_h, low_s, low_v])
        maxS = np.array([top_h, top_s, top_v])
        mask = cv.inRange(hsv, minS, maxS)
        cv.imshow("Mask", mask)

def change_slider(value):
    pass

cap = cv.VideoCapture(0)
cv.namedWindow("Regular")

cv.createTrackbar("HH", "Regular", 0, 180, change_slider)
cv.createTrackbar("LH", "Regular", 0, 180, change_slider)
cv.createTrackbar("HS", "Regular", 0, 255, change_slider)
cv.createTrackbar("LS", "Regular", 0, 255, change_slider)
cv.createTrackbar("HV", "Regular", 0, 255, change_slider)
cv.createTrackbar("LV", "Regular", 0, 255, change_slider)

while(True):

    ret, frame = cap.read()
    cap.set(3, 30)
    cap.set(4, 40)

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    cv.imshow("Regular", frame)

    maxx = cv.setMouseCallback("HSV", mouse_callback, hsv)
    if maxx is not None:
        low_h = (maxx[0] - 5)
        low_s = (maxx[1] - 5)
        low_v = (maxx[2] - 5)
        top_h = (maxx[0] + 5)
        top_s = (maxx[1] + 5)
        top_v = (maxx[2] + 5)

        cv.setTrackbarPos("HH", "Regular", top_h)
        cv.setTrackbarPos("HS", "Regular", top_s)
        cv.setTrackbarPos("HV", "Regular", top_v)
        cv.setTrackbarPos("LH", "Regular", low_h)
        cv.setTrackbarPos("LS", "Regular", low_s)
        cv.setTrackbarPos("LV", "Regular", low_v)
    low_h = cv.getTrackbarPos("HH", "Regular")
    low_s = cv.getTrackbarPos("HS", "Regular")
    low_v = cv.getTrackbarPos("HV", "Regular")
    top_h = cv.getTrackbarPos("LH", "Regular")
    top_s = cv.getTrackbarPos("LS", "Regular")
    top_v = cv.getTrackbarPos("LV", "Regular")
    minS = np.array([low_h, low_s, low_v])
    maxS = np.array([top_h, top_s, top_v])
    mask = cv.inRange(hsv, minS, maxS)
    cv.imshow("Mask", mask)
    cv.imshow('HSV', hsv)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
