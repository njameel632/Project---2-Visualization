import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template, request
from sqlalchemy import func

app = Flask(__name__)

<<<<<<< HEAD
#Clarence
rds_connection_string = "postgres://postgres:Group1Washington@localhost:5432/postgres"
engine = create_engine(rds_connection_string)
=======
#Noaman
# rds_connection_string = "postgres://NoamanJameel:Noamanj1919@localhost:5432/postgres"
# engine = create_engine(rds_connection_string)
>>>>>>> 6ec76b02ad7c245a810ea7dc0e09e5127192d300

#Noaman
# rds_connection_string = "postgres://NoamanJameel:Noamanj1919@localhost:5432/postgres"
# engine = create_engine(rds_connection_string)

#Luke
path_string = "postgres:postgres@localhost:5432/energy"
engine = create_engine(f'postgresql+psycopg2://{path_string}')

#Erica
# path_string = "ericamatrese:Harrisburg1@localhost:5432/energy"
# engine = create_engine(f"postgresql://{path_string}")

#Clarence
# path_string = "postgres:PASSWORD@localhost:5432/energy"
# engine = create_engine(f'postgresql+psycopg2://{path_string}')

# Base = automap_base()
# Base.prepare(engine, reflect=True)

# energyData = Base.classes.energy_data
# incomeData = Base.classes.income_data
# populationData = Base.classes.population_data
# session = Session(engine)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map')
def map():
    return render_template('map.html')

# @app.route('/results', methods=['GET','POST'])
@app.route('/results')
def results():
    # year = request.args.get('year')
    # sources = request.args.get('sources').split(",")
    year=1990
    sources =['Wind','Coal']

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
    results_population = pd.read_sql(f'select state_id, population from population_data where year_population = {year}', con=engine)

    #join query results to return JSONIFY
    results = pd.merge(results_energy, results_population, on = "state_id")

    #change dataframe obj to list of dictionaries
    map_dict = results.to_dict('records')


    #  Green Vs Conventional Energy Graph By State

    green_str = 'select state_id, sum(generation_megawatthours) from energy_data WHERE energy_type = \'Green Energy\' Group By state_id'
    green = pd.read_sql(green_str, con=engine)
    conv_string = 'select state_id, sum(generation_megawatthours) from energy_data WHERE energy_type = \'Conventional\' Group By state_id'
    conventional = pd.read_sql(conv_string, con=engine)

    greenconv = pd.merge(green, conventional, on = "state_id").rename(columns={'sum_x':'Green Energy','sum_y':'Conventional Energy'})
    greenconv_dict = results_energy.to_dict('records')


    # Green VS Conv Over time

    green_conv_str = 'select year_energy, sum(generation_megawatthours)\
         from energy_data WHERE energy_type = \'Green Energy\' Group By year_energy, energy_type'
    green_conv_line = pd.read_sql(green_conv_str, con=engine)

    conv_str = 'select year_energy, sum(generation_megawatthours)\
         from energy_data WHERE energy_type = \'Conventional\' Group By year_energy, energy_type'
    conv_str_line = pd.read_sql(conv_str, con=engine)

    green_conv = pd.merge(green_conv_line, conv_str_line, on="year_energy").rename(columns={'sum_x':'Green Energy','sum_y':'Conventional'})
    green_conventional_dict = green_conv.to_dict('records')

    #  Master Return Dict
    results_dict = {}
    results_dict['map'] = map_dict
    results_dict['bargraph'] = greenconv_dict
    results_dict['linegraph'] = green_conventional_dict

    return jsonify(results_dict)

# @app.route('/income')
# def income(): 
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

# @app.route('/incomefiltered')
# def incomefiltered():
    # return jsonify(session.query(incomeData.year_income, incomeData.state_id, incomeData.median_income)).

if __name__ == '__main__':
<<<<<<< HEAD
    app.run(debug=True, port=8050)
=======
    app.run(debug=True)
>>>>>>> 6ec76b02ad7c245a810ea7dc0e09e5127192d300
