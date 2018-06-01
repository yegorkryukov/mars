from flask import Flask
from datetime import datetime
import pymongo
from scrape_mars import scrape
import os

# Initialize PyMongo to work with MongoDBs
MONGODB_URI = os.environ.get('MONGODB_URI')
client = pymongo.MongoClient(MONGODB_URI)

# Define database and collection
db = client.get_default_database()
collection = db.mars_scrape

# initialize Flask app
app = Flask(__name__)

@app.route('/')
def homepage():
    data = collection.find()
    print(data)
    return f"""
    <h1>Data in the DB:</h1> {str(data[0])}
    """

@app.route('/scrape')
def do_scrape(): 
    # Launch function to scrape data
    results = scrape()

    # Delete all documents inside a collection
    collection.remove({})

    # Insert newly obtained data into the db
    collection.insert_one(results)
    return f'Scrape finished. This was inserted into db\n {results}'


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)