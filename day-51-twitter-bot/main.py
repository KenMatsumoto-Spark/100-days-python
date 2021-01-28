from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
import time

TWITTER_EMAIL = ""
TWITTER_PASS = ""

class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_driver_path = "C:\Development\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.down = ""
        self.up = ""

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        start_button = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        start_button.click()

        time.sleep(60)
        self.up = self.driver.find_element_by_class_name('download-speed').text
        self.down = self.driver.find_element_by_class_name('upload-speed').text


    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/login')
        time.sleep(3)
        user = self.driver.find_element_by_name('session[username_or_email]')
        user.send_keys(TWITTER_EMAIL)
        passw = self.driver.find_element_by_name('session[password]')
        passw.send_keys(TWITTER_PASS)
        passw.send_keys(Keys.ENTER)

        time.sleep(5)
        email = f"My down speed is {self.up} and my up is {self.down}"
        twit = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div')
        twit.send_keys(email)

        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]').click()



connection = InternetSpeedTwitterBot()
connection.get_internet_speed()
connection.tweet_at_provider()
