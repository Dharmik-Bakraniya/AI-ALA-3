from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    if request.method == "POST":
        user_input = request.form["user_input"].lower().strip()

        if user_input == 'quit':
            response = "Happy travels! Bon voyage! 🌍"
        elif 'beach' in user_input or 'island' in user_input:
            response = "Great beach destinations: Bali, Thailand, Maldives, Greece, or Mexico. Don't forget sunscreen!"
        elif 'budget' in user_input or 'cheap' in user_input:
            response = "Budget tips: Travel offseason, use hostels, cook your own meals, walk instead of taxi."
        elif 'pack' in user_input or 'what to bring' in user_input:
            response = "Pack light: Roll clothes, use packing cubes, bring versatile items, and always pack a first-aid kit."
        elif 'adventure' in user_input or 'hiking' in user_input:
            response = "Adventure spots: New Zealand, Costa Rica, Nepal, Peru. Pack good shoes and a waterproof jacket!"
        elif 'city' in user_input or 'urban' in user_input:
            response = "Top cities: Tokyo, Paris, New York, Barcelona, Istanbul. Get city passes for attractions."
        elif 'solo' in user_input or 'alone' in user_input:
            response = "Solo travel tips: Stay in social hostels, join free walking tours, trust your instincts, share itinerary."
        elif 'family' in user_input or 'kids' in user_input:
            response = "Family-friendly: Orlando, Singapore, London. Book apartments, pack snacks, plan kid-friendly activities."
        elif 'passport' in user_input or 'visa' in user_input:
            response = "Check passport validity (6+ months), research visa requirements, make copies of important documents."
        elif 'food' in user_input or 'cuisine' in user_input:
            response = "Food capitals: Italy, Thailand, Japan, Mexico, Vietnam. Try street food for authentic local flavors!"
        elif 'romantic' in user_input or 'honeymoon' in user_input:
            response = "Romantic spots: Paris, Santorini, Venice, Maldives. Book sunset dinners and private tours."
        elif 'winter' in user_input or 'snow' in user_input:
            response = "Winter wonderlands: Switzerland, Canada, Norway, Japan. Pack layers and thermal wear."
        elif 'safe' in user_input or 'security' in user_input:
            response = "Safety tips: Research areas, avoid flashing valuables, know emergency numbers, get travel insurance."
        else:
            response = "I can help with destinations, packing, budgets, safety, or specific types of travel. What are you planning?"

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
