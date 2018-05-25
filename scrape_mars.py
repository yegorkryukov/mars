def scrape1():
    return {'result':'test function works'}


def scrape():
    # Dependencies
    from bs4 import BeautifulSoup
    from splinter import Browser
    import pandas as pd

    #setup resulting dict
    results = {}

    #--------------------------------------------
    # SCRAPE LATEST NEWS
    #--------------------------------------------

    # https://splinter.readthedocs.io/en/latest/drivers/chrome.html
    get_ipython().system('which chromedriver')

    # have to run browser object
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    # URL of NASA's mars news
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

    # launch browser
    browser.visit(url)

    # create beautifulsoup object
    soup = BeautifulSoup(browser.html, 'html.parser')

    # find latest news date, title and body (first appearanse of a tag in html)
    news_date = soup.find('div', class_='list_date').text
    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text

    # save to results
    results['news_date']  = news_date
    results['news_title'] = news_title
    results['news_p']     = news_p


    #--------------------------------------------
    # SCRAPE FEATURED IMAGE
    #--------------------------------------------

    # URL of mars images page
    url = 'https://www.jpl.nasa.gov/'
    url1 = 'spaceimages/?search=&category=Mars'

    # launch browser
    browser.visit(url+url1)

    # create beautifulsoup object
    soup = BeautifulSoup(browser.html, 'html.parser')

    # remove last '/' symbol from url
    # locate the 'style' attribute of 'article' tag
    # split by quotes and access an element of resulting list
    # combine the two text elements get the image url
    featured_image_url = url[:-1] + soup.find('article', class_='carousel_item')['style'].split("'")[1]
    results['featured_image_url'] = featured_image_url


    #--------------------------------------------
    # SCRAPE MARS'S WEATHER
    #--------------------------------------------

    # twitter url to visit
    url = 'https://twitter.com/marswxreport?lang=en'

    # launch browser
    browser.visit(url)

    # create beautifulsoup object
    soup = BeautifulSoup(browser.html, 'html.parser')

    # localate the first tweet and extract text from it
    mars_weather = soup.find('div', class_='js-tweet-text-container').text.split('\n')[1]
    results['mars_weather'] = mars_weather


    #--------------------------------------------
    # SCRAPE MARS'S FACTS
    #--------------------------------------------

    # url to visit
    url = 'http://space-facts.com/mars/'

    # use pandas to extract table from the page
    facts_table = pd.read_html(url)

    # create df with columns' headers
    df = facts_table[0]
    df.columns = ['Parameter','Value']

    # convert to html table
    facts_table = df.to_html()

    results['facts_table'] = facts_table


    #--------------------------------------------
    # SCRAPE HEMISPHERES' IMAGES
    #--------------------------------------------

    # url to visit
    url = 'https://astrogeology.usgs.gov'
    url1 = '/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    # launch browser
    browser.visit(url+url1)

    # create beautifulsoup object
    soup = BeautifulSoup(browser.html, 'html.parser')

    # find section with images on the page
    div = soup.find('div', class_='results').findAll('div', class_='description')

    # extract urls
    urls = []
    for item in div:
        links = item.findAll('a')
        for a in links:
            urls.append(a.get('href'))

    # visit urls to extract links and titles
    hemisphere_image_urls = []
    for u in urls:
        result_dict = {}
        browser.visit(url+u)
        soup = BeautifulSoup(browser.html, 'html.parser')

        # find and extract links to images
        links = soup.find('div', class_='downloads').findAll('a')
        result_dict['img_url_jpeg'] = links[0].get('href')
        result_dict['img_url'] = links[1].get('href')

        # extract title
        result_dict['title'] = soup.find('h2', class_='title').text

        # append dict to results list
        hemisphere_image_urls.append(result_dict)

    results['hemisphere_image_urls'] = hemisphere_image_urls
    
    return results

