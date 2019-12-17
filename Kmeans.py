"""
色の量子化とは、画像中で使用される色の数を削減する処理を指す．
このような処理をする理由として、記憶容量の削減が必要だったり、限られた表示色しか使えない装置があるかもしれない．
このような状況で色の量子化が行われる．ここでは色の量子化にK-Meansクラスタリングを使う．
"""
import cv2
import numpy as np

def sub_color(src,K):

    # 次元数を1落とす Channel 方向はのこしてHeightとWidthは残す．
    Z = src.reshape((-1,3))
    # float32型に変換
    Z = np.float32(Z)
    # 基準の定義
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    # criteriaとクラスタ数(K)を定義し kmeans()関数を適用
    ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    """
    compactness : 各点と対応する重心の距離の二乗和．
    labels : 各要素に与えられたラベル(‘0’, ‘1’ ...)の配列 (前チュートリアルにおける ‘code’ )．
    centers : クラスタの重心の配列．
    """
    # UINT8に変換 元画像の復元
    # Center : クラスタの重心のndarray
    # Label : その画素がどこのクラスタに属する火が　Centerに対応しているので labelは元画像のH*W個になる，
    # center[label.flatten()] これで，量子化を行うことが可能になる．
    center = np.uint8(center)
    res = center[label.flatten()]
    return res.reshape((src.shape))


FILE_PATH = "HashimotoKanna.jpg"
src_img = cv2.imread(FILE_PATH)
dst = sub_color(src_img, K=4)

cv2.imshow('Value', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

