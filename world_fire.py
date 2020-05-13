import csv

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename="world_fires_1_day.csv"
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)

    # get the lattitude longitude brightness
    lons, lats, bris= [], [], []
    for row in reader:
        lat=float(row[0])
        lon=float(row[1])
        bri=float(row[2])

        lats.append(lat)    
        lons.append(lon)
        bris.append(bri)


data=[{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'marker': {
        'color': bris,
        'colorscale': 'Viridis',
        'reversescale':True,
        'colorbar': {'title': 'Brightness'}
    },
}]
my=Layout(title='Global fires')

fig={'data': data, 'layout': my}
offline.plot(fig,filename="global_fires.html")