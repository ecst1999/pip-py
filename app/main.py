import utils
import read_csv
import charts


def run():
  data = read_csv.read_csv('data.csv')
  country = input('Digite el pais =>')
  result = utils.population_by_country(data, country)

  if len(result) > 0:
    countrys = result[0]
    labels, values = utils.population_by_country_years(countrys)
    charts.generate_bar_chart(country, labels, values)

  print(result)

  #draw_population_bars()


def draw_population_bars():
  data = read_csv.read_csv('data.csv')
  labels, values = utils.get_world_population(data)
  charts.generate_pie_chart(labels, values)


if __name__ == '__main__':
  run()
