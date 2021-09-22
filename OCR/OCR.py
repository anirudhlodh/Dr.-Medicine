# text recognition
import cv2
import pytesseract
# read image
im = cv2.imread('./test3.jpg')
# configurations
config = ('-l eng --oem 1 --psm 3')
# pytessercat
text = pytesseract.image_to_string(im, config=config)
# print text
text = text.split('\n')
text