import requests as req
from send_email import send_email
import json as js
apiKey = '46f202589db44e01a664edafeea480f0'
url = "https://newsapi.org/v2/everything?q=Tesla&sortBy=publishedAt&apiKey=46f202589db44e01a664edafeea480f0"

request = req.get(url)
content = request.json()
body = ''
for article in content['articles']:
    body += article['title'] + '\n' + article['description'] + '\n\n'
body = body.encode('utf-8')    
send_email(body)