from flask import Flask, jsonify
import random

app = Flask("my-app")

@app.route("/roll")
def home():
    return jsonify({"roll": random.randint(1, 6)})


