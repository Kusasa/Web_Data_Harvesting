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
#from tkinter import *

#Funtion for data downloading and processing
def processor():
    ws = input_wd.get()
    target_data = dropdown.get()
    
    #Data Options
    data_options = {
            "rsa_population_groups": ['http://www.statssa.gov.za/wp-content/themes/umkhanyakude/mapajax.php', '/rsa_population_groups.shp'],
            "two": ["url", "/file_name.shp"],
            "three": ["ur", "/file_name.shp"]
    }
    
    #Download data from statsa url
    params = (
        ('shape', 'za.geojson'),
    )
    
    response = requests.get(data_options[target_data][0], params=params)
    
    # Save geojson data on disk as a shapefile
    response_text = response.text
    json = gpd.read_file(response_text)
    json.to_file(ws + data_options[target_data][1])

# Tkinter Interactions
def main_screen():
    window = tk.Tk()
    window.title("StatsSA Population Groups Data Harvester")
    window.geometry("760x60")
    
    global input_wd, dropdown
    input_wd = tk.StringVar()
    dropdown = tk.StringVar()
    dropdown.set("rsa_population_groups") # default value
    
    tk.Label(window, text="Please enter details below").pack(side = tk.TOP)
    tk.Label(window, text="Working Directory: ").pack(side = tk.LEFT)
    tk.Entry(window, bd =5, width = 50, textvariable = input_wd).pack(side = tk.LEFT)
    tk.Label(window, text="Target Data: ").pack(side = tk.LEFT)
    tk.OptionMenu(window, dropdown, "rsa_population_groups", "two", "three").pack(side = tk.LEFT)
    tk.Button(text="Run",command = processor, width=10).pack(side = tk.RIGHT)
    window.mainloop()
    
main_screen()