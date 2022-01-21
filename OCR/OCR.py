from paddleocr import PaddleOCR, draw_ocr # main OCR dependencies
from matplotlib import pyplot as plt # plot images
import cv2 #opencv
import os # folder directory navigation

ocr_model = PaddleOCR(lang='en')

img_path = os.path.join('/home/anirudhlodh/Desktop/projects/Dr.-Medicine/OCR/abilify.jpg')

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

# import cv2
# import pytesseract
# import numpy as np
# import matplotlib as plt

# def ocr_core(img):
#     text = pytesseract.image_to_string(img)
#     return text

# img = cv2.imread('/home/anirudhlodh/Desktop/projects/Dr.-Medicine/OCR/abilify.jpg')
# img1 = np.array(img)

# def get_grayscale(image):
#     return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# def remove_noise(image):
#     return cv2.medianBlur(image, 5)

# def thresholding(image):
#     return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# def deskew(image):
#     coords = np.column_stack(np.where(image > 0))
#     angle = cv2.minAreaRect(coords)[-1]
#     if angle < -45:
#         angle = -(90 + angle)
#     else:
#         angle = -angle
#     (h, w) = image.shape[:2]
#     center = (w // 2, h // 2)
#     M = cv2.getRotationMatrix2D(center, angle, 1.0)
#     rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
#     return rotated

# img1 = get_grayscale(img1)
# img1 = thresholding(img1)
# img1 = remove_noise(img1)
# img1 = deskew(img1)
# cv2.imshow("pre-processed image", img)
# def listToString(s): 
#     str1 = " " 
#     return (str1.join(s))  
# x = ocr_core(img1)
# y = x.splitlines()
# print(listToString(y))

# h, w, c = img.shape
# boxes = pytesseract.image_to_boxes(img) 
# for b in boxes.splitlines():
#     b = b.split(' ')
#     img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

# cv2.imshow('img', img)
# cv2.waitKey(0)
