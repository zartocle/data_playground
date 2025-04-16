import folium
import pandas

def color_selector(elevation): # This function will allow us to have different marker colors based on a criteria
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"

volc_data=pandas.read_csv("Volcanoes.txt")  # Import data from text file to dataframe
lat=list(volc_data["LAT"])      # Make the relevant info into a list
lon=list(volc_data["LON"])      # Make the relevant info into a list
elev=list(volc_data["ELEV"])

# Initialize the map, mentioning the starting point (location), zoom and style (tiles)
map = folium.Map(location=[42.92,11.64],zoom_start=12,tiles="Stamen Terrain")

fgv=folium.FeatureGroup(name="Vulcani")

# create the markers layer, based on the coordinates as per the abovementioned lists
for la,lo,el in zip(lat,lon,elev): # The ZIP is required to "stitch" together different lists in a cycle operation
    fgv.add_child(folium.Circle(location=[la,lo],popup=str(el),radius="0.01"))

# Prepare a layer (polygon layer in this case),using a feature group
fgp=folium.FeatureGroup(name="Population")

# Setting up the polygon layer
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
# The following line outlines a dynamic color code based on the population data from the same JSON file
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<10000000 else 'orange' if 10000000< x['properties']['POP2005']< 200000000 else 'red'}))

# Adding the feature groups to the map - it's good to keep them separate, so they'll be separate layers
map.add_child(fgp) # Applying the feature group to the map
map.add_child(fgv) # Applying the feature group to the map

map.add_child(folium.LayerControl())

map.save("Map1.html")   # saving the map to the file




