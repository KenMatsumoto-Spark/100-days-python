from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# number_articles = driver.find_element_by_id("articlecount")
# print(number_articles.text)
# number = int(number_articles.text.split()[0].replace(",", ""))
# print(number)

# article_count = driver.find_element_by_css_selector("#articlecount a")
# article_count.click()

# all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()
#
# search = driver.find_element_by_name("search")
# search.send_keys(("Python"))
# search.send_keys(Keys.ENTER)

# -----------login exercise
#
# driver.get("http://secure-retreat-92358.herokuapp.com/")
#
# fname_entry = driver.find_element_by_name("fName")
# fname_entry.send_keys("Ken")
# lname_entry = driver.find_element_by_name("lName")
# lname_entry.send_keys("Matsumoto")
# email_entry = driver.find_element_by_name("email")
# email_entry.send_keys("h264matsumoto@gmail.com")
# signup_button = driver.find_element_by_css_selector(".btn")
# signup_button.click()
# # driver.quit()

# -----------cookie clicker bot
driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie = driver.find_element_by_id("bigCookie")

is_game_on = True
upgrade_time = True

while is_game_on:
    timeout = time.time() + 5
    while upgrade_time:
        cookie.click()
        if time.time() > timeout:
            break
    upgrade_list = driver.find_elements_by_css_selector("#products .enabled")
    try:
        upgrade_list[-1].click()
    except IndexError:
        pass