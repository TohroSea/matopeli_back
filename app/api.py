from flask import Blueprint, request, abort
from models import db, Score


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
	if not request.json:
		abort(401)
