from plotly.offline import iplot, init_notebook_mode
import plotly.express as plot
import pandas as pd
import numpy as np

data = pd.read_csv('./data/parsed_data.csv')

init_notebook_mode(connected=True)

graph = plot.scatter(data, x="price", y="house_size", trendline="ols", color='price', title='Price vs Square Footage')
graph.show(renderer="png")
