from flask import Flask, abort, request, jsonify
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


@app.route("/users", methods=["GET"])
def get_users():
    users = get_users_from_db()
    json_users = {"users": users}
    return jsonify(json_users)


def save_to_db(user_name):
    new_user = User(name=user_name)
    db.session.add(new_user)
    db.session.commit()
    return new_user


def get_users_from_db():
    query = User.query.all()
    users = [user.name for user in query]
    if users is not None:
        return users
    return ""
