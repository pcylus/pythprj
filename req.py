import requests
res = requests.get('http://localhost:5000/whatsthetime')
print(res.text)