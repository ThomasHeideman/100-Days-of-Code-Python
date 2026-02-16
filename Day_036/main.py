import requests
import datetime

from secrets import alpha_vantage_key, news_api_key, telegram_token, telegram_id
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
TODAY = datetime.date.today()
YESTERDAY = TODAY - datetime.timedelta(days=1)


def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"

    params = {
        "chat_id": telegram_id,
        "text": text,
        "parse_mode" : 'HTML',
        "disable_web_page_preview": True
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    print("Success! Check your phone!.")


def get_news():
    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "from": YESTERDAY,
        "sortBy": "publishedAt",
        "apiKey": news_api_key
    }
    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    news_response.raise_for_status()
    return news_response.json()


def send_news(diff):
    news_data = get_news()
    news = news_data["articles"][0:3]
    icon = "🔺" if diff > 0 else "🔻"
    text_message = f'Tesla: {icon} {abs(diff): .2f}%'
    for news_item in news:
        title = f"<b>Headline:{news_item['title']}</b>"
        source = f"Source: {news_item['source']['name']}"
        descr = f"Brief: {news_item['description']}"
        link = f"<a href='{news_item['url']}'>{source} - Read more...</a>"
        text_message += ('\n\n' + title + '\n\n' + descr + '\n\n' + link)

    send_telegram_message(text_message)


def get_stock_info():
    parameters ={
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": alpha_vantage_key,
    }
    response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
    response.raise_for_status()
    data = response.json()


    if "Time Series (Daily)" in data:
        data_list = [value for (key, value) in data["Time Series (Daily)"].items()]
        last_closing = float(data_list[0]["4. close"])
        second_last_closing = float(data_list[1]["4. close"])
        difference = ((last_closing - second_last_closing) / second_last_closing) * 100

        if abs(difference) > 5:
            send_news(difference)
    else:
        print(f"Couldn't fetch data.  API Message: {data.get('Information', 'Unknown error')}")



get_stock_info()






