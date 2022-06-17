import requests
import json


def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__ == '__main__':
    speak("News For Today")
    r = requests.get(
        'https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=574712d68df14fa983bd9655b4bfa9a8')
    news = r.text
    news_json = json.loads(news)
    arts = news_json['articles']
    for articles in arts:
        speak(articles['title'])
        speak('Moving On To The Next News...')

    speak("Thank You For Listening")
