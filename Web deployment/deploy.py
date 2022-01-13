#core pkgs
import streamlit as st
import cv2
from PIL import Image
import numpy as np
import pandas as pd
import os
from paddleocr import PaddleOCR, draw_ocr # main OCR dependencies
from matplotlib import pyplot as plt # plot images
import cv2 #opencv
import os # folder directory navigation
import spacy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
from selenium.webdriver.common.by import By

@st.cache

def listToString(s): 
    str1 = " " 
    return (str1.join(s))       

def load_image(img):
	ocr_model = PaddleOCR(lang='en')
	image = np.array(img.convert('RGB'))
	result = ocr_model.ocr(image)
	my_list = []
	for res in result:
  		my_list.append(res[1][0]) 

	final_ocr_output = listToString(my_list)

	nlp = spacy.load('/home/anirudhlodh/Desktop/projects/Dr.-Medicine/NER/NER_dr_medicine_new.spacy')
	test_text = final_ocr_output
	doc = nlp(test_text)
	print("Entities in '%s'" % test_text)
	
	for ent in doc.ents:
		return ent.text

	
	

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
		
	st.sidebar.header("About")
	st.sidebar.markdown("This is about and in this we will see who are peoples , had work on the project")

if __name__ == '__main__':
	main()
