from folium import Map, FeatureGroup, Popup, LayerControl, Marker, Icon
import requests
from datetime import datetime, timedelta
import pandas as pd

days_to_pay = 40
excel_path = "path_to_excel"
format = "%d.%m.%Y"
column_names = ["Address", "Date"]

buisnesses = []
excel_sheet = pd.read_excel(excel_path, usecols=column_names)

for row in range(excel_sheet.shape[0]):
	data = excel_sheet.iloc[row].tolist()
	data[1] = data[1].strftime(format)
	buisnesses.append(data)


last_possible_pay_date = datetime.now() - timedelta(days=days_to_pay)

map = Map(location=(50.075518, 14.460031), tiles="Cartodb Positron", zoom_start=11)
group_paid = FeatureGroup(name="Paid", show=True).add_to(map)
group_unpaid = FeatureGroup(name=u"Didn't pay", show=True).add_to(map)

def get_coordinates(address):
	url = "https://nominatim.openstreetmap.org/search"
	params = {"q": address, "format" : "json"}
	headers  = {"User-Agent" : "Project/1.0('veselyfilip27@gmail.com')"}
	data = requests.get(url, params=params, headers=headers).json()
	return data[0]["lat"], data[0]["lon"]

for address, date in buisnesses:
	if last_possible_pay_date < datetime.strptime(date, format):
		Marker(get_coordinates(address), popup=Popup(f"Address: {address}<br>Status: paid {date}", max_width=1000), icon=Icon("green")).add_to(group_paid)
	else:
		Marker(get_coordinates(address), popup=Popup(f"Address: {address}<br>Status: Didnt pay<br>Last payment: {date}", max_width=1000), icon=Icon("red")).add_to(group_unpaid)

LayerControl().add_to(map)
map.save("map.html")
