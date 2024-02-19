from flask import Blueprint, request, abort
from models import db, Score
import json


api = Blueprint("api", __name__)


@api.route("/submit", methods=["POST"])
def submit():
	if not request.json: # Onko pyynnössä json-dataa
		abort(401)

	name = request.json.get("name")
	points = request.json.get("points")

	if not name:
		abort(401)

	if not points:
		abort(401)

	score = Score(name=name, points=points)
	db.session.add(score)
	db.session.commit()
	return "ok"


@api.route("/highscores", methods=["GET"])
def highscores():
	results = Score.query.order_by(Score.points.desc()).limit(10).all()
	data = []
	for result in results:
		data.append({"name": result.name, "points": result.points})
	return json.dumps(data, ensure_ascii=False, indent="\t")


@api.route("/clear", methods=["GET"])
def clear():
	Score.query.delete()
	db.session.commit()
	return "ok"
