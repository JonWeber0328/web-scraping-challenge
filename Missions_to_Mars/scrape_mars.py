import time
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://redplanetscience.com/'
    browser.visit(url)

    listings = {}

    # Iterate through most recent news articles
    for x in range(1):
    
        # HTML object
        html = browser.html
        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')
        # Retrieve all elements that contain title and paragraph text information
        list_text = soup.find_all('div', class_='list_text')

        # Iterate through each list text
        for list_ in list_text:
            # Use Beautiful Soup's find() method to navigate and retrieve attributes
        
            title = list_.find("div", {"class": "content_title"}).get_text()
            paragraph = list_.find("div", {"class": "article_teaser_body"}).get_text()
            time.sleep(1)
            break
    listings["article_title"] = title
    listings["paragraph"] = paragraph
    browser.quit()
    # -------------------------------------------------------
    url2 = 'https://spaceimages-mars.com'
    browser.visit(url2)

    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve elements that contain image header information
    images = soup.find('img', class_='headerimage')

    # Assign the url string to a variable called featured_image_url
    featured_image_url = ['https://spaceimages-mars.com/' + (images['src'])][0]

    listings["featured_image_url"] = featured_image_url
    browser.quit()
    # -------------------------------------------------------
    url3 = 'https://galaxyfacts-mars.com/'
    browser.visit(url3)

    # Read all tables using pandas
    tables = pd.read_html(url3)

    # Select needed table and create a dataframe
    df = tables[0]

    # Change column names
    df.columns = ['Description', 'Mars', 'Earth']

    # Generate HTML table string 
    html_table = df.to_html()

    # Replace unwanted newlines to clean up the table
    html_table = html_table.replace('\n', '')

    listings["html_table"] = html_table
    browser.quit()
    # -------------------------------------------------------
    url4 = 'https://marshemispheres.com/'
    browser.visit(url4)

    # HTML object
    html2 = browser.html
    # Parse HTML with Beautiful Soup
    soup2 = BeautifulSoup(html2, 'html.parser')
    # Retrieve all elements that contain href link to needed photos
    divs = soup2.find_all('div', class_='item')

    # Create a variable to add a list of href's
    href_list = []

    # Iterate through each div item
    for div in divs:
        
        # Use Beautiful Soup's find() method to navigate and retrieve href's
        a = div.find('a')
        href = a['href']
        href_list.append(href)
    
    # Use href_list to scrape hemisphere pages 
    all_titles = []
    all_src = []
    for x in href_list:
    
        urlH = f'{url4}{x}'
        browser.visit(urlH)
    
        # HTML object
        html3 = browser.html
        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html3, 'html.parser')
        # Retrieve all elements that contain image and title information
        anchors = soup.find_all('img', class_='wide-image')
        titles = soup.find_all('h2', class_='title')
        time.sleep(1)
    
        # Iterate through each title
        for ti in titles:
            # Use Beautiful Soup's find() method to navigate and retrieve attributes
            title2 = ti.get_text()
            all_titles.append(title2)
            time.sleep(1)
                
        # Iterate through each anchor
        for anchor in anchors:
            # Use Beautiful Soup's find() method to navigate and retrieve attributes
            src = anchor['src']
            img_url = base_url + src
            all_src.append(img_url)
            time.sleep(1)

    # Create a dictionary using title and img_url lists
    hemisphere_image_urls = []
    for i, j in zip(all_titles, all_src):
        hemisphere_image_urls.append({"title": i, "img_url": j})
    listings["hemisphere_image_urls"] = hemisphere_image_urls

    browser.quit()

    return listings
# -------------------------------------------------------
# -------------------------------------------------------
# -------------------------------------------------------
