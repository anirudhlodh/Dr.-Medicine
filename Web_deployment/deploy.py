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
import sys
import shutil


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

def load_image():
	img_path = os.path.join('/home/anirudhlodh/Desktop/projects/Dr.-Medicine/Web deployment/tempDir/tempfile')
	result = ocr_model.ocr(img_path)

	# result

	my_list = []
	for res in result:
		my_list.append(res[1][0])
	
	final_ocr_output = listToString(my_list)
	final_ocr_output_lower = final_ocr_output.lower()
	print(final_ocr_output_lower)

	# test_text = final_ocr_output
	# doc = nlp(test_text)
	# print("Entities in '%s'" % test_text)
	# for ent in doc.ents:
	# 	return ent.text
	a_file = open("/home/anirudhlodh/Desktop/projects/Dr.-Medicine/Web deployment/dataset_drugs/Drugs.txt", "r")

	list_of_lists = []
	for line in a_file:
		stripped_line = line.strip()
		line_list = stripped_line.split()
		list_of_lists.append(line_list)

	a_file.close()

	result = []
	for sublist in list_of_lists:
		for item in sublist:
			result.append(item)

	for i in range(len(result)):
		result[i] = result[i].lower()

	res = [ele for ele in result if(ele in final_ocr_output_lower)]
	return res[0]

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
	def save_uploadedfile(uploadedfile):
		with open(os.path.join("tempDir","tempfile"),"wb") as f:
			f.write(uploadedfile.getbuffer())
			return st.success("Saved File:{} to tempDir".format(uploadedfile.name))
	html_temp = """ """
	st.markdown(html_temp , unsafe_allow_html = True)

	st.title("DOCTOR MEDICINE")
	st.text("E.P.I.C.S. project")

	st.subheader("Drug named entity extraction from images")
	image_file = st.file_uploader("Upload an image of a medicine box/strip",type=['jpg','png','jpeg'])
	if image_file is not None :
		dir = '/home/anirudhlodh/Desktop/projects/Dr.-Medicine/Web deployment/tempDir'
		for f in os.listdir(dir):
			os.remove(os.path.join(dir, f))		
		our_image = Image.open(image_file)
		st.text("Original Image")
		st.write(type(our_image))
		st.image(our_image)
		save_uploadedfile(image_file)
		if st.button("Identify and get details about the medicine"):
			st.header("Details about the medicine")
			x = load_image()
			st.text(x)
			y = scrape(x)
			for i in range(len(y)):
				st.write(y[i])
				st.text("")

		
	st.sidebar.header("Credits")
	st.sidebar.markdown("Anirudh Lodh - deployment and module linking")
	st.sidebar.markdown("Utkarsh Saxena - Named entity recognition (NER)")
	st.sidebar.markdown("Ajmal Khan - Web scraping (WS)")
	st.sidebar.markdown("Akshay Markhedkar - Optical character recognition (OCR)")
	st.sidebar.markdown("K.A. Patel Himey Atulkumar - NER team")
	st.sidebar.markdown("Bhavya Manoj Votavat - OCR team")
	st.sidebar.markdown("Aditya Pandit - deployment team")
	st.sidebar.markdown("Rituj Raghuwanshi - Documentation")


if __name__ == '__main__':
	main()
