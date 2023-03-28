import cv2

img=cv2.imread("solar-system.jpg") 

cv2.putText(
    img,"Sun",(20,250),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255)
)
cv2.putText(
    img,"Mercury",(120,250),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255)
)
cv2.putText(
    img,"Venus",(220,150),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255)
)
cv2.putText(
    img,"Earth",(320,250),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255)
)
cv2.putText(
    img,"Moon",(330,170),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255)
)
cv2.putText(
    img,"Mars",(420,160),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255)
)
cv2.putText(
    img,"Jupiter",(520,250),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255)
)
cv2.putText(
    img,"Saturn",(720,150),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255)
)
cv2.putText(
    img,"Uranus",(920,250),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255)
)
cv2.putText(
    img,"Neptune",(1120,150),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255)
)



cv2.imshow("output",img)
cv2.waitKey(0)
