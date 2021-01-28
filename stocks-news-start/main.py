import requests
from datetime import datetime
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
change = float
change_message = str
today = datetime.today().date()
today_day = int(today.day)
yesterday_day = today_day - 1
day_before_yesterday = today_day - 2
month = today.month
if today.month < 10:
    month = '0' + str(today.month)
if yesterday_day < 10:
    yesterday_day = '0' + str(yesterday_day)
if day_before_yesterday < 10:
    day_before_yesterday = '0' + str(day_before_yesterday)

yesterday = f"{today.year}-{month}-{yesterday_day}"
day_before_yesterday = f"{today.year}-{month}-{day_before_yesterday}"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
alpha_api_key = "my alpha api key"
alpha_endpoint = "https://www.alphavantage.co/query"
alpha_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": alpha_api_key
}
response = requests.get(url=alpha_endpoint, params=alpha_params)
data = response.json()
yesterday_close = float(data["Time Series (Daily)"][yesterday]["4. close"])
before_yesterday_close = float(data["Time Series (Daily)"][day_before_yesterday]["4. close"])
if yesterday_close / before_yesterday_close < 0.95 or yesterday_close / before_yesterday_close > 1.05:
    change = int((yesterday_close / before_yesterday_close - 1) * 100)
    if change < 0:
        change *= -1
        change_message = f"TSLA: 🔻{change}%"
    else:
        change_message = f"TSLA: 🔺{change}%"

    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_api_key = "my news api key"
    news_endpoint = "https://newsapi.org/v2/everything"
    news_params = {
        "apiKey": news_api_key,
        "q": COMPANY_NAME
    }
    response = requests.get(url=news_endpoint, params=news_params)
    data = response.json()
    news_1 = f"Headline: {data['articles'][0]['title']}\nBrief: {data['articles'][0]['description']}"
    news_2 = f"{data['articles'][1]['title']}\n{data['articles'][1]['description']}"
    news_3 = f"{data['articles'][2]['title']}\n{data['articles'][2]['description']}"
    print(change_message)
    print(f"{news_1}\n{news_2}\n{news_3}")

    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    account_sid = "twilio login"
    auth_token = "twilio pass"
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body=change_message,
        from_="YOUR TWILIO VIRTUAL NUMBER",
        to="YOUR TWILIO VERIFIED REAL NUMBER"
    )
    print(message.status)

    account_sid = "twilio login"
    auth_token = "twilio pass"
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body=news_1,
        from_="YOUR TWILIO VIRTUAL NUMBER",
        to="YOUR TWILIO VERIFIED REAL NUMBER"
    )
    print(message.status)

# Optional: Format the SMS message like this: DONE
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
