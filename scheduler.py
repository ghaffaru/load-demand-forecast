from apscheduler.schedulers.background import BackgroundScheduler
import requests
import datetime
import json
import models
from app import db

now = datetime.datetime.now()
hour = now.hour
day = now.day
month = now.month
year = now.year


def save_predictions_hourly():
    weather = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?q=Ghana,sunyani&appid=e3311f6761891b3558c08b64e1a9bcf9'
    )
    temperature = round(weather.json()['main']['temp'] - 273.15, 2)
    humidity = weather.json()['main']['humidity']

    if temperature and humidity:
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

        pred = round(float(prediction.json()['prediction']), 2)

        already_pred = models.HourlyPrediction.query.filter_by(
            hour=hour, day=day, month=month, year=year).first()

        if already_pred:
            return
        pred_store = models.HourlyPrediction(hour=hour,
                                             day=day,
                                             month=month,
                                             year=year,
                                             humdity=humidity,
                                             temperature=temperature,
                                             prediction=pred)

        db.session.add(pred_store)

        db.session.commit()


def save_daily_predictions():
    weather = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?q=Ghana,sunyani&appid=e3311f6761891b3558c08b64e1a9bcf9'
    )

    temperature = round((weather.json()['main']['temp'] - 273.15), 2)
    humidity = weather.json()['main']['humidity']
    pressure = round(weather.json()['main']['pressure'], 2)

    if (temperature and humidity and pressure):
        headers = {'content-type': 'application/json'}

        prediction = requests.post('http://localhost:5000/api/predict/daily',
                                   data=json.dumps({
                                       'day': day,
                                       'month': month,
                                       'humidity': humidity,
                                       'temperature': temperature,
                                       'pressure': pressure
                                   }),
                                   headers=headers)

        pred = round(float(prediction.json()['prediction']), 2)

        already_pred = models.DailyPrediction.query.filter_by(
            day=day, month=month, year=year).first()

        if already_pred:
            return
        pred_store = models.DailyPrediction(day=day,
                                            month=month,
                                            year=year,
                                            humidity=humidity,
                                            temperature=temperature,
                                            pressure=pressure,
                                            prediction=pred)

        db.session.add(pred_store)

        db.session.commit()


scheduler = BackgroundScheduler()
# scheduler.add_job(save_predictions_hourly, 'cron', minute=00, second=0)
# scheduler.add_job(save_daily_predictions, 'cron', hour=0, minute=00, second=0)
# scheduler.add_job(save_daily_predictions, 'cron', minute=31, second=0)
scheduler.add_job(save_predictions_hourly, 'cron', second=30)
scheduler.start()
