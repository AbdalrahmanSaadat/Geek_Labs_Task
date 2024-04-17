# importing Selinum Library and Other essential modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time



# Setting up the chrome driver 
service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://twitter.com/Mr_Derivatives')

time.sleep(10)

driver.quit()