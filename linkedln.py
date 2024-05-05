
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui


import time

# Open LinkedIn
driver = webdriver.Chrome()
driver.get('https://www.linkedin.com')

# Log in to LinkedIn (replace with your credentials)
username = driver.find_element(By.ID , 'session_key')
time.sleep(2)
username.send_keys('amit97852phogat@gmail.com')
time.sleep(2)
password = driver.find_element(By.XPATH , "//input[@id='session_password']")
time.sleep(2)
password.send_keys('amit@97852')
time.sleep(2)
password.send_keys(Keys.RETURN)
time.sleep(5)

try:
    down_messagebox = driver.find_element(By.XPATH , "//button[@id='ember129']") 
    time.sleep(2)
    down_messagebox.click()
    time.sleep(2)
except:
    pass

search_box = driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")
time.sleep(2)
search_box.send_keys('rajasthan technical university, kota')
time.sleep(2)
search_box.send_keys(Keys.RETURN)
time.sleep(4)


connect_button = pyautogui.locateCenterOnScreen('connect.png' ,confidence=0.7)
pyautogui.sleep(4)
pyautogui.moveTo(connect_button)
pyautogui.sleep(2)
pyautogui.click()

time.sleep(4)