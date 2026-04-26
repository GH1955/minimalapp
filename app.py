import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "ok"

@app.route("/health")
def health():
    return jsonify({
        "test_value": os.environ.get("TEST_VALUE"),
        "zzz_test": os.environ.get("ZZZ_TEST")
    })
