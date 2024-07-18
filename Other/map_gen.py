
# Import libraries
from folium import Map, FeatureGroup, Popup, LayerControl, Marker, Icon
from logging import basicConfig, INFO, getLogger
from datetime import datetime, timedelta
import pandas as pd
import requests

# Configuration
DAYS_TO_PAY = 40
EXCEL_PATH = "excel_path"
DATE_FORMAT = "%d.%m.%Y"
COLUMN_NAMES = ["Address", "Date"]

# Setup logging
basicConfig(level=INFO)
logger = getLogger()

# Load data from excel file
def load_data(excel_path, columns):
	try:
		return pd.read_excel(excel_path, usecols=columns)
	except Exception as e:
		logger.error(f"Error loading excel file: {e}")

# Fetch coordinates
def get_coordinates(address):
	url = "https://nominatim.openstreetmap.org/search"
	params = {"q": address, "format" : "json"}
	headers  = {"User-Agent" : "Project/1.0('veselyfilip27@gmail.com')"}
	try:
		response = requests.get(url, params=params, headers=headers)
		response.raise_for_status()
		data = response.json()
		if data:
			return data[0]["lat"], data[0]["lon"]
		else:
			logger.warning(f"No coordinates found for address: {address}")
			return None, None
	except requests.RequestException as e:
		logger.error(f"Error fetching coordinates for {address}: {e},")
		return None, None

# Create the map
def create_map(businesses, last_possible_pay_date):
	map = Map(location=(50.075518, 14.460031), tiles="Cartodb Positron", zoom_start=11)
	group_paid = FeatureGroup(name="Paid", show=True).add_to(map)
	group_unpaid = FeatureGroup(name=u"Didn't pay", show=True).add_to(map)
	for address, date in businesses:
		lat, lon = get_coordinates(address)
		if lat and lon:
			if last_possible_pay_date < datetime.strptime(date, DATE_FORMAT):
				Marker((lat, lon), popup=Popup(f"Address: {address}<br>Status: paid {date}", max_width=1000), icon=Icon("green")).add_to(group_paid)
			else:
				Marker((lat, lon), popup=Popup(f"Address: {address}<br>Status: Didnt pay<br>Last payment: {date}", max_width=1000), icon=Icon("red")).add_to(group_unpaid)
	LayerControl().add_to(map)
	map.save("map.html")

# Main function
def main():
	try:
		excel_sheet = load_data(EXCEL_PATH, COLUMN_NAMES)
		businesses = [(row[COLUMN_NAMES[0]], row[COLUMN_NAMES[1]].strftime(DATE_FORMAT)) for index, row in excel_sheet.iterrows()]
		last_possible_pay_date = datetime.now() - timedelta(days=DAYS_TO_PAY)
		create_map(businesses, last_possible_pay_date)
		logger.info("Map was successfully created and stored in map.html")
	except Exception as e:
		logger.error(f"Failed to create map: {e}")

# Run
if __name__ == "__main__":
	main()
