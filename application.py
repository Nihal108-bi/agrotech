from flask import Flask,request,render_template,jsonify
from src.pipelines.prediction_pipeline import CustomData,PredictPipeline
from src.logger import logging


application=Flask(__name__)

app=application

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])

def predict_datapoint():
    if request.method == 'GET':
        return render_template('form.html')
    
    else:
        try:
            temperature_celsius = float(request.form.get('temperature_celsius') or 0)
            humidity = float(request.form.get('humidity') or 0)
            wind_mph = float(request.form.get('wind_mph') or 0)
            wind_degree = float(request.form.get('wind_degree') or 0)
            pressure_mb = float(request.form.get('pressure_mb') or 0)
            uv_index = float(request.form.get('uv_index') or 0)
            visibility_km = float(request.form.get('visibility_km') or 0)
            gust_kph = float(request.form.get('gust_kph') or 0)
            cloud = float(request.form.get('cloud') or 0)
            wind_kph = float(request.form.get('wind_kph') or 0)
            pressure_in = float(request.form.get('pressure_in') or 0)
            feels_like_celsius = float(request.form.get('feels_like_celsius') or 0)
            feels_like_fahrenheit= float(request.form.get('feels_like_fahrenheit') or 0)
            visibility_miles = float(request.form.get('visibility_miles') or 0)
            gust_mph= float(request.form.get('gust_mph') or 0)
            wind_direction = request.form.get('wind_direction', '')

            # Assuming CustomData is your data class
            data = CustomData(
                temperature_celsius=temperature_celsius,
                humidity=humidity,
                wind_mph=wind_mph,
                wind_degree=wind_degree,
                pressure_mb=pressure_mb,
                uv_index=uv_index,
                visibility_km=visibility_km,
                gust_kph=gust_kph,
                cloud=cloud,
                wind_kph=wind_kph,
                pressure_in=pressure_in,
                feels_like_celsius=feels_like_celsius,
                feels_like_fahrenheit=feels_like_fahrenheit,
                visibility_miles=visibility_miles,
                gust_mph=gust_mph,
                wind_direction=wind_direction,
            )

            final_new_data = data.get_data_as_dataframe()
            predict_pipeline = PredictPipeline()
            pred = predict_pipeline.predict(final_new_data)

            results = round(pred[0], 2)
            return render_template('form.html', final_result=results)

        except ValueError as ve:
            logging.error(f"ValueError: {ve}")
            return render_template('form.html', error="Invalid input. Please check your data.")
        except Exception as e:
            logging.error(f"Exception occurred: {e}")
            return render_template('form.html', error="An error occurred during prediction.")


if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)        