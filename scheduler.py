from apscheduler.schedulers.background import BackgroundScheduler

def save_predictions_hourly():
    print('hello')

scheduler = BackgroundScheduler()
scheduler.add_job(func=save_predictions_hourly, trigger='interval', seconds=1)
scheduler.start()