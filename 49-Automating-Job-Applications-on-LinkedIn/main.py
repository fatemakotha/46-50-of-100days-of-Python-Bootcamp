from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
#To press enter and everything:
from selenium.webdriver.common.keys import Keys
import os
import time

username = os.environ.get("Lk_email")
password = os.environ.get("Lk_password")


#LOGGING INTO LINKED IN USING THE LINK : -----------------------------------------------------------------------------------------------------------
#Open the desired website:
options = webdriver. ChromeOptions()
options. add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3372310590&f_AL=true&f_E=1&keywords=python%20intern")
#Click on sign-in:
signin_btn = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
signin_btn.click()
##Wait for the next page to load.
# time.sleep(5) **************************************
#Fill the username:
user = driver.find_element(By.ID, "username")
user.send_keys(username)
#Fill the password:
passw = driver.find_element(By.ID, "password")
passw.send_keys(password)
#Click sign in button:
submit = driver.find_element(By.CSS_SELECTOR, ".login__form_action_container button")
submit.click()
#------------------------------------------------------------------------------------------------------------------------------------------------------

#Click easy-apply button:
easyapply_btn = driver.find_element(By.CSS_SELECTOR, ".mt5 .display-flex button")
easyapply_btn.click()
