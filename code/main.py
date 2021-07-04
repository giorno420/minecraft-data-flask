# Initializing packages
import requests, os, json
from flask import Flask


# Opening config.json
with open('config.json', 'r') as configdata__:
  config = json.load(configdata__)

# Initializing Flask app
app = Flask(__name__)


# Main playerlist page
@app.route('/playerlist')
def index():

  # Requests stuff
  url = config['serverIP']
  headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
  }
  response = requests.request('GET', url, headers=headers)
  response = response.json()
  
  # Checking if "players" exists, if it doesn't, that means that the server is offline
  try:
    response = response['players']
  except KeyError:
      return "<h1>SERVER OFFLINE :(</h1>"

  # Checking if "list" exists. If it doesn't that means no one is online
  try:
    response = response['list']
    
    for i in response:
      return f'{i}<br>'
  
  except KeyError:
    return '<h1>NO ONE ONLINE</h1>'

# Returning all the json data acquired from the file
@app.route('/fulljsondata')
def fulljsondata():
  url = config['serverIP']
  headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
  }

  response = requests.get(url, headers=headers)
  return f"{response.text}"


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))