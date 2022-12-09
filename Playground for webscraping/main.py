from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
#To press enter and everything:
from selenium.webdriver.common.keys import Keys
import os
import time

#Make sure the window stays open unless specifically instructed to close or quit:
options = webdriver. ChromeOptions()
options. add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.python.org/")

#FINDING A HEADING:_______________________1
# <div class="list-widgets row">
#     <div class ="list-widgets row" >
#         <div class="list-widgets row">
#             <h2 class="widget-title">
#                 <span></span> Lastest News: </h2>
title = driver.find_element(By.CSS_SELECTOR, ".shrubbery h2") #gets the tite "Latest News"
print(f"title is {title.text}") #title is Latest News
title_x = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[1]/div/h2')
print(f"title is {title_x.text}") #title is Latest News
print("-------------------------------------------------------------------------------------------------------------------------------")

#FINDING A BUTTOM:_______________________2
#<div class="options-bar-container do-not-print">
#   <a href="https://psfmember.org/civicrm/contribute/transact/?reset=1&id=2" class="donate-button"> Donate </a>
donate_button = driver.find_element(By.CSS_SELECTOR, ".options-bar-container a") #Use the first word of class to target as CSS ***
donate_button.click()