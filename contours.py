import cv2 as cv
import numpy as np

vid = cv.VideoCapture(0)

while(True):
    ret, frame = vid.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('gray', gray)

    blank = np.zeros(frame.shape, dtype='uint8')
    cv.imshow('blank', blank)

    blur = cv.GaussianBlur(gray, (1,1), cv.BORDER_DEFAULT)

    canny = cv.Canny(blur, 125, 175)
    cv.imshow('canny', canny)

    # ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
    # cv.imshow('thresh', thresh)

    contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    # print(f'{len(contours)} contours found!')

    cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
    cv.imshow('drawn', blank)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv.destroyAllWindows()
