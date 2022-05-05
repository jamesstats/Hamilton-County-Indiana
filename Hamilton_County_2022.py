#!/usr/bin/env python
# coding: utf-8

# In[2]:


import geopandas as gpd
import pandas as pd  
import numpy as np 
import fiona


# In[3]:


shapefile=gpd.read_file("precincts_hamco/precincts_hamco.shp") 


# In[4]:


results=pd.read_csv("hamilton_county.csv")  


# In[5]:


HamCo = gpd.GeoDataFrame(results.merge(shapefile, on="Precinct")) 


# In[6]:


HamCo=HamCo.drop(['created_us','created_da','last_edite','last_edi_1','GlobalID',],axis=1)  


# In[7]:


HamCo.to_csv('Hamilton_County_PA_Primary.csv', index=False) 


# In[8]:


HamCo.to_file("Hamilton_County.shp") 

