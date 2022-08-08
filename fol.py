import pandas as pd
df =pd.read_csv('train.csv')
data =pd.read_csv('train.csv')
import folium
from folium.plugins import HeatMap
stationArr = df[['Y','X']].values
m = folium.Map(location=[stationArr[0][0],stationArr[0][1]], zoom_start=12)
HeatMap(stationArr[:50000], radius=15).add_to(m)
# m.add_child(folium.ClickForMarker(popup="hiiii"))
m.save('abc.html')

# import folium


# m = folium.Map(location=[45.5236, -122.6750])

# m.save("index.html")