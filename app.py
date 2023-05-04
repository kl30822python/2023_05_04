from flask import Flask,render_template # 2023.05.04.

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.jinja.html")

@app.route("/learning/")
def learning():
    return render_template("learning.jinja.html") #