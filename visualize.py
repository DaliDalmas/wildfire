import geopandas as gpd
import fiona
import os

current_directory = os.getcwd()

gdb_path = "data/wildfires/Wildfires_1878_2019_ContiguousUS_Wildfire_Rasters/FileGeodatabase/ContiguousUS_Wildfire_Rasters.gdb"

layers = fiona.listlayers(gdb_path)
print("Available layers:", layers)