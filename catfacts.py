import requests

def get_cat_fact():
    try:
        response = requests.get("https://catfact.ninja/fact")
        data = response.json()
        return data["fact"]
    except:
        return "😿 Could not get a cat fact."