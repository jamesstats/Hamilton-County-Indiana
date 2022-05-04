#!/usr/bin/env python
# coding: utf-8

# In[1]:


import geopandas as gpd
import pandas as pd  
import numpy as np 


# In[38]:


shapefile=gpd.read_file(r"/Users/jameskuria/Desktop/jupyter/Hamilton County_22/Hamilton County.shp") 


# In[39]:


results=pd.read_csv(r"/Users/jameskuria/Desktop/jupyter/hamilton_county.csv")  


# In[40]:


HamCo = gpd.GeoDataFrame(results.merge(shapefile, on="Precinct")) 


# In[42]:


HamCo=HamCo.drop(['created_us','created_da','last_edite','last_edi_1','GlobalID',],axis=1)  


# In[45]:


HamCo.to_csv('Hamilton_County_PA_Primary.csv', index=False) 


# In[44]:


HamCo.to_file("Hamilton_County.shp")

