"""------------------------------------------------------------------------------------------------------
Script Name:      AfriGIS Weather Data Harvester
Version:          1.1
Description:      This tool harvests AfriGIS Weather Data and extracts the necessary values.
Created By:       Kusasalethu Sithole
Date:             2020-04-08
Revised by:       Kusasalethu Sithole
Last Revision:    2020-04-08
------------------------------------------------------------------------------------------------------"""

def location_weather (key, coordinates):
    global distance, synop_no,datetime, station_name, temperature, humidity, pressure, wind_direction, wind_speed, last_hours_rainfall
    
    #Import modules
    import requests
    import json
    
    #Method parameters
    params = (
        ('location', coordinates),           #location center
        ('location_buffer', '10000'),        #search radius in metres for weather stations
        ('station_count', '1'),              #search count in metres for weather stations
    )
    
    #Make api call
    response = requests.get('https://saas.afrigis.co.za/rest/2/weather.measurements.getByCoord/' + key + '/trial/', params=params)
    weather_json = response.text
    
    #Ingest into json object and extract values
    weather_dict = json.loads(weather_json)
    distance = weather_dict['result'][0]['station_details']['distance']
    synop_no = weather_dict['result'][0]['station_details']['synop_no']
    station_name = weather_dict['result'][0]['station_details']['station_name']
    datetime = weather_dict['result'][0]['station_readings'][0]['datetime']
    temperature = weather_dict['result'][0]['station_readings'][0]['temperature']
    humidity = weather_dict['result'][0]['station_readings'][0]['humidity']
    pressure = weather_dict['result'][0]['station_readings'][0]['temperature']
    wind_direction = weather_dict['result'][0]['station_readings'][0]['wind_direction']
    wind_speed = weather_dict['result'][0]['station_readings'][0]['wind_speed']
    last_hours_rainfall = weather_dict['result'][0]['station_readings'][0]['last_hours_rainfall']