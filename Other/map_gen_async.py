import asyncio
import aiohttp
import pandas as pd
from folium import Map, FeatureGroup, Popup, LayerControl, Marker, Icon
from datetime import datetime, timedelta
import logging

# Configuration
DAYS_TO_PAY = 40
EXCEL_PATH = "path_to_excel"
DATE_FORMAT = "%d.%m.%Y"
COLUMN_NAMES = ["Address", "Date"]

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_data(excel_path, columns):
    try:
        return pd.read_excel(excel_path, usecols=columns)
    except Exception as e:
        logger.error(f"Error loading Excel file: {e}")
        raise

async def fetch_coordinates(session, address):
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": address, "format": "json"}
    headers = {"User-Agent": "Project/1.0 (veselyfilip27@gmail.com)"}
    try:
        async with session.get(url, params=params, headers=headers) as response:
            response.raise_for_status()
            data = await response.json()
            if data:
                return address, data[0]["lat"], data[0]["lon"]
            else:
                logger.warning(f"No coordinates found for address: {address}")
                return address, None, None
    except aiohttp.ClientError as e:
        logger.error(f"Error fetching coordinates for {address}: {e}")
        return address, None, None

async def fetch_all_coordinates(addresses):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_coordinates(session, address) for address in addresses]
        return await asyncio.gather(*tasks)

def create_map(businesses, coordinates, last_possible_pay_date):
    map_obj = Map(location=(50.075518, 14.460031), tiles="Cartodb Positron", zoom_start=11)
    group_paid = FeatureGroup(name="Paid", show=True).add_to(map_obj)
    group_unpaid = FeatureGroup(name="Didn't pay", show=True).add_to(map_obj)

    for (address, date), (_, lat, lon) in zip(businesses, coordinates):
        if lat and lon:
            if last_possible_pay_date < datetime.strptime(date, DATE_FORMAT):
                Marker((lat, lon), popup=Popup(f"Address: {address}<br>Status: paid {date}", max_width=1000), icon=Icon("green")).add_to(group_paid)
            else:
                Marker((lat, lon), popup=Popup(f"Address: {address}<br>Status: Didn't pay<br>Last payment: {date}", max_width=1000), icon=Icon("red")).add_to(group_unpaid)
    
    LayerControl().add_to(map_obj)
    map_obj.save("map.html")

async def main():
    try:
        excel_sheet = load_data(EXCEL_PATH, COLUMN_NAMES)
        businesses = [(row['Address'], row['Date'].strftime(DATE_FORMAT)) for index, row in excel_sheet.iterrows()]
        addresses = [address for address, _ in businesses]
        last_possible_pay_date = datetime.now() - timedelta(days=DAYS_TO_PAY)
        coordinates = await fetch_all_coordinates(addresses)
        create_map(businesses, coordinates, last_possible_pay_date)
        logger.info("Map successfully created and saved to map.html")
    except Exception as e:
        logger.error(f"Failed to create map: {e}")

if __name__ == "__main__":
    asyncio.run(main())