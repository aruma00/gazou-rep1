import cv2
import glob
import numpy as np

# 画像9枚を読み込む
img_list = glob.glob("/Users/arimeshinnosuke/gazou/gazou1/*.png")

# 画像を読み込んでリストに格納
images = [cv2.imread(img_path) for img_path in img_list]

# すべての画像の幅を最小の幅に揃える
min_width = min(image.shape[1] for image in images) #最小の幅を代入
images = [cv2.resize(img, (min_width, img.shape[0])) for img in images] #すべての画像の幅をリサイズ

# 画像を垂直に結合
combined_image = np.vstack(images)

# 結合した画像を表示
cv2.imshow("Combined Image", combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()



