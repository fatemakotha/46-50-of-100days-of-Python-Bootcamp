from selenium import webdriver

chrome_driver_path = "C:/Users/fatem/OneDrive/Desktop/100 days of python bootcamp/DAY 46/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.com") #In mac, it won't run. So go to apple symbol: system preferences: security and privacy
                                    # It will say "chromedriver" was blocked and we click "allow anyway.
                                    #Now, when run it will open a popup with an "open" button. click open.
driver.close() #Closes the active tab
driver.quit() #Closes the entire window

