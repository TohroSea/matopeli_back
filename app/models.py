from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Score(db.Model):
	__tablename__ = "score"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(32), nullable=False)
	points = db.Column(db.Integer, nullable=False)
	time_created = db.Column(db.DateTime(timezone=True), server_default=db.func.now(), nullable=False)
