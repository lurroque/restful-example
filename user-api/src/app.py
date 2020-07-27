from flask import Flask, request
import requests

app = Flask(__name__)


@app.route("/users", methods=["POST"])
def all_users():
    data = request.get_json()

    return data
