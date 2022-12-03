from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
#Set url to open up:
chrome_driver_path = "C:/Users/fatem/OneDrive/Desktop/100 days of python bootcamp/DAY 46/chromedriver.exe"


driver = webdriver.Chrome()
#driver.get() opens up the url assigned:
driver.get("https://www.amazon.com/Instant-Pot-Pressure-Steamer-Sterilizer/dp/B08PQ2KWHS/ref=sr_1_2_sspa?crid=3PS0AQ9GG8NE&keywords=Instant+Pot+Duo+Evo&qid=1669968418&sprefix=instant+pot+duo+evo%2Caps%2C392&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyNTYzWU85WFJUQjlSJmVuY3J5cHRlZElkPUEwMTIwOTkxMVBCQU1GSlY0WkY5SSZlbmNyeXB0ZWRBZElkPUEwMzg0OTAxMk9aTTk5OTJORzU0NCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Get hold of the price using CLASS_NAME:
price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole") #Looks for an element with class name
price_dollar = price_dollar.text
print(price_dollar)
price_cent = driver.find_element(By.CLASS_NAME, "a-price-fraction")
price_cent = price_cent.text
print(price_cent)
#Convert the price into float
price = price_dollar + "." + price_cent
print(price)
driver.close() #Closes the active tab
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Get hold of the price using CSS_SELECTORS:
# new_driver = webdriver.Chrome()
# new_driver = new_driver.get("https://www.python.org/")
#Lets say we have an anchor tag inside a div named "document-widget:
# new_driver.find_element(By.CSS_SELECTOR, ".document-widget a")

#Get hold of the price using X_PATH:
xxxx = driver.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[1]') #copy x_path by right clicking code in html
print(xxxx.text)





# driver.close() #Closes the active tab
# # driver.quit() #Closes the entire window