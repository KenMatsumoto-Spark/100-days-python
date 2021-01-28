from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://tinder.com/app")
FB_USER = ""
FB_PASS = ""

time.sleep(3)
driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button').click()

time.sleep(2)
driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button').click()

time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

input_email = driver.find_element_by_name("email")
input_email.send_keys(FB_USER)
input_pass = driver.find_element_by_name("pass")
input_pass.send_keys(FB_PASS)
input_pass.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)

time.sleep(5)
driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]').click()
driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button').click()

is_tinder_on = True

while is_tinder_on:
    time.sleep(2)
    try:
        driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button').click()

    except NoSuchElementException:
        time.sleep(2)

    except ElementClickInterceptedException:
        try:
            super_popup = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/button[2]')
            super_popup.click()

        except NoSuchElementException:
            try:
                match_popup = driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[4]/button/svg/path')
                match_popup.click()

            except NoSuchElementException:
                try:
                    home_popup = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
                    home_popup.click()

                except:
                    time.sleep(1)


