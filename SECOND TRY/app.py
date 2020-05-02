import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template, request
from sqlalchemy import func

app = Flask(__name__)

#Clarence
# rds_connection_string = "postgres://postgres:Group1Washington@localhost:5432/postgres"
# engine = create_engine(rds_connection_string)

#Noaman
rds_connection_string = "postgres://NoamanJameel:Noamanj1919@localhost:5432/postgres"
engine = create_engine(rds_connection_string)

#Luke
# path_string = "postgres:postgres@localhost:5432/energy"
# engine = create_engine(f'postgresql+psycopg2://{path_string}')

#Erica
# path_string = "ericamatrese:Harrisburg1@localhost:5432/energy"
# engine = create_engine(f"postgresql://{path_string}")

#Jonathan
# rds_connection_string = "postgres://postgres:postgres@localhost:5432/test_db"
# engine = create_engine(rds_connection_string)

# Base = automap_base()
# Base.prepare(engine, reflect=True)

# energyData = Base.classes.energy_data
# incomeData = Base.classes.income_data
# populationData = Base.classes.population_data
# session = Session(engine)

@app.route('/')
def home():

    return render_template('index.html')

@app.route('/results')
def results():
    #build and execute map energy query
    energy_string ='select state_id, sum (generation_megawatthours) from energy_data where energy_type = \'Green Energy\' group by state_id'
    results_energy = pd.read_sql(energy_string, con=engine).rename(columns={'sum':'megawatthours'})
    
    # results_energy_paired = 
    # change dataframe obj to list of dictionaries
    map_dict = results_energy.to_dict('records')


    #  Green Vs Conventional Energy Graph By State

    green_str = 'select state_id, sum(generation_megawatthours) from energy_data WHERE energy_type = \'Green Energy\' Group By state_id'
    green = pd.read_sql(green_str, con=engine)
    conv_string = 'select state_id, sum(generation_megawatthours) from energy_data WHERE energy_type = \'Conventional\' Group By state_id'
    conventional = pd.read_sql(conv_string, con=engine)

    greenconv = pd.merge(green, conventional, on = "state_id").rename(columns={'sum_x':'Green_Energy','sum_y':'Conventional_Energy'})
    bar_dict = greenconv.to_dict('records')


    # Green VS Conv Over time

    green_conv_str = 'select year_energy, sum(generation_megawatthours)\
         from energy_data WHERE energy_type = \'Green Energy\' Group By year_energy, energy_type'
    green_conv_line = pd.read_sql(green_conv_str, con=engine)

    conv_str = 'select year_energy, sum(generation_megawatthours)\
         from energy_data WHERE energy_type = \'Conventional\' Group By year_energy, energy_type'
    conv_str_line = pd.read_sql(conv_str, con=engine)

    green_conv = pd.merge(green_conv_line, conv_str_line, on="year_energy").rename(columns={'sum_x':'Green_Energy','sum_y':'Conventional_Energy'})
    line_dict = green_conv.to_dict('records')

    #  Master Return Dict
    results_dict = {}
    results_dict['map'] = map_dict
    results_dict['bargraph'] = bar_dict
    results_dict['linegraph'] = line_dict

    return jsonify(results_dict)


if __name__ == '__main__':
    app.run(debug=True, port=8050)