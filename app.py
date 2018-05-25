from flask import Flask
from datetime import datetime
import pymongo
# change to scrape before production run
from scrape_mars import scrape1

# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define database and collection
db = client.mars_scrape
collection = db.results

# initialize Flask app
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