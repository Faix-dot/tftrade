from selenium.webdriver import Chrome
import requests
from selenium.webdriver.chrome.options import Options
import time

webdriver = r"C:\Users\assan\AppData\Local\Programs\Python\chromedriver.exe"

driver = Chrome(webdriver)


url = "https://tftrade.net" 

driver.get(url)

time.sleep (25) #wait for site to load and put eventual search filter

items = driver.find_elements_by_class_name("item")

for item in items :
    name = item.find_element_by_class_name("name").get_attribute('innerText')
    price = item.find_element_by_id("price")
    print (name, price.text)








