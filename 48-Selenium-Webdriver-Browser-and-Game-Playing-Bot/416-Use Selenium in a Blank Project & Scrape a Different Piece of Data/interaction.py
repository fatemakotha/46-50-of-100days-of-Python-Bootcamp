from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

options = webdriver. ChromeOptions()
options. add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

num_articles = driver.find_element(By.CSS_SELECTOR, ".mp-box #articlecount a") #***taps into the returns the no of articles that is shown at the top of the page
print(num_articles.text) #6,583,142