import utils
import read_csv
import charts
import pandas as pd


def run():
  '''

  if len(result) > 0:
    countrys = result[0]
    labels, values = utils.population_by_country_years(countrys)
    
  print(result)
  '''
  df = pd.read_csv('data.csv')  
  df = df[df['Continent'] == 'South America']

  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values
  charts.generate_pie_chart(countries, percentages)
  #country = input('Digite el pais =>')  

  


def draw_population_bars():
  data = read_csv.read_csv('data.csv')
  labels, values = utils.get_world_population(data)


if __name__ == '__main__':
  run()
