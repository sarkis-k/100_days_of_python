import requests
from keys import *
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla"


# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def stock_news():
    stock_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "outputsize": "full",
        "apikey": stock_key
    }
    stock_response = requests.get(url="https://www.alphavantage.co/query", params=stock_parameters)
    stock_response.raise_for_status()
    stock_data = stock_response.json()["Time Series (Daily)"]
    stock_data_list = [value for (key, value) in stock_data.items()]

    stock_yesterday = float(stock_data_list[0]["4. close"])
    stock_before_yesterday = float(stock_data_list[1]["4. close"])

    return 100 * (abs(stock_yesterday - stock_before_yesterday)) / ((stock_yesterday + stock_before_yesterday) / 2)


# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
def get_news():
    news_parameters = {
        "q": COMPANY_NAME,
        "from": "2022-05-01",
        "sortBy": "popularity",
        "apiKey": news_key
    }
    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"]
    for x in range(0, 3):
        news_articles.append(news_data[x]["source"]["name"] + ": " + news_data[x]["title"])


# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
def send_sms():
    client = Client(twilio_account_sid, twilio_auth_token)
    for x in news_articles:
        message = client.messages \
                        .create(
                             body=x,
                             from_=twilio_from_num,
                             to=twilio_to_num
                         )


news_articles = []
percent_change = stock_news()
if percent_change > 5:
    get_news()
    send_sms()
else:
    news_articles.append("Not worthy")
    send_sms()

