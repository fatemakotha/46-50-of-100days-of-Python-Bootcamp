from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
#To press enter and everything:
from selenium.webdriver.common.keys import Keys
import time



#Open the desired website:
options = webdriver. ChromeOptions()
options. add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options=options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

#Get cookie to click on
# cookie = driver.find_element(By.ID, "cookie")


#Get upgrade item ids:
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
print(items) #[<selenium.webdriver.remote.webelement.WebElement (session="3e543f33de0881f92e542becce1ab368", element="87cc12f5-ee08-423c-9e9a-2c1e7b99f154")>, <selenium.webdriver.remote.webelement.WebElement (session="3e54

# item = driver.find_element(By.CSS_SELECTOR, "#store div")
# print(item)


#Create a list of item_ids:
# item_ids = [item.get_attribute("id") for item in items] #----OR------#
item_ids = []
for item in items:
    attribute = item.get_attribute("id")
    item_ids.append(attribute)
    # print(attribute)
print(item_ids) #['buyCursor', 'buyGrandma', 'buyFactory', 'buyMine', 'buyShipment', 'buyAlchemy lab', 'buyPortal', 'buyTime machine', 'buyElder Pledge']


