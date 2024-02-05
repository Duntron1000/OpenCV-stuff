import cv2 as cv

vid = cv.VideoCapture(0)

while(True):
    ret, src = vid.read()

    cv.imshow('frame', src)


    blur = cv.GaussianBlur(src, (15,15), 0)
    cv.imshow("blur", blur)

    hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)
    # mask = cv.inRange(hsv, (0, 150, 140), (12, 255, 255)) old hsv
    mask = cv.inRange(hsv, (0, 196, 192), (10, 255, 255))
    mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, (11, 11), iterations=10)
    cv.imshow("mask", mask)
    # masked = cv.bitwise_and(src, src, mask=mask)
    # cv.imshow("masked", masked)

    # canny = cv.Canny(mask, 75, 100)
    # cv.imshow("canny", canny)

    # thresh = cv.threshold(mask, 200, 255, cv.THRESH_BINARY_INV)[1]
    # cv.imshow("Thresh", thresh)

    contours, hiarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    contours_list = []
    area_list = []
    aprox_list = []
    centers_list = []

    # for contour in contours:
    #     approx = cv.approxPolyDP(contour, 0.01*cv.arcLength(contour, False), False)
    #     area = cv.contourArea(contour)
    #     if (len(approx) > 10) and (area > 100):
    #         contours_list.append(contours)
    #         aprox_list.append(approx)
    #         area_list.append(area)
    

    if (len(contours) > 0):

        contour = max(contours, key=cv.contourArea)

        largestContour = cv.approxPolyDP(contour, 0.01*cv.arcLength(contour, False), False)

        cv.drawContours(src, [largestContour], -1, 255, 2)

        # x,y,h,w = cv.boundingRect(largestContour)
        M = cv.moments(largestContour)
        if (M["m00"] != 0):
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

            # cv.rectangle(src, (x, y), (x+w, y+h), (0, 255, 255), 2)
            cv.circle(src, (cX, cY), 7, (0, 0, 255), -1)

            cv.imshow("final", src)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv.destroyAllWindows()
