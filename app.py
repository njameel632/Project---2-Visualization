import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
from flask import render_template
from flask import request
from sqlalchemy import func



app = Flask(__name__)


app = Flask(__name__)

rds_connection_string = "postgres://NoamanJameel:Noamanj1919@localhost:5432/postgres"

engine = create_engine(rds_connection_string)

Base = automap_base()

Base.prepare(engine, reflect=True)

energyData = Base.classes.energy_data

incomeData = Base.classes.income_data

populationData = Base.classes.population_data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/energy')
def energy():

    return render_template('map.html')
    session = Session(engine)
    
    results_energy = session.query(energyData.year_energy, energyData.state_id, 
    energyData.type_of_producer, energyData.energy_source,energyData.generation_megawatthours,
    energyData.energy_type).all()
    
    qs = request.query_string
    print(qs)
    name = request.args.get('category').split(',')
    print(type(name))
    Group = request.args.get('Group')
    print(Group)

    energy_data = []

    for i in results_energy:
        energy_data.append(i)


    return jsonify(energy_data)

@app.route('/income')
def income():
 
    session = Session(engine)
 
    results_income = session.query(incomeData.year_income, incomeData.state_id, incomeData.median_income).\
    order_by(year_income, state_id).all()
    qs1 = request.query_string
    print(qs1)
    name1 = request.args.get('category').split(',')
    print(type(name1))
    Group = request.args.get('Group')
    print(Group)

    income_data = []

    for i in results_income:
        income_data.append(i)
       

    return jsonify(income_data)

@app.route('/population')
def population():

    session = Session(engine)
    results_population = session.query(populationData.year_population, 
    populationData.state_id, populationData.population).all()
    
    qs2 = request.query_string
    print(qs2)
    name = request.args.get('category').split(',')
    print(type(name))
    Group = request.args.get('Group')
    print(Group)
 
    population_data = []
 
    for i in results_population:
         population_data.append(i)
     
    return jsonify(population_data)

#Grouping Energy Sources Data. Energy produced By years and states
@app.route('/results')
def results():
 
    session = Session(engine)
    return jsonify(session.query(energyData.year_energy,energyData.state_id, energyData.energy_type,
    func.sum(energyData.generation_megawatthours)).\
    group_by(energyData.year_energy,energyData.state_id, energyData.energy_type).order_by(energyData.year_energy,
    energyData.state_id).all())

# @app.route('/incomefiltered')
# def incomefiltered():
# 
    # return jsonify(session.query(incomeData.year_income, incomeData.state_id, incomeData.median_income)).
    # 


if __name__ == '__main__':
    app.run(debug=True)
