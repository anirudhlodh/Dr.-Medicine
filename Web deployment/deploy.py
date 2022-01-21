#core pkgs
import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
from paddleocr import PaddleOCR, draw_ocr # main OCR dependencies
from matplotlib import pyplot as plt # plot images
import cv2 #opencv
import os # folder directory navigation
import spacy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from gingerit.gingerit import GingerIt
import pytesseract

user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
ocr_model = PaddleOCR(lang='en')
nlp = spacy.load('/home/anirudhlodh/Desktop/projects/Dr.-Medicine/NER/NER_dr_medicine_new.spacy')
@st.cache

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def remove_noise(image):
    return cv2.medianBlur(image, 5)

def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

def ocr_core(img):
    text = pytesseract.image_to_string(img)
    return text

def listToString(s): 
    str1 = " " 
    return (str1.join(s))       

def load_image(img):
	image = np.array(img)
	result = ocr_model.ocr(image)

	# result

	my_list = []
	for res in result:
		my_list.append(res[1][0])
	
	final_ocr_output = listToString(my_list)
	print(final_ocr_output)
	# print(my_list)
	# image = get_grayscale(image)
	# image = thresholding(image)
	# image = remove_noise(image)
	# image = deskew(image)
	# # cv2.imshow("pre-processed image", img)

	# x = ocr_core(image)
	# y = x.splitlines()
	# final_sc_output = listToString(y)

	# lo_case = listToString(y).lower()
	# parser = GingerIt()
	# ct = parser.parse(lo_case)
	# final_sc_output = ct['result']

	test_text = final_ocr_output
	doc = nlp(test_text)
	print("Entities in '%s'" % test_text)
	for ent in doc.ents:
		return ent.text
	# return doc.ents[0]

def scrape(ner_output):
	options = webdriver.ChromeOptions()
	options.headless = True
	options.add_argument(f'user-agent={user_agent}')
	options.add_argument("--window-size=1920,1080")
	options.add_argument('--ignore-certificate-errors')
	options.add_argument('--allow-running-insecure-content')
	options.add_argument("--disable-extensions")
	options.add_argument("--proxy-server='direct://'")
	options.add_argument("--proxy-bypass-list=*")
	options.add_argument("--start-maximized")
	options.add_argument('--disable-gpu')
	options.add_argument('--disable-dev-shm-usage')
	options.add_argument('--no-sandbox')
	driver = webdriver.Chrome(executable_path="/home/anirudhlodh/Desktop/projects/Dr.-Medicine/Scraping script/chromedriver", options = options)
	drug_query_name = ner_output
	driver.get("https://go.drugbank.com/")
	driver.find_element(By.XPATH, '/html/body/main/div/div[1]/div[1]/div[2]/form/div[1]/div/input').send_keys(drug_query_name) # entering text in search bar       
	driver.find_element(By.XPATH, '/html/body/main/div/div[1]/div[1]/div[2]/form/div[1]/div/div/button').click()     #clicking search button
	my_list = [["ABOUT THE DRUG :"],[driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/div[2]/dl[1]/dd[1]/p').text],
	["GENERIC NAME :"],[driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/div[2]/dl[1]/dd[3]').text],
	["OTHER BRAND NAMES :"],[driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/div[2]/dl[1]/dd[2]').text],
	["BACKGROUND :"],[driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/div[2]/dl[1]/dd[5]').text],
	["INDICATIONS :"],[driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/div[2]/dl[2]/dd[1]').text],
	["SIDE EFFECTS :"],[driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/div[2]/dl[2]/dd[2]').text]]

	return my_list
        
def main():
	""" Dr. Medicine App"""
	html_temp = """ """
	st.markdown(html_temp , unsafe_allow_html = True)

	st.title("Dr. Medicine ")
	st.text("Build with Streamlit and OpenCV and Intenal Modules")

	st.subheader("Medicine Detection")
	image_file = st.file_uploader("Upload Image",type=['jpg','png','jpeg'])
	if image_file is not None :
		our_image = Image.open(image_file)
		st.text("Original Image")
		st.write(type(our_image))
		st.image(our_image)
		if st.button("Detect"):
			st.header("Details about the medicine")
			x = load_image(our_image)
			st.text(x)
			y = scrape(x)
			for i in range(len(y)):
				st.write(y[i])
				st.text("")
	
		
	st.sidebar.header("About")
	st.sidebar.markdown("This is about and in this we will see who are peoples , had work on the project")

if __name__ == '__main__':
	main()
