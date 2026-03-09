from flask import Flask, request, jsonify
from ai_explainer import explain_car_choice
from rag import retrieve_cars
from financial import calculate_affordable_limit

app = Flask(__name__)

@app.route("/chat", methods=["POST"])

def chat():

    data = request.json
    income = float(data.get("income"))

    affordable_limit = calculate_affordable_limit(income)

    cars = retrieve_cars(affordable_limit)

    explanation = explain_car_choice(income, cars)

    return jsonify({
        "income": income,
        "affordable_limit": affordable_limit,
        "recommended_cars": cars,
        "ai_recommendation": explanation
    })

if __name__ == "__main__":
    app.run(debug=True)