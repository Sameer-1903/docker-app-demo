from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def home():
    # return jsonify(message="Hello from Flask Backend", service="backend")
    return jsonify(message="Hello from CI/CD! Sameer Suresh Kanade", service="backend")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)