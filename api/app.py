from flask import Flask, jsonify
from model import session, Transposon

app = Flask(__name__)


@app.route("/")
def index():
    return "Hey there"

@app.route("/transposon/count", methods=["GET"])
def get_transposon_count():
    return jsonify(session.query(Transposon.name).count())

if __name__ == "__main__":
    app.run(debug=True)
