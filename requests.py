from flask import Flask
import datetime
from datetime import date


app = Flask(__name__)

@app.route('/google')
def hello_world():
  app.add_url_rule('/','google', hello_world)

if __name__ == '__main__':
   app.run()

