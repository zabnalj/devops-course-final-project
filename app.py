import os
from flask import Flask, request, redirect, url_for
import redis

app = Flask(__name__)
r = redis.Redis(host="redis", port=6379)


OPTIONS = ["Cats", "Dogs"]

@app.route("/", methods=["GET"])
def index():
    votes = {option: int(r.get(option) or 0) for option in OPTIONS}
    return f"""
    <h1>Vote for your favorite animal</h1>
    <form method="POST" action="/vote">
        <button type="submit" name="vote" value="Cats">Cats</button>
        <button type="submit" name="vote" value="Dogs">Dogs</button>
    </form>
    <h2>Current Results</h2>
    <ul>
        <li>Cats: {votes['Cats']}</li>
        <li>Dogs: {votes['Dogs']}</li>
    </ul>
    """

@app.route("/vote", methods=["POST"])
def vote():
    option = request.form.get("vote")
    if option in OPTIONS:
        r.incr(option)
    return redirect(url_for("index"))