import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template, request
from sqlalchemy import func

app = Flask(__name__)

rds_connection_string = "postgres://NoamanJameel:Noamanj1919@localhost:5432/postgres"

engine = create_engine(rds_connection_string)
Base = automap_base()
Base.prepare(engine, reflect=True)

energyData = Base.classes.energy_data
incomeData = Base.classes.income_data
populationData = Base.classes.population_data
session = Session(engine)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/results')
def results():
    year = request.args.get('year')
    sources = request.args.get('sources').split(",")

    #clean input_sources
    def clean(list):
        # sources=[]
        # for i in input_sources:
        #     if i == 'Green Energy':
        #         sources.append('Geothermal','Pumped Storage','Solar Thermal and Photovoltaic','Nuclear','Hydroelectric Conventional')
        #     elif i == 'Conventional Energy':
        #         sources.append('Natural Gas','Petroleum''Coal','Other Biomass','Wood and Wood Derived Fuels','Other Gases')
        #     else:
        #         for x in sources:
        #             if i = x:
        #                 break
        #         sources.append(i)

    #build and execute energy query
    in_string = ""
    query_string =f'select state_id, sum (generation_megawatthours) from energy_data where energy_source in ('

    for i in sources: #creates string of sources for SQL query
        if i == sources[0]:
            in_string += f'\'{i}\''
            continue
        in_string += f',\'{i}\''

    query_string += in_string+f') and year_energy = {year} group by state_id'
    
    results_energy = pd.read_sql(query_string, con=engine).rename(columns={'sum':'megawatthours'})

    #execute population query
    results_population = pd.read_sql(f'select state_id, population from population_data where year_population = {year}')

    #join query results to return JSONIFY
    results = pd.merge(results_energy, results_population, on = "state_id")

    #change dataframe obj to list of dictionaries.
    results_list = []
    for result in results:
        row = {}
        row["state_id"] = result[0]
        row["megawatthours"] = result[1]
        row['population'] = result[2]
        results_list.append(row)

    # session.query(populationData.year_population, 
    # populationData.state_id, populationData.population).all()

    # results_energy = session.query(energyData.year_energy, energyData.state_id, 
    # energyData.type_of_producer, energyData.energy_source,energyData.generation_megawatthours,
    # energyData.energy_type).all()
    
    # qs = request.query_string
    # print(qs)
    # name = request.args.get('category').split(',')
    # print(type(name))
    # Group = request.args.get('Group')
    # print(Group)

    # energy_data = []

    # for i in results_energy:
    #     energy_data.append(i)


    return jsonify(results_list)

@app.route('/income')
def income(): 
    # results_income = session.query(incomeData.year_income, incomeData.state_id, incomeData.median_income).\
    # order_by(year_income, state_id).all()
    # qs1 = request.query_string
    # print(qs1)
    # name1 = request.args.get('category').split(',')
    # print(type(name1))
    # Group = request.args.get('Group')
    # print(Group)

    # income_data = []

    # for i in results_income:
    #     income_data.append(i)
       

    # return jsonify(income_data)

@app.route('/population')
def population():
    # results_population = session.query(populationData.year_population, 
    # populationData.state_id, populationData.population).all()
    
    # # qs2 = request.query_string
    # # print(qs2)
    # # name = request.args.get('category').split(',')
    # # print(type(name))
    # # Group = request.args.get('Group')
    # # print(Group)
 
    # population_data = []
 
    # for i in results_population:
    #      population_data.append(i)
     
    # return jsonify(population_data)

#Grouping Energy Sources Data. Energy produced By years and states
@app.route('/results')
def results():
    return jsonify(session.query(energyData.year_energy,energyData.state_id, energyData.energy_type,
    func.sum(energyData.generation_megawatthours)).\
    group_by(energyData.year_energy,energyData.state_id, energyData.energy_type).order_by(energyData.year_energy,
    energyData.state_id).all())

@app.route('/incomefiltered')
def incomefiltered():
    # return jsonify(session.query(incomeData.year_income, incomeData.state_id, incomeData.median_income)).
    # 


if __name__ == '__main__':
    app.run(debug=True)
