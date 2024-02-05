import cv2 as cv

vid = cv.VideoCapture(0)


while(True):
    ret, frame = vid.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow('frame', frame)
    cv.imshow('gray', gray)

    # Blur
    blur = cv.GaussianBlur(frame, (5, 5), cv.BORDER_DEFAULT)
    cv.imshow('blur', blur)

    # Edge Cascade
    canny = cv.Canny(blur, 125, 175)
    cv.imshow('cany', canny)

    # Dilateing the image
    dilated = cv.dilate(canny, (7,7), iterations=3)
    cv.imshow('dilated', dilated)

    # Eroding 
    eroded = cv.erode(dilated, (7,7), iterations=3)
    cv.imshow('eroded', eroded)

    # Resize
    resized = cv.resize(frame, (500, 500), interpolation=cv.INTER_CUBIC)
    cv.imshow('Resized', resized)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv.destroyAllWindows()