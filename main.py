import cv2 as cv
import numpy as np

show_mask = False
mask = None
maxx = ([130,34,76])

def mouse_callback(event, x, y, flags, param):
    global show_mask, mask, maxx
    if(event == cv.EVENT_LBUTTONDOWN):
        maxx = (hsv[y, x])
        show_mask = True

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
count = 0
while(True):
    ret, frame = cap.read()
    cap.set(3, 30)
    cap.set(4, 40)
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    cv.setMouseCallback("HSV", mouse_callback, hsv)
    cv.imshow('HSV', hsv)
    cv.imshow("Regular", frame)
    if show_mask:
        low_h = (maxx[0] - 10)
        low_s = (maxx[1] - 10)
        low_v = (maxx[2] - 10)
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
        kernel = np.ones((5,5), np.uint8)
        erosion = cv.erode(mask, kernel, iterations = 1)
        dilation = cv.dilate(mask, kernel, iterations=1)
        cv.imshow("Mask", mask)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

