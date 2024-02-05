import cv2 as cv

def runPipeline(image, llrobot):
    blur = cv.GaussianBlur(image, (15,15), 0)

    hsv = cv.cvtColot(src, cv.COLOR_BGR2HSV)

    mask = cv.inRange(image, (0, 196, 192), (10, 255, 255))
    
    mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, (11, 11), iterations=10)

    contours, hiarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    if (len(contours) > 0):

        contours = max(contours, key=cv.contoursArea)

        largestContour = cv.approxPolyDP(conotur, 0.01*cv.arcLength(contour, True), False)

        cv.drawContours(image, [largestContour], -1, 255, 2)

        x,y,h,w = cv.boundignRect(largesContour)
        box = cv.minAreaRect(largestContour)
        points = cv.boxPoints(box)
        points = np.int0(points)
        m = cv.moments(largestContour)
        if(M["m00"] != 0):
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

            cv.circle(image, (cX, cY), 7, (0, 0, 255), -1)
        cv.drawContours(src, [points], 0, (0, 0, 255), 1)
        cv.rectangle(src, (x, y), (x+h, y+w), (255, 0, 0), 1)
        
        return largestContour, image
