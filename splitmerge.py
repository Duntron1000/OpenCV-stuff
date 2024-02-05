import cv2 as cv
import numpy as np

vid = cv.VideoCapture(0)


while(True):
    ret, frame = vid.read()

    blank = np.zeros(frame.shape[:2], dtype='uint8')

    cv.imshow('frame', frame)

    b, g, r = cv.split(frame)

    blue = cv.merge([b, blank, blank])
    green = cv.merge([blank, g, blank])
    red = cv.merge([blank, blank, r])

    cv.imshow('blue', blue)
    cv.imshow('green', green)
    cv.imshow('red', red)

    merged = cv.merge([b,g,r])
    cv.imshow('merged', merged)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv.destroyAllWindows()
