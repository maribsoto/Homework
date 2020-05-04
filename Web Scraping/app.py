# Import necessary libraries
from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo

# Python Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver
from scrape_mars import scrape_all

#################################################
# Database and Flask Setup
#################################################

# create instance of Flask app
app = Flask(__name__)

#app.config['MONGO_URI'] = "mongodb://localhost:27017/mars_db"
#mongo = PyMongo(app)

# Create route that renders index.html template
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/scrape')
def scrape():
    mars_data = scrape_all()
    return mars_data


if __name__ == '__main__':
    app.run(debug=True)
