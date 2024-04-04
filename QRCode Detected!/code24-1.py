# code24-1
import sys
import cv2
import time
camera = cv2.VideoCapture(0)
if (camera.isOpened() == False):
    print("Can not open camera #0.")
    sys.exit(0)
print("Camera ready")
frameCounter = 0
doAgain = True
while doAgain:
    ret, image = camera.read()
    if ret:
        frameCounter += 1
        print("frame no.{}".format(frameCounter))
        cv2.imshow("Image", image)
        key = cv2.waitKey(1) & 0xFF
        if key == 27: # ESC
            cv2.destroyAllWindows()
            doAgain = False
camera.release()
