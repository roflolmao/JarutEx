#code24-2
import sys
import cv2
import time
camera = cv2.VideoCapture(0)
if (camera.isOpened() == False):
    print("Can not open camera #0.")
    sys.exit(0)
print("Camera ready")
doAgain = True
while doAgain:
    ret, image = camera.read()
    if ret:
        qrCodeDetector = cv2.QRCodeDetector()
        text, points = qrCodeDetector.detectAndDecode(image)
        if points is not None:
            print(text)
            cv2.imwrite("./result.jpg",image)
        else:
            print("QR code not detected")
        cv2.imshow("Image", image)
        key = cv2.waitKey(1) & 0xFF
        if key == 27: # ESC
            cv2.destroyAllWindows()
            doAgain = False
camera.release()
