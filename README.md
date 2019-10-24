# Identify Commercial Centers in Jaipur

**Aim:** Identify commercial centers using Points of Interest (POI) data of Jaipur city.

There's a lot of open data available about the demographics and geography of the planet. But this information is not necessarily supervised in any particular structure from which insights can be drawn.

This project creates clusters of distinct commercial centers or markets using points of interest data of Jaipur. Points of interest (POI) data provides location information of different places along with their defining tags like school, type of outlets, type of building, etc.

POI data refers to the coordinates (latitudes and longitudes) of any physical entity with a tag describing its type like commercial buildings, schools, hospitals, restaurants, etc.
 
**Objectives:**

* Get Points of Interest from open data sources like open street maps (OSM).
* Understand how spatial location data works
  * Understand spatial vector data types and how to manipulate it using your language of choice.
  * Understand necessary GIS concepts like projections, spatial clustering, etc.
* Figure out a way of clustering these points into commercial centers/markets. You can use standard size polygons also to cluster the points.
* Find and label the most significant clusters, statistically and intuitively. 
* Visualize the resultant commercial centres/markets. 

## Methodology

### Collect POI data of Jaipur city
All the commercial centers form the heart of the city and contain most of the amenities like restaurants, commerical shopping complexes, malls, hospitals, etc. So, we considered 39 such amenities and using `overpy` we collected POI spatial data of the city. Overpy is the python module used for extracting open data from Open Street Maps (OSM) using `Overpass QL` query language. POI data mainly contains:
* Node: Represents amenities with their lat, lon and tags providing information like type of amenity, name and their address.
* Way: An ordered list of nodes represents a way.
* Relation: A group of elements used to model logical or geographical relationships between objects.

POI data contains `422 nodes` and `72 ways`.



## Running the project
* Clone this repository by typing following command on the terminal: `git clone https://github.com/vibhor98/Identify-Commercial-Centers.git`.

* Run: **pip install requirements.txt** to install all the required dependencies.

* Navigate to the directory containing `IdentifyCommercialClusters.ipynb` python notebook and run: jupyter notebook to open the analysis file.
