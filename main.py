import cv2
import numpy as np

url = 'http://192.168.0.106:8080/video'
cap = cv2.VideoCapture(url)

if not cap.isOpened():
    print("Failed to open camera")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame")
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        area = cv2.contourArea(contour)

        if area < 200:
            continue

        (x, y), radius = cv2.minEnclosingCircle(contour)
        center = (int(x), int(y))
        
        cv2.circle(frame, center, int(radius), (0, 255, 0), 2)

    cv2.imshow("Camera", frame)

    if cv2.waitKey(2) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
