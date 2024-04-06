import cv2
import webbrowser 
def FindURL(string):
    x=string.split()
    res=[]
    for i in x:
        if i.find("https:")==0 or i.find("http:")==0:
            res.append(i)
    return res

img = cv2.imread( 'my_id.png' )
img2 = cv2.imread("my_assignment1.png")

qrCodeDetector = cv2.QRCodeDetector()
text = qrCodeDetector.detectAndDecode(img)[0]
text2 = qrCodeDetector.detectAndDecode(img2)[0]

if len(FindURL(text))==0:
    print(text)
else:
    webbrowser.open(text)
if len(FindURL(text2))==0:
    print(text2)
else:
    webbrowser.open(text2)
