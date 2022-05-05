library(sf)
library(dplyr)
library(magrittr)  

shapefile <-st_read("~/Documents/Shapefile/precincts_hamco/precincts_hamco.shp") 
hamilton<-left_join(shapefile,hamilton_county, by=c('Precinct'='Precinct'))  

st_write(hamilton,paste0('data/',Sys.Date(), 'HamiltonCounty','.shp')  
