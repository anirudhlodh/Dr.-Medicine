from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
from selenium.webdriver.common.by import By
# import unicodedata

class MyBot:
    def __init__(self):
        
        user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
        
        self.options = webdriver.ChromeOptions()
        self.options.headless = True
        self.options.add_argument(f'user-agent={user_agent}')
        self.options.add_argument("--window-size=1920,1080")
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--allow-running-insecure-content')
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--proxy-server='direct://'")
        self.options.add_argument("--proxy-bypass-list=*")
        self.options.add_argument("--start-maximized")
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--no-sandbox')

        self.driver = webdriver.Chrome(executable_path="Scraping script/chromedriver", options=self.options)

        drug_query_name = "Aspirin"

        self.driver.get("https://go.drugbank.com/")
        self.driver.find_element(By.XPATH, '/html/body/main/div/div[1]/div[1]/div[2]/form/div[1]/div/input').send_keys(drug_query_name) # entering text in search bar       
        
        self.driver.find_element(By.XPATH, '/html/body/main/div/div[1]/div[1]/div[2]/form/div[1]/div/div/button').click()     #clicking search button
        #self.driver.get_screenshot_as_file("screenshot.png")
        print("\n\nABOUT THE DRUG : \n")
        print(self.driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/div[2]/dl[1]/dd[1]/p').text)       #printing stuff in first paragraph
        print("\n\nGENERIC NAME : \n")
        print(self.driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/div[2]/dl[1]/dd[3]').text)         #prints generic name
        print("\n\nOTHER BRAND NAMES : \n")
        print(self.driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/div[2]/dl[1]/dd[2]').text)      #clicking other names link
        #print(self.driver.find_element(By.XPATH, '/html/body/main/div/div[1]/div[2]').text)         #prints contentBox
        print("\n\nBACKGROUND : \n")
        print(self.driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/div[2]/dl[1]/dd[5]').text)
        print("\n\nINDICATIONS : \n")
        print(self.driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/div[2]/dl[2]/dd[1]').text)         #ads also come up in this
        print("\n\nSIDE EFFECTS : \n")
        print(self.driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/div[2]/dl[2]/dd[2]').text)
MyBot()