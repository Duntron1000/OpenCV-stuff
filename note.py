import cv2 as cv
import numpy as np

# vid = cv.VideoCapture(0)

# ret, src = vid.read()
src = cv.imread('Photos/frcNote.jpeg')
cv.imshow('frame', src)


blur = cv.GaussianBlur(src, (13,13), 0)
cv.imshow("blur", blur)

hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)
# mask = cv.inRange(hsv, (0, 150, 140), (12, 255, 255)) old hsv
mask = cv.inRange(hsv, (0, 196, 192), (10, 255, 255))
cv.imshow("mask no morph", mask)
mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, (11, 11), iterations=10)
# mask = cv.dilate(mask, (200, 200), iterations=10)
cv.imshow("mask", mask)
# masked = cv.bitwise_and(src, src, mask=mask)
# cv.imshow("masked", masked)

# canny = cv.Canny(mask, 75, 100)
# cv.imshow("canny", canny)

# thresh = cv.threshold(mask, 200, 255, cv.THRESH_BINARY_INV)[1]
# cv.imshow("Thresh", thresh)

contours, hiarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# for contour in contours:
#     approx = cv.approxPolyDP(contour, 0.01*cv.arcLength(contour, False), False)
#     area = cv.contourArea(contour)
#     if (len(approx) > 10) and (area > 100):
#         contours_list.append(contours)
#         aprox_list.append(approx)
#         area_list.append(area)


if (len(contours) > 0):

    contour = max(contours, key=cv.contourArea)

    largestContour = cv.approxPolyDP(contour, 0.01*cv.arcLength(contour, True), False)

    cv.drawContours(src, [largestContour], -1, 255, 2)

    x, y, h, w = cv.boundingRect(largestContour)
    box = cv.minAreaRect(largestContour)
    points = cv.boxPoints(box)
    points = np.int0(points)
    M = cv.moments(largestContour)
    if (M["m00"] != 0):
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

        cv.drawContours(src, [points], 0, (0, 0, 255), 1)
        cv.rectangle(src, (x, y), (x+h, y+w), (255, 0 , 0), 1)
        cv.circle(src, (cX, cY), 7, (0, 0, 255), -1)

        cv.imshow("final", src)

cv.waitKey(0)
vid.release()
cv.destroyAllWindows()
