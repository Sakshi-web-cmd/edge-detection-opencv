import cv2
image=cv2.imread("c:\\Users\\Sakshi Hiremath\\Pictures\\A O J 7.jpg")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(gray,100,200)
#resizing the image and edge
resized_image=cv2.resize(image,(400,400))
resized_edges=cv2.resize(edges,(400,400))                           
cv2.imshow("Original image",resized_image)
cv2.imshow("Edge Detected image",resized_edges)
cv2.waitKey(0)
cv2.destroyAllWindows()