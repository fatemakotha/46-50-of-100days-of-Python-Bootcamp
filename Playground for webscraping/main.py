from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
#To press enter and everything:
from selenium.webdriver.common.keys import Keys
import os
import time
import urllib


#Make sure the window stays open unless specifically instructed to close or quit:
options = webdriver. ChromeOptions()
options. add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.python.org/")

#FINDING A HEADING:_______________________1
# <div class="list-widgets row">
#     <div class ="medium-widget blog-widget" >
#         <div class="shrubbery">
#             <h2 class="widget-title">
#                 <span></span> Lastest News: </h2>
title = driver.find_element(By.CSS_SELECTOR, ".shrubbery h2") #gets the tite "Latest News"
print(f"title is {title.text}") #title is Latest News
title_x = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[1]/div/h2')
print(f"title is {title_x.text}") #title is Latest News
title_y = driver.find_element(By.CSS_SELECTOR, ".medium-widget .shrubbery .widget-title")
print(f"title is {title_y.text}") #title is Latest News
print("-------------------------------------------------------------------------------------------------------------------------------")



#FINDING A BUTTON:__________a href_____________2
#<div class="options-bar-container do-not-print">
#   <a href="https://psfmember.org/civicrm/contribute/transact/?reset=1&id=2" class="donate-button"> Donate </a>
#Uncomment later ******:
donate_button = driver.find_element(By.CSS_SELECTOR, ".options-bar-container a") #Use the first word of class to target as CSS ***Co
donate_button.click() #WORKS
donate_button_x = driver.find_element(By.CSS_SELECTOR, ".options-bar-container .donate-button") #Use first words of 2 classes
donate_button_x.click() #WORKS
print("-------------------------------------------------------------------------------------------------------------------------------")





#FINDING A BUTTON:___________button____________3
#<div class="options-bar">
#   <a id="site-map-link" class="jump-to-menu" href="#site-map">
#   <form class="search-the-site" action="/search/" method="get">
#       <fieldset title="Search Python.org">
#           <input id="id-search-field" name="q" type="search" role="textbox" class="search-field" placeholder="Search" value tabindex="1">
#           <button type="submit" name="submit" class="search-button" title="Submit this Search" tabindex="3">
# go_button = driver.find_element(By.CSS_SELECTOR, ".screen-reader-text input button") #DOES NOT WORK
# go_button = driver.find_element(By.CSS_SELECTOR, ".options-bar .jump-to-menu .search-the-site fieldset button") #DOES NOT WORK
# go_button = driver.find_element(By.CSS_SELECTOR, ".options-bar .jump-to-menu .search-the-site button") #DOES NOT WORK
# go_button = driver.find_element(By.CSS_SELECTOR, ".options-bar .jump-to-menu .search-the-site .search-button") #DOES NOT WORK
go_button = driver.find_element(By.CLASS_NAME, "search-button") #DOES NOT WORK
go_button.click() #worksss **
go_button_x = driver.find_element(By.CSS_SELECTOR, ".options-bar form fieldset button") #workssss ***
go_button_x.click() #worksss **
go_button_x = driver.find_element(By.CSS_SELECTOR, ".options-bar form fieldset .search-button") #workssss ***
go_button_x.click() #worksss **
print("-------------------------------------------------------------------------------------------------------------------------------")

#FINDING A TEXTBOX TO TYPE IN:_______________________4
# <form class="search-the-site" action="/search/" method="get">
#   <fieldset title="Search Python.org">
#       <span></span>
#           <label class="screen-reader-text" for="id-search-field"> Search This Site </label>
#               <input id="id-search-field" name="q" type="search" role="textbox" class="search-field" placeholder="Search" value tabindex="1">

textbox = driver.find_element(By.CSS_SELECTOR, ".search-the-site fieldset .search-field") #*****
textbox.send_keys("Look for xyz") #Works

# textbox_x = driver.find_element(By.CSS_SELECTOR, ".screen-reader-text input")
# textbox_x.send_keys("hhhh") #DOES NOT WORK
# textbox_x = driver.find_element(By.CSS_SELECTOR, ".screen-reader-text .search-field")
# textbox_x.send_keys("hhhh")#DOES NOT WORK
#print("-------------------------------------------------------------------------------------------------------------------------------")

#FINDING AN IMAGE:_______________________4
# get the image source
img = driver.find_element(By.CLASS_NAME, "python-logo")
# src = img.get_attribute('src')
# # download the image
# urllib.urlretrieve(src, "python.png")
with open("python-img.png", "wb") as f:
    f.write(img.screenshot_as_png)
