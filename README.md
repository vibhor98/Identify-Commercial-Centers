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

## Description of the files
* `IdentifyCommercialCenters.ipynb` is the jupyter file containing all the analysis and code for clustering and identifying the commercial centers of Jaipur.
* `poi_data_json.py` is the python script to get the POI data of Jaipur and save it as JSON file.
* `spatial_data.json` file contains the POI data in JSON format.
* `shapefiles/polygon.shp` is the Polygon ESRI Shapefile containing POI data.
* `requirements.txt` contains all the dependencies (python modules) required to run this project.

## Methodology

### 1. Collect POI data of Jaipur city
All the commercial centers form the heart of the city and contain most of the amenities like restaurants, commerical shopping complexes, malls, hospitals, etc. So, we considered 39 such amenities and using `overpy` we collected POI spatial data of the city. Overpy is the python module used for extracting open data from Open Street Maps (OSM) using `Overpass QL` query language. POI data mainly contains:
* Node: Represents amenities with their latitudes, longitudes and tags providing information like type of amenity, name and their address.
* Way: An ordered list of nodes represents a way.
* Relation: A group of elements used to model logical or geographical relationships between objects.

POI data of Jaipur contains `422 nodes` and `72 ways`. Below is the Scatterplot showing the nodes (POIs) of Jaipur plotted with longitude on x-axis and latitude on y-axis:
![POI Data Scatterplot](https://github.com/vibhor98/Identify-Commercial-Centers/blob/master/Images/poi_data_scatterplot.png)

The **densely clustered points (amenities)** denote the heart (posh commercial area) of the city while other far-away points indicate the small number of amenities in secluded, outskirts and underdeveloped areas of the Jaipur city.

### 2. Write POI data to a Polygon ESRI Shapefile
POI data is written into an ESRI shapefile using `pyshp`, a Python module to read, write and modify the shapefiles efficiently.

### 3. Cluster the points to figure out commercial centers in Jaipur
For spatial clustering of points, we used both Density-Based Spatial Clustering of Applications (DBSCAN) and K-means algorithm to figure out the commercial centers. We know that the areas containing large number of amenities as compared to other areas will be a commercial center.

#### Clustering by DBSCAN algorithm
DBSCAN clusters the data points to separate the area of high density (having large no. of amenities) with the area of low density and hence, separating out commercial areas from other areas of the city. DBSCAN is used because: it is robust to outliers, and does not require number of clusters to be specified priorly.

![DBSCAN Clustering](https://github.com/vibhor98/Identify-Commercial-Centers/blob/master/Images/dbscan_clustering.png)
From the scatterplot, we can observe that most of the points (amenities) are at the center surrounded by far-away points. So, the center area must be the posh main area of the city. Within this large cluster, there may be some small clusters as well. We'll zoom into the cluster to analyse it well in the further sections.

#### Clustering by K-Means algorithm
The points are clustered using K-Means algorithm by finding distance between them using their longitude and latitude values. 

![K-Means Clustering](https://github.com/vibhor98/Identify-Commercial-Centers/blob/master/Images/k-means_clustering.png)
Here, intententionally number of clusters is set high (=8) so that we can get smaller clusters within this center large cluster. So, as seen in the figure, the center cluster has 4 smaller clusters denoted by colors: yellow, parrot green, purple, and dark green.

### 4. Digging Deeper: Analysing sub-clusters within a center cluster
![POI Data zoomed-in](https://github.com/vibhor98/Identify-Commercial-Centers/blob/master/Images/poi_data_zoomedin.png)
This is a zoomed-in scatterplot of the large center cluster. We can clearly see some smaller clusters here. Let's cluster them using both DBSCAN and K-Means Clustering.

#### Using DBSCAN
![DBSCAN Clustering zoomed-in](https://github.com/vibhor98/Identify-Commercial-Centers/blob/master/Images/dbscan_clust_zoomedin.png)
From the above scatterplot, we can intuitively say that purple cluster has the highest density. It means it has the highest number of amenities in Jaipur. So, it is one of the commercial centers of Jaipur. Additionally, other smaller clusters are separate commercial areas in the city providing fewer amenities to the population residing there.

#### Using K-Means Clustering
![K-Means Clustering zoomed-in](https://github.com/vibhor98/Identify-Commercial-Centers/blob/master/Images/kmeans_clust_zoomedin.png)
The above plot demonstrates the K-means clustering on the POI points. Here, we can clearly see that there are many sub-clusters denoting separate commercial centers. Blue cluster is the largest among them.

## Running the project
* Clone this repository by typing following command on the terminal: `git clone https://github.com/vibhor98/Identify-Commercial-Centers.git`.

* Run: **pip install requirements.txt** to install all the required dependencies.

* Navigate to the directory containing `IdentifyCommercialClusters.ipynb` python notebook and run: jupyter notebook to open the analysis file.

## References
* [Overpass API Official documentation](https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL)
* [Loading Data from OpenStreetMap with Python and the Overpass API](https://janakiev.com/blog/openstreetmap-with-python-and-overpass-api/)
* [Shapefile (pyshp) Official documentation](https://pypi.org/project/pyshp/)
* [Detecting Urban Polycentric Structure from POI Data](https://www.researchgate.net/publication/333832256_Detecting_Urban_Polycentric_Structure_from_POI_Data)
* [Let’s cluster data points using DBSCAN](https://medium.com/@agarwalvibhor84/lets-cluster-data-points-using-dbscan-278c5459bee5)
