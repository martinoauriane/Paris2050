import pandas as pd
import geopandas as gpd
from sklearn.linear_model import LinearRegression
import numpy as np

## urbanized data for France : year 2000 and year 2018 
clc_2000 = gpd.read_file("CLC_2000_Paris.shp")
clc_2018 = gpd.read_file("CLC_2018_Paris.shp")

## Population estimation in Paris - INSEE
population_data = {
    'Year': [2000, 2006, 2012, 2018],
    'Population': [2129731, 2187526, 2240621, 2175601]
}

def urbanized_surface(clc):
  urbanized_area = clc[clc['CLC_CODE'].isin([111, 112, 121, 122, 123, 124, 131, 132, 133, 141, 142, 143, 151, 152, 153, 154])]
  total = urbanized_area.geometry.area.sum()
  return total

surface_2000 = urbanized_surface(clc_2000)
surface_2018 = urbanized_surface(clc_2018)

## Creating a data frame whose goal is to centralize all corresponding data.
## - The year 2000 had approximatively surface_2000 amount of urbanized land, for appromatively 2 129 731 people.
## - The year 2018 had approximatively surface_2018 amount of urbanized land, for appromatively 2 175 601 people.

paris_data = pd.DataFrame({
    'Year': [2000, 2018],
    'Urban_surface': [surface_2000, surface_2018],
    'Population': [2129731, 2175601]
})

## Now let's add a new category. This category will record the urban density for each year, dividing the year approximate recorded population 
## by the year recorded approximate urbanized surface.
paris_data['Densité_urbaine'] = paris_data['Population'] / paris_data['Urban_surface']

## Now let's use Linear Regression to determine the quantity of urbanized land for an unknown variable, X, using a known quantity
## of urbanized land, Y. 
x = paris_data['Year'].values.reshape(-1, -1)
y_surface = paris_data['Urban_surface'].values #prepping data to train linear regression model
y_population = paris_data['Population'].values

## creating two separated linear regression models: one for Paris surface, another for Paris population
linear_regression_model_surface = LinearRegression().fit(x, y_surface)
linear_regression_model_surface = LinearRegression().fit(x, y_population)
## We obtain two models able to make predictions for the year 2050.

surface_2050 = linear_regression_model_surface.predict(np.array([[2025]]))[0]
population_2050 = linear_regression_model_surface.predict(np.array([[2025]]))[0]