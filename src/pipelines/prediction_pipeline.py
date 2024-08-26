import sys
import os
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object
import pandas as pd

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model_path=os.path.join('artifacts','model.pkl')

            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)

            data_scaled=preprocessor.transform(features)
            pred=model.predict(data_scaled)
            return pred
            
        except Exception as e:
            logging.info("Exception occured in prediction")
            raise CustomException(e,sys)
        
class CustomData:
    def __init__(self,
                 temperature_celsius:float,
                 humidity:float,
                 wind_mph:float,
                 wind_degree:float,
                 wind_direction:str,
                 pressure_mb:float,
                 cloud:float,
                 visibility_km:float,
                 uv_index:float,
                 gust_kph:float,
                 # Add missing fields with default values if necessary
                #  wind_kph: float = 0.0,
                #  pressure_in: float = 0.0,
                #  feels_like_celsius: float = 0.0,
                #  feels_like_fahrenheit: float = 0.0,
                #  visibility_miles: float = 0.0,
                #  gust_mph: float = 0.0 ):
        
                 wind_kph: float ,
                 pressure_in: float ,
                 feels_like_celsius: float ,
                 feels_like_fahrenheit: float,
                 visibility_miles: float ,
                 gust_mph: float ):

        
        self.temperature_celsius=temperature_celsius
        self.humidity=humidity
        self.wind_mph=wind_mph
        self.wind_degree=wind_degree
        self.wind_direction=wind_direction
        self.pressure_mb=pressure_mb
        self.cloud=cloud
        self.visibility_km=visibility_km
        self.uv_index=uv_index
        self.gust_kph=gust_kph
        #deafult value
        self.wind_kph = wind_kph
        self.pressure_in = pressure_in
        self.feels_like_celsius = feels_like_celsius
        self.feels_like_fahrenheit = feels_like_fahrenheit
        self.visibility_miles = visibility_miles
        self.gust_mph = gust_mph        
        

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'temperature_celsius':[self.temperature_celsius],
                'humidity':[self.humidity],
                'wind_mph':[self.wind_mph],
                'wind_degree':[self.wind_degree],
                'wind_direction':[self.wind_direction],
                'pressure_mb':[self.pressure_mb],
                'cloud':[self.cloud],
                'visibility_km':[self.visibility_km],
                'uv_index':[self.uv_index],
                'gust_kph':[self.gust_kph],
                #defalut value
                'wind_kph': [self.wind_kph],
                'pressure_in': [self.pressure_in],
                'feels_like_celsius': [self.feels_like_celsius],
                'feels_like_fahrenheit': [self.feels_like_fahrenheit],
                'visibility_miles': [self.visibility_miles],
                'gust_mph': [self.gust_mph]                
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise CustomException(e,sys)