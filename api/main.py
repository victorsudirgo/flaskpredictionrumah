from flask import Flask, redirect, url_for, render_template, request
import pickle
import numpy as np
import pandas as pd
import csv

app = Flask(__name__, template_folder='templates')

rf_model = open("api/RF_Model.pkl", "rb")
gb_model = open("api/GBoosting_Model.pkl", "rb")
ada_model = open("api/AdaBoost_Model.pkl", "rb")

#rf = pickle.load(rf_model)
#gb = pickle.load(gb_model)
#ada = pickle.load(ada_model)


@app.route("/test_link")
def test_link():
    return render_template('test_link.html')

@app.route('/methods', methods=['GET', 'POST'])
def methods():
    return render_template('methods.html')

@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('home'))
    
    data = pd.read_csv('clean_lamudi_tangsel.csv')
    datacsv = data.to_dict('records')
    results = []
    for row in datacsv:
        results.append(dict(row))
    
    print(results)
    return render_template('homepage.html', results=results)

    # show the form, it wasn't submitted
    #return render_template('homepage.html')

@app.route("/", methods=['GET', 'POST'])
def home():
    area_arr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    if request.method == 'GET':
        return (render_template('index.html'))
    
    if request.method == 'POST':
        lt = float(request.form['lt'])
        lb = float(request.form['lb'])
        kt = float(request.form['kt'])
        km = float(request.form['km'])
        carspaces = float(request.form['carspaces'])
        multiple_floor = request.form['multiple_floor']
        security = request.form['security']
        garden = request.form['garden']
        courtyard = request.form['courtyard']
        balcony = request.form['balcony']

        if multiple_floor == "Yes":
            multiple_floor = 1
        else :
            multiple_floor = 0

        
        if security == "Yes":
            security = 1
        else :
            security = 0
        
        
        if garden == "Yes":
            garden = 1
        else :
            garden = 0

        if courtyard == "Yes":
            courtyard = 1
        else :
            courtyard = 0

        if balcony == "Yes":
            balcony = 1
        else :
            balcony = 0

        area = request.form['area']
        if area == "Alam Sutera":
            area_arr[0] = 1
        elif area == "Bambu Apus":
            area_arr[1] = 1
        elif area == "Bintaro":
            area_arr[2] = 1
        elif area == "Bumi Serpong Damai":
            area_arr[3] = 1
        elif area == "Ciputat":
            area_arr[4] = 1
        elif area == "Cirendeu":
            area_arr[5] = 1
        elif area == "Daerah Lainnya":
            area_arr[6] = 1
        elif area == "Jombang":
            area_arr[7] = 1
        elif area == "Kedaung":
            area_arr[8] = 1
        elif area == "Pamulang":
            area_arr[9] = 1
        elif area == "Pamulang Barat":
            area_arr[10] = 1
        elif area == "Pamulang Timur":
            area_arr[11] = 1
        elif area == "Pondok Aren":
            area_arr[12] = 1
        elif area == "Pondok Benda Baru":
            area_arr[13] = 1
        elif area == "Pondok Benda Lama":
            area_arr[14] = 1
        elif area == "Pondok Cabe":
            area_arr[15] = 1
        elif area == "Pondok Cabe Ilir":
            area_arr[16] = 1
        elif area == "Pondok Cabe Udik":
            area_arr[17] = 1
        elif area == "Rawa Buntu":
            area_arr[18] = 1
        elif area == "Rempoa":
            area_arr[19] = 1
        elif area == "Sarua":
            area_arr[20] = 1
        elif area == "Sarua Indah":
            area_arr[21] = 1
        elif area == "Sawah Baru":
            area_arr[22] = 1
        elif area == "Sawah Lama":
            area_arr[23] = 1
        elif area == "Serpong":
            area_arr[24] = 1
        elif area == "Serpong Utara":
            area_arr[25] = 1
        elif area == "Setu":
            area_arr[26] = 1

        

    input = pd.DataFrame([[kt,km,carspaces,lt,lb,multiple_floor,security,garden,balcony,courtyard, area_arr[0], 
                           area_arr[1], area_arr[2], area_arr[3], area_arr[4],
                           area_arr[5], area_arr[6], area_arr[7], area_arr[8],
                           area_arr[9], area_arr[10], area_arr[11], area_arr[12],
                           area_arr[13], area_arr[14], area_arr[15], area_arr[16],
                           area_arr[17], area_arr[18], area_arr[19], area_arr[20],
                           area_arr[21], area_arr[22], area_arr[23], area_arr[24],
                           area_arr[25], area_arr[26]]], 
                           columns=['bedrooms', 'bathrooms', 'car_spaces', 'land_size', 'building_size',
                            'multiple_floor', 'issecurity', 'isgarden', 'isbalcony', 'iscourtyard',
                            'daerah_Alam Sutera', 'daerah_Bambu Apus', 'daerah_Bintaro',
                            'daerah_Bumi Serpong Damai', 'daerah_Ciputat', 'daerah_Cirendeu',
                            'daerah_Daerah Lainnya', 'daerah_Jombang', 'daerah_Kedaung',
                            'daerah_Pamulang', 'daerah_Pamulang Barat', 'daerah_Pamulang Timur',
                            'daerah_Pondok Aren', 'daerah_Pondok Benda Baru',
                            'daerah_Pondok Benda Lama', 'daerah_Pondok Cabe',
                            'daerah_Pondok Cabe Ilir', 'daerah_Pondok Cabe Udik',
                            'daerah_Rawa Buntu', 'daerah_Rempoa', 'daerah_Sarua',
                            'daerah_Sarua Indah', 'daerah_Sawah Baru', 'daerah_Sawah Lama',
                            'daerah_Serpong', 'daerah_Serpong Utara', 'daerah_Setu'],
                            )
    
    algorithm = request.form['algorithm']
    if(algorithm == 'Random Forest'):
        pred = int(model.predict(input)[0])
        algo = 'Random Forest'
    elif(algorithm == 'AdaBoost'):
        pred = int(ada.predict(input)[0])
        algo = 'AdaBoost'
    else:
        pred = int(gb.predict(input)[0])
        algo = 'Gradient Boosting'
    #score = int(model.score)

    print(pred)    
    
    return render_template('hasil.html', original_input={'Kamar Tidur': kt, 'Kamar Mandi': km, 'Luas Tanah': lt,
                                                          'Luas Bangunan': lb, 'Garasi': carspaces, 'Lokasi':area, 
                                                          'Methods' :algo},
                                     result=pred)
if __name__=="__main__":
    app.run(debug=True)
