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

    stock_yesterday = float(stock_data["2022-04-29"]["4. close"])
    stock_before_yesterday = float(stock_data["2022-04-28"]["4. close"])
    print(stock_yesterday)
    print(stock_before_yesterday)
    return 100 * (abs(stock_yesterday - stock_before_yesterday)) / ((stock_yesterday + stock_before_yesterday) / 2)
    # if 100*(abs(stock_yesterday-stock_before_yesterday))/((stock_yesterday+stock_before_yesterday)/2)>5:
    #     print("here")
    # else:
    #     print(100*(abs(stock_yesterday-stock_before_yesterday))/((stock_yesterday+stock_before_yesterday)/2))


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
        # print(news_data[x]["source"]["name"]+": "+news_data[x]["title"])


# print(news_data)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
def send_sms():
    client = Client(twilio_account_sid, twilio_auth_token)
    for x in news_articles:
        message = client.messages \
                        .create(
                             body=x,
                             from_=twilio_from_num,
                             to=twilio_to_num
                         )

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
news_articles = []
percent_change = stock_news()
if stock_news() > 5:
    get_news()
    send_sms()
else:
    get_news()
    send_sms()

