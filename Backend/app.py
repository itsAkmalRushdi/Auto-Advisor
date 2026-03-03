

from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route("/", methods=["GET"])
def home():
    return "AutoAdvisor Backend Running"
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    return jsonify({"reply": "Backend is alive."})

if __name__ == "__main__":
    app.run(debug=True)