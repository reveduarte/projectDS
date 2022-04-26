import flask
import pickle
import numpy 
import pandas as pd
import os
from datetime import datetime

fn = './model/modelmk06.pkl'
model_instance = pickle.load(open(fn,'rb'))

app = flask.Flask(__name__, template_folder='pages')

@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('home.html'))   
    if flask.request.method == 'POST':
        store = flask.request.form['store']
        dayOfWeek = flask.request.form['dayOfWeek']
        date = flask.request.form['date']
        customers = flask.request.form['customers']
        open = flask.request.form['open']
        promo = flask.request.form['promo']
        stateHoliday = flask.request.form['stateHoliday']
        schoolHoliday = flask.request.form['schoolHoliday']
        
        #preprocess date
        date_string = date
        dt = datetime.strptime(date_string, '%Y-%m-%d')
        
        month = dt.month
        year = dt.year
        day = dt.day
        # weekOfYear = dt.isocalendar().week

        input_variables = numpy.array([[ store,dayOfWeek,customers,open,promo,stateHoliday,schoolHoliday,month,year,day]])
        print(input_variables)
        array_inputs =  input_variables.astype(numpy.int)
        print(array_inputs)
        predictions = model_instance.predict(array_inputs)
        print("tttttttt" + str(predictions))
        
        predictions = str(predictions).strip('[]')
        # predictions = 1
        return flask.render_template('home.html',
                                     original_input={'store': store,
                                                     'dayOfWeek': dayOfWeek,
                                                     'date': date,
                                                     'customers': customers,
                                                     'open': open,
                                                     'promo': promo,
                                                     'stateHoliday': stateHoliday,
                                                     'schoolHoliday': schoolHoliday,
                                                     'month': month,
                                                     'year': year,
                                                     'day': day
                                                    #  'weekOfYear': weekOfYear
                                                     },result=str(predictions))
                                           
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)