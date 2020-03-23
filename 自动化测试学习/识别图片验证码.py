# coding=utf-8

from PIL import Image   # 用于打开图片和对图片处理
import numpy as np
import pytesseract  # 用于图片转文字
import cv2
import re
class VerificationCode(object):
    def get_picture(self):
        image = cv2.imread(r'C:\Users\Administrator\Desktop\pic.png')
        img = image[241:293,283:388]  # 裁剪坐标为[y0:y1, x0:x1]
        cv2.imshow('image',img)
        cv2.waitKey(0)
        return img
    #  #将图片进行降噪处理, 通过二值化去掉后面的背景色并加深文字对比度
    # def convert_Image(self,standard=127.5):
    #     #【灰度转换】
    #     image = self.get_picture()
    #     imgs = Image.open(image)
    #     img_obj = imgs.convert('L')
    #     #二值化
    #     #根据阈值 standard , 将所有像素都置为 0(黑色) 或 255(白色), 便于接下来的分割
    #     pixels = img_obj.load()
    #     for x in range(image.width):
    #         for y in range(image.height):
    #             if pixels[x, y] > standard:
    #                 pixels[x, y] = 255
    #             else:
    #                 pixels[x, y] = 0
    #     return image
    def change_Image_to_text(self):
        img = self.get_picture()
        # pytesseract.pytesseract.tesseract_cmd = r"D:\Program Files\Tesseract-OCR\tesseract.exe"  # 设置pyteseract路径
        testdata_dir_config =r'D:\Program Files\Tesseract-OCR\tessdata'
        result = pytesseract.image_to_string(img,lang='eng', config=testdata_dir_config)  # 图片转文字
        textCode = re.sub("\W", "", result)
        return textCode
if __name__=='__main__':
    a = VerificationCode()
    b = a.change_Image_to_text()
    print(b)