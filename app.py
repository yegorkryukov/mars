from flask import Flask
from datetime import datetime
import pymongo

# change to scrape before production run
from scrape_mars import scrape1
import pymongo
app = Flask(__name__)

@app.route('/')
def homepage():

    return """
    <h1>Main page to Mars</h1>
    """


@app.route('/scrape')
def do_scrape(): 
    results = scrape1()
    return str(results)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)