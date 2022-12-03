from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

options = webdriver. ChromeOptions()
options. add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")


#Combine class, ID and name in CSS Selecttor
#<div id="mp-topbanner" class="mp-box">_____(1)
# <div id="articlecount">_____(1)
# <a href="/wiki/Special:Statistics" title="Special:Statistics">6,583,131</a>_____(1)
num_articles = driver.find_element(By.CSS_SELECTOR, ".mp-box #articlecount a") #_____(1)
print(num_articles.text) #6,583,142 _____(1)

#Just another example of CSS Selectors
vvv = driver.find_element(By.CSS_SELECTOR, ".mp-box #articlecount") #***taps into the returns the no of articles that is shown at the top of the page
print(vvv.text) #6,583,149 articles in English

