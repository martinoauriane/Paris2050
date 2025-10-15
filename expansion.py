import pandas as pd
import geopandas as gpd

clc_2000 = gpd.read_file("CLC_2000_Paris.shp")
clc_2018 = gpd.read_file("CLC_2018_Paris.shp")
