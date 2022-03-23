import pandas as pd
import plotly.figure_factory as pff

wireframe = pd.read_csv("Project/data.csv")
fig = pff.create_distplot([wireframe["Avg Rating"].tolist()],["Average rating for Mobiles"])
fig.show()