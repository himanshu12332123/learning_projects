import requests
query = input("Enter the topic you want news about: ")
api = "f1b5a02185a54f45be6dfb659d588f5c"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-10-15&sortBy=publishedAt&apiKey={api}"

print(url)

r = requests.get(url)
data = r.json()

articles = data["articles"]

for article in articles:
    print(article["title"])
    print(article["description"])
    print(article["url"])
    print("\n")