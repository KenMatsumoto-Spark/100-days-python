from bs4 import BeautifulSoup
import requests
import lxml
product_url = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    "Accept-Language": "pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6,ja;q=0.5"
}

response = requests.get(url=product_url, headers=headers)
product_web_page = response.text

soup = BeautifulSoup(product_web_page, parser="html.parser", features="lxml")

price = float(soup.find(name="span", id="priceblock_ourprice").getText()[1:])
if price < 100:
    print("send email")
else:
    print(f"{price}$ is still too expensive")
