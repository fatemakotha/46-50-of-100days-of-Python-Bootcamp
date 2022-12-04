from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

#Open the desired website:
options = webdriver. ChromeOptions()
options. add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

#Find the article_count number:
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(article_count.text) #,583,440

##How to click on an element:
# article_count.click() #clicks and goes to the statictics page

#Find element using link tag:
wikipedia_info = driver.find_element(By.LINK_TEXT, "Wikipedia")
print(wikipedia_info.text)
wikipedia_info.click()
