#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import streamlit as st


# In[4]:


import streamlit as st

st.title('Find the Highest Value')

# Take two values as input from the user
value1 = st.number_input('Enter the first value')
value2 = st.number_input('Enter the second value')

# Find and display the highest value
highest_value = max(value1, value2)
st.write(f'The highest value is: {highest_value}')


# In[ ]:




