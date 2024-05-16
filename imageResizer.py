import cv2

source="flowerss.jpg"
destination="newImage.jpg"
scale_percent=50

pht= cv2.imread(source,cv2.IMREAD_UNCHANGED)

new_width=int(pht.shape[1] * scale_percent / 100)
new_hight=int(pht.shape[0] * scale_percent/ 100)

output=cv2.resize(pht,(new_width,new_hight))

cv2.imwrite(destination,output)
cv2.waitKey(0)