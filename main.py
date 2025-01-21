import requests as req
from send_email import send_email
import json as js
apiKey = '46f202589db44e01a664edafeea480f0'
topic = 'India'
url = "https://newsapi.org/v2/everything?" \
    f"q={topic}&" \
    "sortBy=publishedAt&" \
    f"apiKey={apiKey}&" \
    "language=en"

request = req.get(url)
content = request.json()
body = ''
for article in content['articles'][:20]:
    if article['title'] == None:
        continue
    body = "Subject : Todays News" +"\n"+ body + article['title'] + '\n' \
    + article['description'] \
    + '\n'+article['url'] +'\n\n'
body = body.encode('utf-8')    
send_email(body)