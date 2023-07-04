import folium
import pandas as pd
import tkinter.filedialog as fd
import os

root = fd.Tk()
root.withdraw()  # use to hide tkinter window

currdir = os.getcwd()

input_file_path = fd.askopenfilename(parent=root, initialdir=currdir, title='Please select an input file')
if len(input_file_path) > 0:
    print("You chose %s" % input_file_path)

data = pd.read_excel(input_file_path)

# Create a Folium map centered on the mean latitude and longitude
center_lat = data['Latitude'].mean()
center_lon = data['Longitude'].mean()

m = folium.Map(location=[center_lat, center_lon], zoom_start=16, control_scale=True)

# Add satellite imagery as a TileLayer
folium.TileLayer(
    tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
    attr='ArcGIS',
    name='Satellite Imagery',
    opacity=1,
    overlay=True
).add_to(m)

# Add OpenStreetMap overlay with increased opacity for street names
folium.TileLayer(
    tiles='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
    attr='OpenStreetMap Overlay',
    name='Street Names',
    overlay=True,
    opacity=0.5,  # Increase the opacity to make the street names more opaque
).add_to(m)

# Create a layer control
folium.LayerControl().add_to(m)

# Iterate over the rows of the data table
for index, row in data.iterrows():
    # Extract the required information from the row
    location = [row['Latitude'], row['Longitude']]
    type = row['Type']
    price = row['Price']
    lot_t = row['Lot type']
    w_and_p = row['Water&Power']
    a_l = row['Adjacent Lot']

    popup_text = f'Type: {type}<br>Lot type: {lot_t}<br>Price: {price}<br>Water&Power: {w_and_p}<br>Adjacent Lot: {a_l}'
    popup_html = folium.Html(popup_text, script=True)
    popup = folium.Popup(popup_html, max_width=1000)

    # Create a marker with a popup for each location
    icon = folium.Icon(icon='sign-hanging fa-bounce', prefix='fa', color='red')
    folium.Marker(location=location, icon=icon, popup=popup).add_to(m)

# Save the map to an HTML file
output_file_path = fd.asksaveasfilename(parent=root, initialdir=currdir, title='Please select an output file',
                                        defaultextension='.html', filetypes=[('HTML files', '.html')])
if len(output_file_path) > 0:
    m.save(output_file_path)
    print("Map saved to %s" % output_file_path)
