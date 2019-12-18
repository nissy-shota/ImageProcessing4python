"""
前述したように，フィルタリングは一般的にエッジまでぼかしてしまいますが,
cv2.bilateralFilter() によって使えるバイラテラルフィルタはエッジを保存しながら画像をぼかすことができます．
しかし，上記のフィルタリングに比べて処理速度が遅いという欠点があります．
既に紹介したガウシアンフィルタは注目がその近傍領域に対して重み付け平均した値を出力します．
これはガウシアンフィルタが注目画素の近傍の画素のみを考慮した関数であることを意味します．
近傍領域内の画素が似たような値を持っているか否か，注目画素がエッジ上に存在するか否かなどは考慮されません．
結果としてガウシアンフィルタはエッジの劣化が不可避です．

バイラテラルフィルタも同様にガウシアンフィルタを採用していますが，
画素値の差を考慮した関数として別のガウシアンフィルタも同時に使用します．
一つ目のガウシアンフィルタはフィルタリングに使用する画素は
‘空間的に近い位置にある’ことを保証してくれます．一方で，
二つ目のガウシアンフィルタは注目画素に似た画素値を持つ画素の値のみ考慮してフィルタリングすることを保証します．
結果としてバイラテラルフィルタはエッジを保存した画像のぼかしを実現できることになります．

cf:
http://people.csail.mit.edu/sparis/bf_course/
"""

import cv2
import numpy as np


FILE_PATH = "HashimotoKanna.jpg"
src_img = cv2.imread(FILE_PATH)

bilateral= cv2.bilateralFilter(src_img,9,75,75)


cv2.imshow('source', src_img)
cv2.imshow('bilateral', bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()