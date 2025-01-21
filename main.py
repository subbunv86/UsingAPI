import requests as req
import json as js
url = "https://newsapi.org/v2/everything?q=Tesla&sortBy=publishedAt&apiKey=46f202589db44e01a664edafeea480f0"

request = req.get(url)
content = request.json()

for article in content['articles']:
    print(article['title'])
    print(article['description'])