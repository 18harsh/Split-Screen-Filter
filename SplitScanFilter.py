import cv2
import numpy as np
import os
 
###################################
widthImg=400
heightImg =600
#####################################


cap = cv2.VideoCapture(0)
cap.set(10,150)
out = cv2.VideoWriter("video.avi", cv2.VideoWriter_fourcc(*'XVID'), 25, (widthImg,heightImg))


def drawLine(copyImg,y):
	copyImg = cv2.line(copyImg, (0,y), (copyImg.shape[1],y), (0,0,255), 10) 
	return copyImg

count =1
ResultImg= np.zeros((heightImg,widthImg,3),np.uint8)

while True:
    success, img = cap.read()
    img = cv2.resize(img,(widthImg,heightImg))

    copyImg = img.copy()
    ResultImg[count-1:count+4,0:img.shape[1]] = copyImg[count-1:count+4,0:img.shape[1]]
    copyImg = drawLine(copyImg,count+5)

    copyImg[0:count,0:img.shape[1]] = ResultImg[0:count,0:img.shape[1]]
    out.write(copyImg)
    cv2.imshow("WorkFlow", copyImg)
    # cv2.imshow("Result", ResultImg)
    count+=1

    if count>=600:
    	break

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break


cap.release()
out.release()
cv2.destroyAllWindows()