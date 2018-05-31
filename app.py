from flask import Flask
from datetime import datetime
import pymongo
from scrape_mars import scrape
import os

# Initialize PyMongo to work with MongoDBs
MONGODB_URI = os.environ.get('MONGODB_URI')
print(f'\n######## MONGODB_URI: {MONGODB_URI}\n')
conn = MONGODB_URI # connection to heroku addon
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
    results = scrape()
    collection.insert_one(results)
    return str(results)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)