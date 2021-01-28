from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time



FORMS_LINK = ""
ZILLOW_SF = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    "Accept-Language": "pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6,ja;q=0.5"
}

response = requests.get(url=ZILLOW_SF, headers=headers)
zillow_web_page = response.text


soup = BeautifulSoup(zillow_web_page, parser="html.parser", features="lxml")
links = [f"https://www.zillow.com/{ap['href']}" for ap in soup.find_all(class_='list-card-link', href=True)]

prices = []
for ap in soup.find_all(class_='list-card-price'):
    new_price = ap.getText().split('+')[0]
    new_price = new_price.split('/mo')[0]
    prices.append(new_price)

addresses = [ap.getText() for ap in soup.find_all(class_='list-card-addr')]

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)


for index in range(len(prices)):
    driver.get(FORMS_LINK)
    time.sleep(2)
    ans1 = addresses[index]
    ans2 = prices[index]
    ans3 = links[index*2]
    inputs = driver.find_elements_by_class_name("quantumWizTextinputPaperinputInput")

    inputs[0].send_keys(ans1)
    inputs[1].send_keys(ans2)
    inputs[2].send_keys(ans3)

    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div').click()
