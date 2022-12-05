from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
#To press enter and everything:
from selenium.webdriver.common.keys import Keys

#Open the desired website:
options = webdriver. ChromeOptions()
options. add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3372310590&f_AL=true&f_E=1&keywords=python%20intern")

signin_btn = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
signin_btn.click()