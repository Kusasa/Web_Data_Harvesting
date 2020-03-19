"""------------------------------------------------------------------------------------------------------
Script Name:      StatsSA Population Groups Data Harvester
Version:          1.1
Description:      This tool harvests Stats SA Population Groups Data.
Created By:       Kusasalethu Sithole
Date:             2020-03-19
Revised by:       Kusasalethu Sithole
Last Revision:    2020-03-19
------------------------------------------------------------------------------------------------------"""

# Import modules
import geopandas as gpd
import requests
import tkinter as tk

#Funtion for data downloading and processing
def processor(working_directory):
    ws = working_directory.get()
    
    #Download data from statsa url
    params = (
        ('shape', 'za.geojson'),
    )
    
    response = requests.get('http://www.statssa.gov.za/wp-content/themes/umkhanyakude/mapajax.php', params=params)
    
    # Save geojson data on disk as a shapefile
    response_text = response.text
    json = gpd.read_file(response_text)
    json.to_file(ws + "/rsa_population_groups.shp")

# Tkinter Interactions
window = tk.Tk()
window.title("StatsSA Population Groups Data Harvester")
input_request = tk.Label(text="Working Directory: ")
input_wd = tk.Entry()
button = tk.Button(master=window,
    text="Run",
    command=processor(input_wd))
input_request.pack()
input_wd.pack()
button.pack()
window.mainloop()
