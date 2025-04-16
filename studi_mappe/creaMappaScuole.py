import folium
import pandas

def color_selector(statale): # This function will allow us to have different marker colors based on a criteria
    if lower(statale) == "statale":
        return "green"
    elif lower(statale) == "paritaria":
        return "red"
    else:
        return "orange"

dati_scuole=pandas.read_csv("lista_scuole_FINALE.csv")  # Import data from text file to dataframe
lat=list(dati_scuole["latitudine"])      # Make the relevant info into a list
lon=list(dati_scuole["longitudine"])      # Make the relevant info into a list
nome=list(dati_scuole["des_tipo_scuola"])
#print(dati_scuole)
# Initialize the map, mentioning the starting point (location), zoom and style (tiles)
map = folium.Map(location=[42.92,11.64],zoom_start=12,tiles="Stamen Terrain")

fgv=folium.FeatureGroup(name="Scuole")

# create the markers layer, based on the coordinates as per the abovementioned lists
for la,lo,nm in zip(lat,lon,nome): # The ZIP is required to "stitch" together different lists in a cycle operation
    fgv.add_child(folium.Circle(location=[la,lo],popup=str(nm),radius="0.01"))

# Adding the feature groups to the map - it's good to keep them separate, so they'll be separate layers
map.add_child(fgv) # Applying the feature group to the map

map.add_child(folium.LayerControl())

map.save("Map1.html")   # saving the map to the file

