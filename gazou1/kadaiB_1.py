import cv2
import numpy as np
import glob

#画像ファイル9枚を順番に読み込み、5秒ずつ表示する

for i in range(9):
    img = cv2.imread(str(i)+".png")
    
    # 画像の表示
    cv2.imshow("Image", img)
    cv2.waitKey(5000) #5000ミリ秒（5秒）


