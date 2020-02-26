from apscheduler.schedulers.background import BackgroundScheduler
import requests
import datetime
import json
import models

now = datetime.datetime.now()
hour = now.hour
day = now.day
month = now.month

# def save_predictions_hourly():
#     print('hello')

# scheduler = BackgroundScheduler()
# scheduler.add_job(func=save_predictions_hourly, trigger='interval', seconds=1)
# scheduler.start()

weather = requests.get(
    'http://api.openweathermap.org/data/2.5/weather?q=Ghana,sunyani&appid=e3311f6761891b3558c08b64e1a9bcf9'
)
temperature = round(weather.json()['main']['temp'] - 273.15, 2)
humidity = weather.json()['main']['humidity']

if (temperature and humidity):
    headers = {'content-type': 'application/json'}
    prediction = requests.post('http://localhost:5000/api/predict/hourly',
                               data=json.dumps({
                                   'hour': hour,
                                   'day': day,
                                   'month': month,
                                   'humidity': humidity,
                                   'temperature': temperature
                               }),
                               headers=headers)

    print(round(float(prediction.json()['prediction']), 2))
