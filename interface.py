from flask import Flask, request, render_template, jsonify
from utils import Urban_air_quality_and_health_risk_score, load_dataset
import config
from flask_cors import CORS



from flask import Flask, request, render_template, jsonify
from utills import Urban_air_quality_and_health_risk_score, load_dataset


df=load_dataset()
urban_air_and_hlt_rsk_scr=Urban_air_quality_and_health_risk_score()

app=Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return render_template('index_html')

@app.route("/preciptype_options")
def preciptype_options():
    urban_air_and_hlt_rsk_scr.load_data()
    return jsonify(list(urban_air_and_hlt_rsk_scr.load_data.column_data['preciptype'].keys()))

@app.route("/conditions_options")
def condition_options():
   return jsonify(list(df['condition'].unique()))

@app.route("/description_options")
def description_options():
    return jsonify(list(df['description'].unique()))

@app.route("/icon_options")
def icon_options():
    return jsonify(list(df['icon'].unique()))

@app.route("/stations_options")
def stations_options():
    return jsonify(list(df['station'].unique()))

@app.route("/source_options")
def source_options():
    return jsonify(list(df['source'].unique()))

@app.route("/City_conditions")
def City_conditions():
    return jsonify(list(df['City'].unique()))

@app.route("/Season_options")
def Season_options():
    return jsonify(list(df['Season'].keys()))


@app.route("/Day_of_Week_options")
def Day_of_Week_options():
    return jsonify(list(df['Day_of_Week'].unique()))

@app.route("/Is_Weekend_options")
def Is_Weekend_options():
    return jsonify(list(df['Is_Weekend'].keys()))

@app.route('/prediction', methods=['POST'])
def prediction():
    data=request.form
    print(data)


    datetime = data['datetime']
    monthtime=data['monthtime']
    yeartime=data['yeartime']
    datetimeEpoch  = data['datetimeEpoch']
    tempmax =data['tempmax']
    tempmin =data['tempmin']
    temp =data['temp']
    feelslikemax  =data['feelslikemax']
    feelslikemin  =data['feelslikemin']
    feelslike  =data['feelslike']
    dew  =data['dew']
    humidity =data['humidity']
    precip     =data['precip']
    precipprob  =data['precipprob']
    precipcover=data['precipcover']
    preciptype =data['preciptype']
    windgust  =data[' windgust']
    windspeed    =data['windspeed']
    winddir     =data['winddir']
    pressure   =data['pressure']
    cloudcover  =data['cloudcover']
    visibility   =data['visibility']
    solarradiation   =data['solarradiation']
    solarenergy    =data['solarenergy']
    uvindex     =data['uvindex']
    severerisk    =data['severerisk']
    sunrisehour=data['sunrisehour']
    sunriseminute=data['sunriseminute']
    sunrisecond=data['sunrisecond']
    sunriseEpoch  =data['sunriseEpoch']
    sunsethours=data['sunsethours']
    sunsetminutes=data['sunsetminutes']
    sunsetsecond=data['sunsetsecond']
    sunsetEpoch =data['sunsetEpoch']
    moonphase   =data['moonphase']
    conditions = data['conditions']
    description=data['description']
    icon    = data['icon']
    stations =data['stations']
    source =data['source']
    City     =data['City']
    Temp_Range    =data['Temp_Range']
    Heat_Index    =data['Heat_Index']
    Severity_Score =data['Severity_Score']
    Month  =data['Month']
    Season  =  data['Season']
    Day_of_Week= data['Day_of_Week']
    Is_Weekend  = data['Is_Weekend']


    pred_health_risk_score= urban_air_and_hlt_rsk_scr.predicted_health_risk_score (
                                    datetime,monthtime,yeartime,datetimeEpoch,tempmax,tempmin,temp,feelslikemax,
                                    feelslikemin,feelslike,dew,humidity,precip,precipprob,precipcover,preciptype,
                                    windgust,windspeed,winddir,pressure,cloudcover,visibility,solarradiation,solarenergy,
                                    uvindex,severerisk,sunrisehour,sunriseminute,sunrisecond,sunriseEpoch,sunsethours,sunsetminutes,
                                    sunsetsecond,sunsetEpoch,moonphase,conditions,description,icon,stations,source,City,Temp_Range,             
                                    Heat_Index,Severity_Score,Month,Season,Day_of_Week,Is_Weekend
                    )
    

    print(f"Predicted Health Risk Score:{pred_health_risk_score}")   #Debugging log
    return jsonify({'Predicted Health Risk Score':pred_health_risk_score})

