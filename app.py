from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_cat_fact():
    try:
        r = requests.get("https://catfact.ninja/fact")
        return r.json().get("fact", "Couldn't fetch a cat fact 😿")
    except:
        return "Cat fact service not available."

def get_joke():
    try:
        r = requests.get("https://official-joke-api.appspot.com/random_joke")
        data = r.json()
        return f"{data['setup']} - {data['punchline']}"
    except:
        return "Joke service not available."

def get_weather(city="Mumbai"):
    try:
        r = requests.get(f"https://wttr.in/{city}?format=%C+%t")
        return r.text.strip()
    except:
        return "Weather service not available."

@app.route("/", methods=["GET", "POST"])
def home():
    cat_fact = None
    joke = None
    weather = None
    if request.method == "POST":
        city = request.form.get("city", "Mumbai")
        cat_fact = get_cat_fact()
        joke = get_joke()
        weather = get_weather(city)
    return render_template("index.html", cat_fact=cat_fact, joke=joke, weather=weather)

if __name__ == "__main__":
    app.run(debug=True)