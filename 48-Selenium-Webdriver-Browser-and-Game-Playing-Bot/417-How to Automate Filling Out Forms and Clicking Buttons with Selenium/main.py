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
driver.get("https://en.wikipedia.org/wiki/Main_Page")

#Find the article_count number:_____(1)
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(article_count.text) #,583,440

##How to click on an element:_____(1)
# article_count.click() #clicks and goes to the statictics page

#Find element using link tag:_____(2)
# wikipedia_info = driver.find_element(By.LINK_TEXT, "Wikipedia")
# print(wikipedia_info.text)
# wikipedia_info.click()

#How to type in to a search bar of the website and then enter it: _____(3)
search = driver.find_element(By.NAME, "search")
print(search) #<selenium.webdriver.remote.webelement.WebElement (session="c9d583b27c94aa2facc99e092c09fdd3", element="c2850bf5-857e-40eb-9997-b763ac508782")>
search.send_keys("Neymar jr")
# go_button = driver.find_element(By.NAME, "go")
# go_button.click()
#--------------OR-----------------
search.send_keys(Keys.ENTER)