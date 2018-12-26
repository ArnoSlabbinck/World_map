import folium
import pandas

data = pandas.read_json("cities.json")
lat = list(data["lat"])
lng = list(data["lng"])
cities = list(data["name"])

map = folium.Map(location=[51.2263, 4.8353], zoom_start=6, tiles="Mapbox Bright")
folium.CircleMarker(location=[51.2263, 4.8353], radius = 130, fill=True,  color = 'green', fill_opacity=1)

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")
