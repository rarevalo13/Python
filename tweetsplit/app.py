from flask import Flask
from flask import url_for
from flask import request
from flask import redirect
from flask import render_template
import requests
import os
import tweetauth

SECRET_KEY = os.urandom(100)


app = Flask(__name__)
app.debug = True




@app.route('/')
def home():
    return render_template("index.html")

@app.route('/callback')
def callback():
    try:
        redirect_url = tweetauth.auth.()
        session['request_token'] = (tweetauth.auth.request_token.key, tweetauth.auth.request_token.secret)
    except tweetauth.tweepy.TweepError:
        print("Error! Failed to get request token!")
    return flask.redirect(redirect_url)


if __name__ == "__main__":
    app.run()