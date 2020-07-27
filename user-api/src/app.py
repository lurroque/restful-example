from flask import Flask, abort, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/user-api.db"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)


@app.route("/users", methods=["POST"])
def all_users():
    data = request.get_json()
    user = data.get("name") or abort(422, "name is required")
    try:
        save_to_db(user)
    except ConnectionError:
        abort(500)
    else:
        return data, 201


def save_to_db(user):
    new_user = User(name=user)
    db.session.add(new_user)
    db.session.commit()
