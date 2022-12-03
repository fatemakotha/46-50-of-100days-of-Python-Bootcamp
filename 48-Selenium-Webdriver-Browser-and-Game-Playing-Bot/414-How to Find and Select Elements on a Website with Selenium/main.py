from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service

#Set url to open up:
chrome_driver_path = "C:/Users/fatem/OneDrive/Desktop/100 days of python bootcamp/DAY 46/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.amazon.com/Instant-Pot-Pressure-Steamer-Sterilizer/dp/B08PQ2KWHS/ref=sr_1_2_sspa?crid=3PS0AQ9GG8NE&keywords=Instant+Pot+Duo+Evo&qid=1669968418&sprefix=instant+pot+duo+evo%2Caps%2C392&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyNTYzWU85WFJUQjlSJmVuY3J5cHRlZElkPUEwMTIwOTkxMVBCQU1GSlY0WkY5SSZlbmNyeXB0ZWRBZElkPUEwMzg0OTAxMk9aTTk5OTJORzU0NCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=")



driver.close() #Closes the active tab
# driver.quit() #Closes the entire window