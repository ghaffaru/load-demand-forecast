from app import db

class HourlyPrediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hour = db.Column(db.Integer, nullable=False)
    day = db.Column(db.Integer, nullable=False)
    month = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    humdity = db.Column(db.Float, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    prediction = db.Column(db.Float, nullable=False)


class DailyPrediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.Integer, nullable=False)
    month = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    humidity = db.Column(db.Integer, nullable=False)
    pressure = db.Column(db.Integer, nullable=False)
    temperature = db.Column(db.Integer, nullable=False)
    prediction = db.Column(db.Float, nullable=False)

    