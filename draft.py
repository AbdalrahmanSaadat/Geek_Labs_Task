# importing Selinum Library and Other essential modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
from bs4 import BeautifulSoup


# Setting up the chrome driver 
service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)


# list of links
links = [
    'https://twitter.com/Mr_Derivatives',
    'https://twitter.com/warrior_0719',
    'https://twitter.com/ChartingProdigy',
    'https://twitter.com/allstarcharts',
    'https://twitter.com/yuriymatso',
    'https://twitter.com/TriggerTrades',
    'https://twitter.com/AdamMancini4',
    'https://twitter.com/CordovaTrades',
    'https://twitter.com/Barchart',
    'https://twitter.com/RoyLMattox'
        ]

# the sympol class to look for it
ticker = '//a[contains(text(), "$")]'

# container = '//div[@data-testid="tweetText"]'

#r-bcqeeo r-qvutc0 r-poiln3 r-1loqt21

# the time between each session
time_interval = 15


driver.get(links[0])

time.sleep(5)


last_height = driver.execute_script("return document.body.scrollHeight")
while True:

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


soup = BeautifulSoup(driver.page_source, 'lxml')


symbols = soup.find_all('a', string=lambda t: t and t.startswith('$'))

# Write the results to a CSV file
with open('Results.csv', 'w', newline='', encoding='utf-8') as fhand:
    writer = csv.writer(fhand)
    writer.writerow(['Symbol'])
    for symbol in symbols:
        writer.writerow([symbol.text])
# driver.implicitly_wait(100)


# SCROLL_PAUSE_TIME = 1

# last_height = driver.execute_script("return document.body.scrollHeight")

# while True: 
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(SCROLL_PAUSE_TIME)
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height


# driver.implicitly_wait(100)





# WebDriverWait(driver, 20).until(
#     EC.presence_of_all_elements_located((By.XPATH, container))
# )

# with open('Results.csv', 'w', newline='', encoding='utf-8') as fhand:
#     writer = csv.writer(fhand)
    
#     writer.writerow(['Symbol'])
    
    # tweets = driver.find_elements(By.XPATH, container)
    
#     WebDriverWait(driver, 20).until(
#     EC.presence_of_all_elements_located((By.XPATH, container))
# )   
    
    # for spans in tweets:
    #     span = spans.find_elements(By.CLASS_NAME, 'r-18u37iz')
    
        # for text in span:
            # symbols = text.find_elements(By.XPATH, ticker)
        
#         WebDriverWait(driver, 20).until(
#     EC.presence_of_all_elements_located((By.XPATH, ticker))
# )

    # symbols = driver.find_elements(By.XPATH, ticker)
    #     # for symbol in symbols:
    # # if symbols.text:
    
    # for symbol in symbols:
    #     text = symbol.text
    #     if text.startswith('$'):
    #         writer.writerow([text])
    # else:
    #     print("empty")
    
# time.sleep(50)


print("succsseful")
driver.quit()





# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import csv
# from bs4 import BeautifulSoup



# service = Service(executable_path='chromedriver.exe')
# driver = webdriver.Chrome(service=service)



# links = [
#     'https://twitter.com/Mr_Derivatives',
#     'https://twitter.com/warrior_0719',
#     'https://twitter.com/ChartingProdigy',
#     'https://twitter.com/allstarcharts',
#     'https://twitter.com/yuriymatso',
#     'https://twitter.com/TriggerTrades',
#     'https://twitter.com/AdamMancini4',
#     'https://twitter.com/CordovaTrades',
#     'https://twitter.com/Barchart',
#     'https://twitter.com/RoyLMattox'
#         ]

# driver.get(links[0])

# time.sleep(5)


# last_height = driver.execute_script("return document.body.scrollHeight")
# while True:
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(5)
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height


# soup = BeautifulSoup(driver.page_source, 'lxml')


# # Write the results to a CSV file
# with open('Results.csv', 'w', newline='', encoding='utf-8') as fhand:
#     writer = csv.writer(fhand)
#     writer.writerow(['Symbol'])
#     symbols = soup.find_all('div', {'data-testid': 'tweetText'})
#     for symbol in symbols:
        
#         targets = symbol.find_all('span',{'class':'r-18u37iz'})
        
#         for target in targets:
#             writer.writerow([target.text])
        
        

# print("succsseful")
# driver.quit()