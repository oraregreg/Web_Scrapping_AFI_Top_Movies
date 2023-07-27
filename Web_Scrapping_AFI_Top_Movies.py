#!/usr/bin/env python
# coding: utf-8

# # Web_Scrapping_AFI_Top_Movies

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


url = 'https://en.wikipedia.org/wiki/AFI%27s_100_Years...100_Movies'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')


# In[3]:


print(soup)


# In[7]:


soup.find_all('table')[1]


# In[8]:


table = soup.find_all('table')[1]

print(table)


# In[9]:


column_names = table.find_all('th')


# In[10]:


print(column_names)


# In[12]:


column_names_final = [names.text.strip() for names in column_names]

print(column_names_final)


# In[13]:


import pandas as pd


# In[14]:


df = pd.DataFrame (columns = column_names_final)


# In[15]:


df


# In[17]:


#filling in the column data

column_data = table.find_all('tr')


# In[19]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data


# In[20]:


df


# In[21]:


#exporting the dataframe to csv with a specified file path
#Companies.csv is the name we are calling the excel file, 
#index = False means we get rid of the indexing column

df.to_csv(r'C:\Users\Greg\Desktop\Python_Web_Scraping\Folder for output\Top_Films.csv', index = False)


# In[ ]:




