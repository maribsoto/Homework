import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, join, outerjoin, MetaData, Table
from flask import Flask, jsonify, render_template


app = Flask(__name__)

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/index.html")
def welcome():

    return render_template("index.html")


@app.route("/fact_sheet.html")
def fact_sheet():

    return render_template("fact_sheet.html")

@app.route("/Pie_Chart.html")
def pie_chart():

    return render_template("Pie_Chart.html")


@app.route("/api/v1.0/metadata")
def metadata():

    path = (f"sqlite:///./astronauts.db")

    engine = create_engine(path)

    Base = automap_base()

    Base.prepare(engine, reflect=True)

    Metadata = Base.classes.metadata

    session = Session(engine)

    results = session.query(Metadata.Name, Metadata.Status, Metadata.Birth_Date, Metadata.Undergraduate_Major, Metadata.Graduate_Major, Metadata.Military_Rank, Metadata.Mission_One, Metadata.Mission_Two, Metadata.Mission_Three, Metadata.Mission_Four)

    df = pd.read_sql(results.statement, session.connection())

    session.close()

    return jsonify(df.to_dict(orient="records"))

@app.route("/api/v1.0/figures")
def figures():

    path = (f"sqlite:///./astronauts.db")

    engine = create_engine(path)

    Base = automap_base()

    Base.prepare(engine, reflect=True)

    Figures = Base.classes.figures

    session = Session(engine)

    results = session.query(Figures.Name, Figures.Space_Flights, Figures.Space_Flight_hr, Figures.Space_Walks, Figures.Space_Walks_hr)

    df = pd.read_sql(results.statement, session.connection())

    session.close()

    return jsonify(df.to_dict(orient="records"))

@app.route("/api/v1.0/branch")
def branch():

    path = (f"sqlite:///./astronauts.db")

    engine = create_engine(path)

    Base = automap_base()

    Base.prepare(engine, reflect=True)

    Branch = Base.classes.branch

    session = Session(engine)

    results = session.query(Branch.Name, Branch.Military_Branch)

    df = pd.read_sql(results.statement, session.connection())

    session.close()

    return jsonify(df.to_dict(orient="records"))


@app.route("/api/v1.0/gender")
def gender():

    path = (f"sqlite:///./astronauts.db")

    engine = create_engine(path)

    Base = automap_base()

    Base.prepare(engine, reflect=True)

    Gender = Base.classes.gender

    session = Session(engine)

    results = session.query(Gender.Name, Gender.Gender)

    df = pd.read_sql(results.statement, session.connection())

    session.close()

    return jsonify(df.to_dict(orient="records"))


@app.route("/api/v1.0/locations")
def location():

    path = (f"sqlite:///./astronauts.db")

    engine = create_engine(path)

    Base = automap_base()

    Base.prepare(engine, reflect=True)

    Location = Base.classes.locations

    session = Session(engine)

    results = session.query(Location.Name, Location.Birth_Place, Location.Birth_State, Location.Alma_Mater, Location.Mission_One)

    df = pd.read_sql(results.statement, session.connection())

    session.close()

    return jsonify(df.to_dict(orient="records"))


@app.route("/api/v1.0/bubble")
def bubble():

    path = (f"sqlite:///./astronauts.db")

    engine = create_engine(path)

    Base = automap_base()

    Base.prepare(engine, reflect=True)

    Bubble = Base.classes.bubble

    session = Session(engine)

    results = session.query(Bubble.Name, Bubble.Group_number, Bubble.Space_Flight_hr)

    df = pd.read_sql(results.statement, session.connection())

    session.close()

    return jsonify(df.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)


