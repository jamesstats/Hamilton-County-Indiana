# Hamilton-County-Indiana
The shapefile came from the offical Hamilton County gis and map portal which was updated in accordance to the redisctricting. The mapserver files can be found here(https://gis1.hamiltoncounty.in.gov/arcgis/rest/services/). Used ArcGIS REST servers in QGIS to download the mapserver files,turned them into polygons and exported as a shapefile. 
```
The shapefile is in the data folder and contains the following main attributes.
```


`OBJECT_1` One of the Object ID for the precincts

`Precinct`  Name and number of the precincts
 
`TOWNSHIP_NUMBER` Township number corresponding to the precinct
 
`CO_COMM(COUNTY COMMISSIONER)` Number of the County Commissioner seat correspoding to the precinct
 
`CO_COUNC(COUNTY COUNCIL)` Number of the Councty Council seat correspoding to the precinct
 
`ST_SEN` Number of the Senate seat correspoding to the precinct
 
`ST_HOUSE` Number of the House seat correspoding to the precinct
 
