import json

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin


from app.helper import AlchemyEncoder
from config import SQLITE_URL

app = Flask(__name__)
app.config["CORS_HEADERS"] = "Content-Type"
app.config["SQLALCHEMY_DATABASE_URI"] = SQLITE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
cors = CORS(app)
db = SQLAlchemy(app)

from app.database.models import Track
from app.database.models import tracks

db.drop_all()
db.create_all()

[db.session.add(i) for i in tracks]
db.session.commit()


@app.route("/musics")
def get_random_musics():
    return jsonify(Track.get_random_tracks(limit=9))


@app.route("/music/filter/<label>/")
def filter_music(label: str):
    return jsonify(Track.filter_by_label_or_author(label=label, author=label))


@app.route("/music/filter/<label>/")
def filter_music(label: str):
    return jsonify(Track.filter_by_label_or_author(label=label, author=label))
