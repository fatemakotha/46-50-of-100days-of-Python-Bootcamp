from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
#To press enter and everything:
from selenium.webdriver.common.keys import Keys
import os
import time

#Set facebook email and password as env variables:
FB_EMAIL = os.environ.get("fb_email")
FB_PASSWORD = os.environ.get("fb_pass")

#LOGGING INTO LINKED IN USING THE LINK : -----------------------------------------------------------------------------------------------------------
#Open the desired website:
options = webdriver. ChromeOptions()
options. add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://tinder.com/")
time.sleep(5)


#Login using Facebook:
login = driver.find_element(By.XPATH, '//*[@id="q-401777178"]/div/div[1]/div/main/div[1]/div/div/div/div/div[3]/div/div[2]/button')
login.click()

fb_login = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()

