from flask import Flask
from flask import url_for
from flask import request
from flask import render_template
import os
from flask_bootstrap import Bootstrap
import podgetter as pg

SECRET_KEY = os.urandom(100)


app = Flask(__name__)
Bootstrap(app)
app.debug = True

@app.route('/results', methods=["POST", "GET"])
def index():
    if request.method == 'POST':
        podcast_url = request.form['podcast']
        import ipdb; ipdb.set_trace()
        pg.get_new_podcast(podcast_url)
        return render_template("results.html")

@app.route('/home', methods=["POST", "GET"])
def home():
        return render_template("index.html")


if __name__ == "__main__":
    app.run()