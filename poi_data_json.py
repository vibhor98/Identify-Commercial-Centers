# Gets the POI data of the city of Jaipur and saves it in a JSON file.

import requests
import json

overpass_url = "http://overpass-api.de/api/interpreter"
# Selecting amenities like: restaurants, shopping malls, hospitals, etc. as
# POIs. All the commerical areas of the city must contain most of these
# amenities.
overpass_query ="""[out:json];
    area[name="Jaipur"][boundary=administrative]->.searchArea;
    (node["amenity"](area.searchArea);
     way["amenity"](area.searchArea);
     relation["amenity"](area.searchArea);
    );
    out center;
    """

response = requests.get(overpass_url, params={'data': overpass_query})
data = response.json()
f = open('spatial_data.json', 'w')

print('Dumping spatial data...')
# Saving data to a json file.
json.dump(data, f)
f.close()
