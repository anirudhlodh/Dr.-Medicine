from paddleocr import PaddleOCR, draw_ocr # main OCR dependencies
from matplotlib import pyplot as plt # plot images
import cv2 #opencv
import os # folder directory navigation

ocr_model = PaddleOCR(lang='en')

img_path = os.path.join('OCR/test1.png')

result = ocr_model.ocr(img_path)

# result

my_list = []
for res in result:
  my_list.append(res[1][0]) 
# print(my_list)

def listToString(s): 
    str1 = " " 
    return (str1.join(s))       
final_ocr_output = listToString(my_list) 

print(final_ocr_output)