from selenium import webdriver

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463")

# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)


driver.get("https://www.python.org")
# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))
# logo = driver.find_element_by_class_name("python-logo")
# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")

# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

event_dates = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")

events = {}

for n in range(0, len(event_dates)):
    events[n] = {
        "time": event_dates[n].text,
        "name": event_names[n].text
    }

print(events)

#closes the tab
# driver.close()
#closes the window
driver.quit()