from selenium.webdriver import Chrome
import requests
from selenium.webdriver.chrome.options import Options
import time

webdriver = r"C:\Users\assan\AppData\Local\Programs\Python\chromedriver.exe"

driver = Chrome(webdriver)
driver.get("https://tftrade.net" )

time.sleep (25) #wait for site to load and put eventual search filter

items = driver.find_elements_by_class_name("item")

for item in items :
    name = item.find_element_by_class_name("name").get_attribute('innerText')
    price = item.find_element_by_id("price")

    #api url (only works for unique items!), sry i didn't put my key , just safety reasons
    url = ('https://backpack.tf/api/classifieds/search/v1?item_names=1&item=' + str(name) + '&quality=6&tradable=1&craftable=1&page_size=30&key=apikey')

    #takes the json data from the api url and converts it to a dictionary
    dict = (requests.get(url)).json()

    try :
        #this tries to find unpainted/unfestivized items
        for x in range(len(dict['buy']['listings'])):
            try:
                if dict['buy']['listings'][x]['item']['attributes']:
                    ()
            except KeyError:
                break

        #this tries to find out if the item has a key or metal value. if one of them is missing, then the value gets set to 0
        for bpmetalX in dict['buy']['listings'][x]['currencies']:
            try:
                if dict['buy']['listings'][x]['currencies']['metal']:
                    bpmetal = dict['buy']['listings'][x]['currencies']['metal']
            except KeyError:
                bpmetal = 0

        for bpkeysX in dict['buy']['listings'][x]['currencies']:
            try:
                if dict['buy']['listings'][x]['currencies']['keys']:
                    bpkeys = dict['buy']['listings'][x]['currencies']['keys']
            except KeyError:
                bpkeys = 0 

    except IndexError :
        continue

    print(name, price.text)
    print('backpack price: ', 'keys: ', bpkeys, 'metal: ', bpmetal)
