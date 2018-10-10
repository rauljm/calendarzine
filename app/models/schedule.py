from models import db


class Schedule(db.Model):
    __tablename__ = "schedule"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('schedules', lazy=True))

    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))  # this is not nullable because of a bug in sqlite :(
    room = db.relationship('Room', backref=db.backref('schedules', lazy=True))
