from flask import Flask
from flask import render_template
from flask import request

import requests
from api_model import DataCountry
from api import get_summary_covid_by_country

app = Flask(__name__)

@app.route('/')
@app.route('/<country>')
def hello_world(country=None):
    return render_template('/index.html',county=country)
    #return 'Hello, World!'

@app.route('/submit_data', methods=['POST'])
def submit_data():
    country = request.form['country']
    summary = get_summary_covid_by_country(country)
    list_data = []
    for item in summary:
        obj_data = DataCountry( item['ID'], 
                                item['Confirmed'],
                                item['Deaths'],
                                item['Recovered'],
                                item['Active'],
                                item['Date'])
        list_data.append(obj_data)
    return render_template('/index.html',country=list_data)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)