# -*- coding: UTF-8 -*-
# 讀取 QRcode 圖檔的內容，自動偵測內容的編碼
from pyzbar.pyzbar import decode
from PIL import Image
import chardet

def auto_decode_qrcode(image_path):
    # 讀取圖片
    image = Image.open(image_path)

    # 解碼QR碼
    decoded_objects = decode(image)

    # 檢測字元編碼
    encoding = chardet.detect(decoded_objects[0].data)['encoding']

    # 輸出解碼結果
    decoded_data = decoded_objects[0].data.decode(encoding)
    print(f'Data: {decoded_data}')
    print(f'Encoding: {encoding}')
    return decoded_data, encoding

if __name__ == "__main__":
    image_path = r"hasChineseContent.png"  # 替換成您的QR碼圖片路徑
    data, encode = auto_decode_qrcode(image_path)
    print(data, encode)
