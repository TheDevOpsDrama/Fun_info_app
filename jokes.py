import requests

def get_joke():
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        data = response.json()
        return f"{data['setup']} 😂 {data['punchline']}"
    except:
        return "😅 Could not get a joke."