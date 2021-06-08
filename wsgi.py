from flask import Flask, jsonify
import random

app = Flask("another-name")

@app.route("/roll")
def home():
    return jsonify({"roll": random.randint(1, 6)})

print("ok")
