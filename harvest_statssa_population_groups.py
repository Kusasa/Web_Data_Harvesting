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
def main_screen():
    window = tk.Tk()
    window.title("StatsSA Population Groups Data Harvester")
    window.geometry("500x50")
    
    global input_wd
    input_wd = tk.StringVar()
    
    tk.Label(window, text="Please enter details below").pack()
    tk.Label(window, text="Working Directory: ").pack(side = tk.LEFT)
    tk.Entry(window, bd =5, width = 50, textvariable = input_wd).pack(side = tk.LEFT)
    tk.Button(text="Run",command = processor ).pack()
    window.mainloop()
    
main_screen()