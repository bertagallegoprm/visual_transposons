from flask import Flask, jsonify, render_template
from model import session, Transposon

app = Flask(__name__, static_folder="static")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/transposon/count", methods=["GET"])
def get_transposon_count():
    # count = jsonify(session.query(Transposon.name).count())
    count = session.query(Transposon.name).count()
    return render_template("test.html", count=count)

if __name__ == "__main__":
    app.run(debug=True)
