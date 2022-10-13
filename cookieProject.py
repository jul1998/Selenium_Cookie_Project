import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chrome_driver_path = Service("./chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=chrome_driver_path, options=op)

driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")


store_items = driver.find_elements(By.CSS_SELECTOR, "#store div b")
costs = [int(i.text.split(" - ")[1].replace(",","")) for i in store_items[:len(store_items) - 1]]

store = driver.find_elements(By.CSS_SELECTOR, "#store div")
items_ids = [i.get_attribute("id") for i in store]

#Get dict for ids and their costs
cookie_upgrades_dict = {items_ids[n]:costs[n] for n in range(len(costs))}

timeout = time.time() + 60*5

while True:
    #Get current money for purchaing items
    money = int(driver.find_element(By.ID, "money").text)
    if timeout > time.time():
        cookie.click()
        item_cost = 0

        #Get afoordable upgrade for cookie
        affordable_upgrades = {}
        for item, cost in cookie_upgrades_dict.items():
            if money >= cost:
                affordable_upgrades[cost] = item

            #Update the next affordable item for cookie
            try:
                if len(affordable_upgrades) > 0:
                    best_upgrade = max(affordable_upgrades)
                    purchase = affordable_upgrades[best_upgrade]
                    print(purchase)
                    driver.find_element(By.ID,purchase).click()
                else:
                    break
            except:
                break









