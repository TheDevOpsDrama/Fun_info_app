from catfacts import get_cat_fact
from jokes import get_joke
from weather import get_weather

def main():
    print("\n🎉 Welcome to Fun Info App 🎉\n")

    # Cat Fact
    print("🐱 Cat Fact:")
    print(get_cat_fact())
    print()

    # Joke
    print("🤣 Random Joke:")
    print(get_joke())
    print()

    # Weather
    city = input("🏙️ Enter city name to check weather: ")
    print(f"🌤️ Weather in {city}:")
    print(get_weather(city))

if __name__ == "__main__":
    main()