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
cookie = driver.find_element(By.ID, "cookie")


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

#Set time variables
timeout = time.time() + 5
# print(timeout)
five_min = time.time() + 60*5 # 5minute
# print(five_min)



#Set up the mechanism:
while True:
    cookie.click()
    #Get all upgrade <b> tags
    all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
    item_prices = []
    #Convert <b> text into an integer price list:
    for price in all_prices:
        element_text = price.text
        if element_text != "":
            cost = int(element_text.split("-")[1].strip().replace(",", ""))
            item_prices.append(cost)

    print(item_prices)
    #Create dictionary of store items and prices:
    cookie_upgrades = {}
    for n in range(len(item_prices)):
        cookie_upgrades[item_prices[n]] = item_ids[n]
    print(f"cookie_upgrades: {cookie_upgrades}")
    print(f"cookie_upgrades.items(): {cookie_upgrades.items()}") #dict_items([(15, 'buyCursor'), (100, 'buyGrandma'), (500, 'buyFactory'), (2000, 'buyMine'), (7000, 'buyShipment'), (50000, 'buyAlchemy lab'), (1000000, 'buyPortal'), (123456789, 'buyTime machine')])

    #Get current cookie count:
    money_element = driver.find_element(By.ID, "money").text
    print(f"money_element: {money_element}") #1
    if "," in money_element:
        money_element = money_element.replace(",", "")
    cookie_count = int(money_element)
    #Find upgrades that we can currently afford:
    affordable_upgrades = {}
    for cost, id in cookie_upgrades.items():
        if cookie_count > cost:
            affordable_upgrades["cost"] = id
    print(f"affordable_upgrades: {affordable_upgrades}")


    #Purchase the most expensive affordable upgrade
    highest_price_affordable_upgrade = max(affordable_upgrades)
    print(highest_price_affordable_upgrade)
    to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

    driver.find_element(By.ID, "to_purchase_id").click()

    #Add another 5 seconds until the next check
    timeout = time.time() + 5
    #After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break