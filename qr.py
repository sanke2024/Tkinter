import pyzbar.pyzbar as pyzbar
import cv2
import numpy
# global result
final_result=[]
def scan():
    i = 0
    cap =captureDevice = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    while i<1:
        _,frame = cap.read()
        decoded = pyzbar.decode(frame)
        for obj in decoded:
            # print(obj.data)
            result=str(obj.data)
            result1=result[2:-1]
            global final_result
            final_result=result1.split(",")
            # print(result)
            i=i+1

        
        # cv2.imshow("QRCode",frame)
        # cv2.waitKey(5)
        # cv2.destroyAllWindows

# scan()
# print(final_result)
