import requests

city = "Moscow,RU"
appid = "a0d5cd142f95cf18239809115efc54a8"

res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                   params = {'q': city,'units':'metric','lang':'ru','APPID':appid})
data = res.json()

print("Город:", city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура", data['main']['temp'])
print("Скорость ветра:", data['wind']['speed'])
print("Видимость", data['visibility'])

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params = {'q': city,'units':'metric','lang':'ru','APPID':appid})
data = res.json()

print("--------------------------------------------")
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], ">\nТемпература <",
          '{0:+3.0f}'.format(i['main']['temp']), ">\nПогодные условия <",
          i['weather'][0]['description'], ">\nСкорость ветра <", i['wind']['speed'], ">\nВидимость <", i['visibility'], ">")
    print("--------------------------------------------")
