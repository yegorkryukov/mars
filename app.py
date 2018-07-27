from flask import Flask, render_template, redirect
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
def index(rerender=False):
    data = collection.find_one()
    print(f'Data: {data["news_date"]}')
    #extract table html from string
    table = data['facts_table']
    #replace class and other style params to pickup bootstrap
    table = table.replace('dataframe','table').replace('style="text-align: right;','style="text-align: center;')
    #print(type(data.facts_table))
    return render_template("index.html", data=data, table=table, rerender=rerender)

@app.route('/scrape')
def do_scrape(): 
    # Launch function to scrape data
    results = scrape()

    # Delete all documents inside a collection
    collection.remove({})

    # Insert newly obtained data into the db
    collection.insert_one(results)
    return index(True) #redirect("/", code=302)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)