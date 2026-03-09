from groq import Groq

client = Groq(api_key="YOUR_GROQ_API_KEY")

def explain_car_choice(income, cars):

    if not cars:
        return "No vehicles found within your budget."

    car_list = "\n".join(
        [f"{c['brand']} {c['model']} ({c['year']}) - {c['price']} LKR"
         for c in cars]
    )

    prompt = f"""
A Sri Lankan user earns {income} LKR monthly.

These vehicles are within their budget:

{car_list}

Recommend the best vehicle considering:
- reliability
- resale value in Sri Lanka
- fuel efficiency

Give a short explanation (max 4 sentences).
"""

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return completion.choices[0].message.content