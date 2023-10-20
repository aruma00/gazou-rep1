import cv2

# 画像ファイルの読み込み(カラー画像(3チャンネル)として読み込まれる)
img = cv2.imread("hoge.jpg")

# 画像の表示
cv2.imshow("Image", img)

# キー入力を待つ（無制限）
while True:
    key = cv2.waitKey(0)
    
    # qキーで終了
    if key == ord('q'):
        break

# ウィンドウを閉じる
cv2.destroyAllWindows()