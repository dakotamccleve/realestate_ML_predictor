import plotly.express as plot
import pandas as pd


data = pd.read_csv('./data/parsed_data.csv')

graph = plot.scatter(data, x="house_size", y="price", trendline="ols", color='price', title='Price vs Square Footage')
graph.show()

graph = plot.scatter(data, x="bed", y="price", trendline="ols", color='price', title='Price vs Beds')
graph.show()

graph = plot.scatter(data, x="bath", y="price", trendline="ols", color='price', title='Price vs Beds')
graph.show()
