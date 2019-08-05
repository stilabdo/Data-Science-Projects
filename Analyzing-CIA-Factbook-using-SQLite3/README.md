# Analyzing CIA Factbook Using SQLite and Python 
This project is a part of my data science portfolio of projects.

#### -- Project Status: Completed



### Methods Used
* Database Connection
* Data Visualization

### Technologies
#### SQLite3 with Python in jupyter notebook
##### Libiries
* SQLite3
* Pandas 
* Matplotlib

## Project Description
The database includes two tables, facts and cities

 
#### Attributes:
##### facts table 
* name &nbsp; : &nbsp; The name of the country.
* area &nbsp; : &nbsp; The total land and sea area of the country.
* population &nbsp; : &nbsp; The country's population.
* population_growth &nbsp; : &nbsp; The country's population growth as a percentage.
* birth_rate &nbsp; : &nbsp; The country's birth rate, or the number of births a year per 1,000 people.
* death_rate &nbsp; : &nbsp; The country's death rate, or the number of death a year per 1,000 people.
* area &nbsp; : &nbsp; The country's total area (both land and water).
* area_land &nbsp; : &nbsp; The country's land area in square kilometers.
* area_water &nbsp; : &nbsp; The country's waterarea in square kilometers.

##### cities table
* id &nbsp; : &nbsp; A unique ID for each city.
* name &nbsp; : &nbsp; The name of the city.
* population &nbsp; : &nbsp; The population of the city.
* capital &nbsp; : &nbsp; Whether the city is a capital city: 1 if it is, 0 if it isn't.
* facts_id &nbsp; : &nbsp; The ID of the country, from the facts table.