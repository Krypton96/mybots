import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import json
from config import open_weather_token



def get_first_news():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"
    }
    url = "https://www.securitylab.ru/news/"
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    articles_cards = soup.find_all("a", class_="article-card")
    news_dict = {}


    for article in articles_cards:
        article_title = article.find("h2", class_="article-card-title").text.strip()
        article_desc = article.find("p").text.strip()
        article_url = f'https://www.securitylab.ru{article.get("href")}'
        
        article_date_time = article.find("time").get("datetime")
        date_from_iso = datetime.fromisoformat(article_date_time)
        date_time = datetime.strftime(date_from_iso, "%Y-%m-%d %H:%M:%S")
        article_date_timestamp = time.mktime(datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S").timetuple())


        article_id = article_url.split("/")[-1]
        article_id = article_id[:-4]

        # print (f"{article_title} | {article_url} | {article_date_timestamp}")

        news_dict[article_id] = {
            "article_date_timestamp" : article_date_timestamp,
            "article_title" : article_title,
            "article_url" : article_url,
            "article_desc" : article_desc
        }

        with open("news_dict.json", "w", encoding='utf-8') as file:
            json.dump(news_dict, file, indent=4, ensure_ascii=False)



def check_news_update():
    with open("news_dict.json", encoding='utf-8') as file:
        news_dict = json.load(file)
    
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"
    }

    url = "https://www.securitylab.ru/news/"
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    articles_cards = soup.find_all("a", class_="article-card")

    fresh_news ={}

    for article in articles_cards:
        article_url = f'https://www.securitylab.ru{article.get("href")}'
        article_id = article_url.split("/")[-1]
        article_id = article_id[:-4]

        if article_id in news_dict:
            continue
        else:
            article_title = article.find("h2", class_="article-card-title").text.strip()
            article_desc = article.find("p").text.strip()
            
            article_date_time = article.find("time").get("datetime")
            date_from_iso = datetime.fromisoformat(article_date_time)
            date_time = datetime.strftime(date_from_iso, "%Y-%m-%d %H:%M:%S")
            article_date_timestamp = time.mktime(datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S").timetuple())

            news_dict[article_id] = {
            "article_date_timestamp" : article_date_timestamp,
            "article_title" : article_title,
            "article_url" : article_url,
            "article_desc" : article_desc
        }

        fresh_news[article_id] = {
            "article_date_timestamp" : article_date_timestamp,
            "article_title" : article_title,
            "article_url" : article_url,
            "article_desc" : article_desc
        }
    with open("news_dict.json", "w", encoding='utf-8') as file:
        json.dump(news_dict, file, indent=4, ensure_ascii=False)

    return fresh_news


#############################################

def get_weather(city, open_weather_token):
    
    code_to_smile = { 
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Морось \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001f328",
        "Mist": "Туман \U0001f328"
    }
    
    
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        # pprint (data)

        city = data["name"]
        cur_weather = data["main"]["temp"]
        
        weather_description =data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            ds = "Посмотри в окно, не пойму что там за погода!"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
            f"Погода в городе: {city}\n{wd}\nТемпература: {cur_weather}°С\n"
            f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\n{wind} м/с\n"
            f"Восход солнца: {sunrise_timestamp}\n"
            f"Закат солнца: {sunset_timestamp}\n"
            f"Продолжительность дня: {length_of_the_day}\n"
            F"Хорошего дня:)"
        )

    except Exception as ex:
        print (ex)
        print ("Проверьте название города")


def main():
    # get_first_news()
    print (check_news_update())
    city = input("Введи город: ")
    get_weather(city, open_weather_token)

if __name__ == "__main__":
    main()
