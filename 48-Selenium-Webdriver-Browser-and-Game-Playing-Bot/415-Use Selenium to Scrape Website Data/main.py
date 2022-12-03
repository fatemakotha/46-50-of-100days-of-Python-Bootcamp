from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#Make sure the window stays open unless specifically instructed to close or quit:
options = webdriver. ChromeOptions()
options. add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.python.org/")
# driver.close()

title = driver.find_element(By.CSS_SELECTOR, ".shrubbery h2") #gets the tite "Latest News"
print(title.text) #Latest News

# news = driver.find_element(By.CSS_SELECTOR, ".shrubbery .menu")
# print(news.text)

print("__________________________________________________________________________________________")

# Extract all dates as a list:
dates = []
extract_dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
# print(extract_dates) #[<selenium.webdriver.remote.webelement.WebElement (session="8d8106ff3d360a7e2480bba38ecf0aae", element="80d93403-7ca1-4516-9363-8310b4587070")>, <selenium.webdriver.remote.webelement.WebElement (session="8d8106ff3d360a7e2
for each_item in extract_dates:
    dates.append(each_item.text)
print(dates)


# Extract all events as a list:
events = []
extract_events = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
# print(extract_events) #[<selenium.webdriver.remote.webelement.WebElement (session="8d8106ff3d360a7e2480bba38ecf0aae", element="a5cb1f3e-14e9-4fd7-b95f-a17da7fd0fa9")>, <selenium.webdriver.remote.webelement.W
for each_title in extract_events:
    events.append(each_title.text)
print(events)


#Create a dictionary like this: {0: {'time': '12-07', 'name': 'NZPUG-Auckland Coding Evening'}, 1: {'time': '12-09', 'name': 'PyCon Bolivia 2022'}, 2: {'time': '12-17', 'name': 'Python Pizza Holguín'}, 3: {'time': '12-21', 'name': 'An Introduction to Model Drift - PyLadies A
events_dictio = {}
for n in range(len(events)):
    events_dictio[n] = {
        "time": dates[n],
        "name": events[n],
    }

print(events_dictio)

