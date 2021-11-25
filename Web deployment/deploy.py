#core pkgs
import streamlit as st
import cv2
from PIL import Image
import numpy as np
import pandas as pd
import os

@st.cache
def load_image(img):
	im = Image.open(img)
	return im



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
	
	



	st.header("Display")

	sentence = st.text_area("enter text")
	if st.button("Detect"):
		st.success(sentence.title())



	st.sidebar.header("About")
	st.sidebar.markdown("This is about and in this we will see who are peoples , had work on the project")

if __name__ == '__main__':
	main()
