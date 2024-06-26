# importing Selenium and BeautifulSoup librarys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re
import time
import hashlib
import logging


# Set up logging
logging.basicConfig(level=logging.INFO)

# hashing function
def hash_content(content, position):
    return hashlib.sha256(f'{content}_{position}'.encode('utf-8')).hexdigest()

# Set up the Selenium web driver
service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)

links = [
    'https://twitter.com/Mr_Derivatives',
    #'https://twitter.com/warrior_0719',
    # 'https://twitter.com/ChartingProdigy',
    # 'https://twitter.com/allstarcharts',
    # 'https://twitter.com/yuriymatso',
    # 'https://twitter.com/TriggerTrades',
    # 'https://twitter.com/AdamMancini4',
    # 'https://twitter.com/CordovaTrades',
    # 'https://twitter.com/Barchart',
    # 'https://twitter.com/RoyLMattox'
        ]

output_counter = 0

time_interval = 120
try:
    while True:
        # count the appearence            
        symbol_counts = {}
        
        for link in links:
            
            
            # hashing symbols store
            unique_hashes = set()
            position = 0
                
            last_scroll_height = driver.execute_script("return document.body.scrollHeight")

            # adding the Links
            driver.get(link)


            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.TAG_NAME, 'body'))
                )
            
            while True:
                # parse the page using beautifulsoup
                soup = BeautifulSoup(driver.page_source, 'html.parser')

                # cashtag pattern
                tricker = re.compile(r'\$[A-Za-z]{3,4}')

                # Find all text matching the pattern
                symbols = soup.find_all(string=tricker)

                # Scroll down function
                # for _ in range(1): 
                driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
            
                time.sleep(2.5)
                        
                for symbol in symbols:
                    symbol_string = symbol.upper()
                    position += 1
                    symbol_hash = hash_content(symbol_string, position)
                    
                    if symbol_hash not in unique_hashes: 
                        unique_hashes.add(symbol_hash)
                        symbol_counts[symbol_string] = symbol_counts.get(symbol_string, 0) + 1

                driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
            
                time.sleep(2.5)
                        
                new_scroll_height = driver.execute_script("return document.body.scrollHeight")
            
                if new_scroll_height == last_scroll_height:
                    break
                
                else:
                # If it has, update the last scroll height for the next iteration
                    last_scroll_height = new_scroll_height
                        
                        
                    
        # print the output
        for symbol, count in symbol_counts.items():
            
            if output_counter != 0:
                print(f'{symbol} was mentioned \"{count}\" times, in the last \"{time_interval // 60}\" minutes.')
            else:
                print(f'{symbol} was mentioned \"{count}\" times')
            # print(symbol)
        
        print(f'Waiting for {time_interval // 60} minutes before starting the next session.')
        time.sleep(time_interval)
        
        # increment the counter when starting a new session
        output_counter += 1


    
    
except:  
    # quit the driver  
    driver.quit()
