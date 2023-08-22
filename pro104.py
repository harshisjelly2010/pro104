import cv2

solar = cv2.imread("PRO-104-Project-Image-main\solar-system.jpg")
height,width,channel = solar.shape 
cv2.putText(solar,"Sun", (100, 100), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255))
cv2.putText(solar,"Mercury", (100, 180), cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255))
cv2.putText(solar,"Venus", (180, 180), cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255))
cv2.putText(solar,"Earth", (280, 180), cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255))
cv2.putText(solar,"Mars", (380, 180), cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255))
cv2.putText(solar,"Jupiter", (430, 120), cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255))
cv2.putText(solar,"Saturn", (680, 120), cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255))
cv2.putText(solar,"Uranus", (890, 180), cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255))
cv2.putText(solar,"Neptun", (1045, 180), cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255))
cv2.imshow("solar pic", solar)
cv2.waitKey(0)