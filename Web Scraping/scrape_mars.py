#!/usr/bin/env python
# coding: utf-8

# # Mission to Mars
#
#     In the Web Scraping Homework, we are building a web application that scrapes various websites for data
#     related to the Mission to Mars and displays the information in a single HTML page
#
# #### Note: Please bear in mind that all cells were originally ran on Apr 29, 2020. It seems one process did not run correctly @ JPL exercise. So, I reran the nb on May 1st.

# ## Step 1 - Scraping
#     - We are using this notebook to complete all scraping and analysis tasks

# ### Dependencies
#     These are the dependencies required to run this notebook

# In[1]:


import pandas as pd
import time
import requests
from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver


def scrape_all():

    # Initiating headless driver for deployment
    browser = Browser('chrome', headless=False)
    executable_path = {
        'executable_path': '/c/Users/marib/OneDrive/Documents/Data Analytics/Programs/chromedriver'}


    # Running all scraping functions and storing in a dictionary
    mars_data = {
        "latest_news": latest_title,
        "latest_paragraph": latest_text,
        "featured_image": featured_image_url(browser),
        "hemispheres": hemisphere_image_urls(browser),
    }

# ## NASA Mars News

#     - Scraping the NASA Mars News Site and collecting the latest News Title and Paragraph Text.
#     - Assign the text to variables, so they can be referenced later.

# #### Locating and activating Chromedriver and its executable path

# In[2]:


# In[3]:

    executable_path = {
        'executable_path': '/c/Users/marib/OneDrive/Documents/Data Analytics/Programs/chromedriver'}


# In[4]:

    browser = Browser('chrome', headless=False)


#     - Defining the browser, url and html

# In[5]:

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)


# #### Finding the latest title and paragraph text

# In[6]:

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

# Finding the location @html of latest title
    latest_title = soup.find('div', class_='bottom_gradient').find('h3').text
# print('\n')
    print(latest_title)


# In[7]:


# Finding the location @html of latest paragraph
    latest_text = soup.find('div', class_='article_teaser_body')

    browser.quit()
    print(latest_text.text)


# ### JPL Mars Space Images
#
#     Visiting the url for JPL Featured Space Image, navigating the site and finding the full size image url for the current Featured Mars Image and assigning the url string to a variable -featured_image_url.

#     Activating chromedriver, browser and visiting the url

# In[8]:

    executable_path = {
        'executable_path': '/c/Users/marib/OneDrive/Documents/Data Analytics/Programs/chromedriver'}
    browser = Browser('chrome', headless=False)
    url = "https://www.jpl.nasa.gov/spaceimages/"
    browser.visit(url)
    time.sleep(1)


# In[9]:

    full_image = browser.find_by_id('full_image')

    full_image.click()


# In[10]:

    more_info = browser.links.find_by_partial_text('more info')

    more_info.click()


# In[11]:

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


# In[12]:

    image = soup.select_one('figure.lede a img').get('src')
    featured_image_url = url + image

    browser.quit()
    print(featured_image_url)


# ## Mars Weather

# In[13]:

    executable_path = {
        'executable_path': '/c/Users/marib/OneDrive/Documents/Data Analytics/Programs/chromedriver'}
    browser = Browser('chrome', headless=False)
    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    time.sleep(1)


# In[14]:

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


# In[15]:

    x_path = "/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div/div/div/div[2]/section/div/div/div[1]/div/div/div/div/article/div/div[2]/div[2]/div[2]/div[1]/div/span"

    if browser.is_element_present_by_xpath(x_path, wait_time=5):
        twit = browser.find_by_xpath(x_path).text

    browser.quit()


    print(twit)


# ## Mars Fact

# In[16]:


    url = 'https://space-facts.com/mars/'
    mars = pd.read_html(url)[0]
    mars


# In[17]:


    mars_fact = pd.DataFrame(mars)
    mars_fact.columns = mars_fact.columns.astype(str)
    mars_fact.columns = ['Parameters', 'Values']
    mars_fact


# In[18]:


    mars_html = mars_fact.to_html(header=False, index=False)
    print(mars_html)


# ## Mars Hemispheres

# In[19]:


    executable_path = {
        'executable_path': '/c/Users/marib/OneDrive/Documents/Data Analytics/Programs/chromedriver'}
    browser = Browser('chrome', headless=False)
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    time.sleep(1)


# In[20]:


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


#     Defining my lists:

# In[21]:


    hemisphere_image_urls = []  # final list

    title = []  # where we save the hemisphere titles
    img_url = []  # where we save the full image urls


#     Extracting the Hemisphere titles:

# In[22]:


    print(soup.prettify())


#     Browsing through the webpage to extract the hemisphere titles and the urls of the full images. The results defined as dictionaries are appended to the main list - hemisphere_image_urls

# In[23]:


    for item in range(4):
        time.sleep(5)

    # Clicking the title to get to the original hires image (.tif)
        img = browser.find_by_tag('h3')[item].click()

    # Finding the hemisphere full image url
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        src = soup.find("img", class_="wide-image")["src"]
        img_url = 'https://astrogeology.usgs.gov' + src

    # Finding the hemisphere image titles
        title = soup.find('div', class_='description').find('h3').text

    # Creating the dictionary where we're storing the variables
        hemisphere = {"title": title, "img_url": img_url}

    # Appending our dictionary to our main list - hemisphere_image_url
        hemisphere_image_urls.append(hemisphere)

        browser.back()

        return mars_data
