import requests, os, json
from flask import Flask

with open('config.json', 'r') as configdata__:
  config = json.load(configdata__)

app = Flask(__name__)

@app.route('/')
def index():
  url = config['serverIP']
  headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
  }
  response = requests.request('GET', url, headers=headers)
  response = response.json()
  try:
    response = response['players']
  except KeyError:
      return "<h1>SERVER OFFLINE :(</h1>"

  try:
    response = response['list']
    for i in response:
      return f'{i}<br>'
  except KeyError:
    return '<h1>NO ONE ONLINE</h1>'

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))