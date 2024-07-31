
import cv2
import webbrowser

# initalize the camera

cap = cv2.VideoCapture(0)

# initialize the cv2 QRCode detector

detector = cv2.QRCodeDetector()
while True:
    _, img = cap.read()
    # detect and decode
    data,  bbox, _ = detector.detectAndDecode(img)
    # check if there is a QRCode in the image
    if data:
        a=data
        break
    # display the result
    cv2.imshow("QRCODEscanner", img)    
    if cv2.waitKey(1) == ord("q"):
        break
if data:
            if not data.startswith("http"):
                data = "http://" + data
b=webbrowser.open(str(data))
# print(str(a))
cap.release()
cv2.destroyAllWindows()
    
    
         

