#!/usr/bin/env python
# coding: utf-8

# In[9]:


from bs4 import BeautifulSoup
import requests
url = 'https://en.wikipedia.org/wiki/Starbucks' #URL to the web page
page = requests.get(url)
pulled_page = BeautifulSoup(page.text,'html')


table = pulled_page.find_all('table')[2] ##saving table with index 2 to the variable

titles = table.find_all('th')
titles
table_titles = [title.text.strip() for title in titles]


import pandas as pd
df = pd.DataFrame(columns=table_titles)
df
column_data = table.find_all('tr')

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    length = len(df)
    df.loc[length] = individual_row_data
df.to_csv(r'Starbucks_Development.csv', index = False) ##Saving the table to a csv file
print(df)


# In[ ]:





# In[ ]:




