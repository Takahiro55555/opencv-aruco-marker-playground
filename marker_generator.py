#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2

# ArUcoのライブラリを導入
aruco = cv2.aruco

# 4x4のマーカー，ID番号は50までの辞書を使う
dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)

marker_image = []
def main():
    col_num = 3
    row_num = 4
    marker_id = 0
    for r in range(row_num):
        tmp_marker_image = []
        for c in range(col_num):
            # ID番号は marker_id ，150x150ピクセルでマーカー画像を作る．
            ar_image = aruco.drawMarker(dictionary, marker_id, 150)

            # マーカ画像に余白を追加する
            ar_image_with_margin = cv2.copyMakeBorder(ar_image, 50, 90, 50, 50 ,cv2.BORDER_CONSTANT, value=[255])

            # マーカ画像の下部に区切り線を追加する
            ar_image_with_margin = cv2.copyMakeBorder(ar_image_with_margin, 0, 10, 0, 0 ,cv2.BORDER_CONSTANT, value=[0])

            # マーカ画像の下部にID文字列を追加する
            ar_image_with_text = cv2.putText(ar_image_with_margin, 'id: %d' % marker_id, (50, 270), cv2.FONT_HERSHEY_PLAIN, 2, (0), 1, cv2.LINE_AA)

            # 生成したマーカ画像をリストに格納する
            tmp_marker_image.append(ar_image_with_text)

            marker_id += 1

        # 上記のループで生成したマーカ画像のリストを水平方向に連結しリストに格納する
        marker_image.append(cv2.hconcat(tmp_marker_image))

    fileName = "ar.png"

    # 水平方向に連結したマーカ画像のリストを垂直方向に連結し、ファイルに保存する
    cv2.imwrite(fileName, cv2.vconcat(marker_image))

if __name__ == "__main__":
    main()
