# Mission to Mars

Built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. Each time the page is visited, here is what's happening:

## 1. Scraping

Using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

### NASA Mars News

* Scrapes the [NASA Mars News Site](https://mars.nasa.gov/news/) and collects the latest News Title and Paragragh Text. 

### JPL Mars Space Images - Featured Image

* Visits the url for JPL's Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).

* Uses splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.

### Mars Weather

* Visits the Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en) and scrapes the latest Mars weather tweet from the page. Saves the tweet text for the weather report as a variable called `mars_weather`.

### Mars Facts

* Visits the Mars Facts webpage [here](http://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

* Use Pandas to convert the data to a HTML table string.

### Mars Hemisperes

* Visits the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

* Saves both the image url string for the full resolution hemipshere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.
---

## 2. MongoDB and Flask Application

Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.
