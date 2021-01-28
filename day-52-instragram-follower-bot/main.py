from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException

chrome_driver_path = "C:\Development\chromedriver.exe"
similar_acc = ''
USER = ''
PASS = ''

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def login(self):
        self.driver.get('https://www.instagram.com/')
        time.sleep(2)
        user = self.driver.find_element_by_name('username')
        user.send_keys(USER)
        passw = self.driver.find_element_by_name('password')
        passw.send_keys(PASS)
        passw.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(3)
        search = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search.send_keys(similar_acc)
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]/div').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
        time.sleep(3)

        modal = self.driver.find_element_by_xpath('html/body/div[5]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(3)

    def follow(self):
        follows = self.driver.find_elements_by_css_selector('li button')
        for button in follows:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                time.sleep(2)
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                cancel_button.click()
                time.sleep(1)

        time.sleep(2)


connection = InstaFollower()
connection.login()
connection.find_followers()
connection.follow()