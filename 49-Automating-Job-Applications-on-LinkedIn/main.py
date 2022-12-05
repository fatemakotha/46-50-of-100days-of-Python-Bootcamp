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
PHONE = "01210121012"

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
time.sleep(5)
#Fill the username:
user = driver.find_element(By.ID, "username")
user.send_keys(username)
#Fill the password:
passw = driver.find_element(By.ID, "password")
passw.send_keys(password)
#Click sign in button:
submit = driver.find_element(By.CSS_SELECTOR, ".login__form_action_container button")
submit.click()
#--------------------------------------------------------------------------------------------------------------------------------------


#CLICK THE EASY-APPLY BUTTON: -----------------------------------------------------------------------------------------------------------
# time.sleep(5)
apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
apply_button.click()

#If application requires phone number and the field is empty, then fill in the number.
time.sleep(5)
phone = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
if phone.text == "":
    phone.send_keys(PHONE)

#Submit the application
submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
submit_button.click()