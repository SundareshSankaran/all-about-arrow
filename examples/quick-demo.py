# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.7
#   kernelspec:
#     display_name: buildproj
#     language: python
#     name: buildproj
# ---

# %% [markdown] vscode={"languageId": "plaintext"}
# # PyArrow - Getting Started
#
# ## Quick Demo

# %% [markdown] vscode={"languageId": "plaintext"}
# ## Import Package

# %% vscode={"languageId": "plaintext"}
import pyarrow as pa

# %% [markdown] vscode={"languageId": "plaintext"}
# ## Let's look at two basic structures : Arrays & Tables

# %% [markdown]
# ### Create a simple array.  Start with a list

# %%
a_list = [1,2,3,4,5]

# Convert to PyArrow Array
array_a = pa.array(a_list)

# %%
# Describe the array

array_a

# %% [markdown]
# ### Same operation, but, this time, specify the type as int8

# %%
array_b = pa.array(a_list, type=pa.int8())

# %%
array_b

# %% [markdown]
# ### Why is this useful?  
# #### Let's consider the size of these two objects

# %%
import sys

# %%
sys.getsizeof(array_a)

# %%
sys.getsizeof(array_b)

# %% [markdown]
# ##### Takeaway: Characterise your data and specify appropriate type when loading, in order to minimise memory

# %% [markdown]
# ### Common Mistakes
#
# #### Try this:  Provide a type of Int 8 and Int 16 for the following array

# %%
years = pa.array([1990, 2000, 1995, 2000, 1995], type=pa.int8())

# %%
years = pa.array([1990, 2000, 1995, 2000, 1995], type=pa.int16())

# %%
years = pa.array([1990, 2000, 1995, 2000, 1995])
type(years)

# %% [markdown]
# #### Takeaway: Calling function with defaults may lead to errors such as above
#
# #### See Data Types and In-Memory Data Models (https://arrow.apache.org/docs/python/data.html#data) for more details.

# %% [markdown]
# ### Create a Table

# %% [markdown]
# #### Table can be loaded as a list of lists, like this:

# %%
a_table = pa.table([[1,2,3,4],[10,20,30,40],[100,200,300,400]],  names=["units", "tens", "huns"])

# %%
a_table

# %%
type(a_table["tens"])

# %% [markdown]
# #### Or, you can define arrays beforehand and then load to table

# %%
units = pa.array([1,2,3,4])
tens = pa.array([10,20,30,40])
hundreds = pa.array([100,200,300,400])
b_table = pa.table([units,tens,hundreds],  names=["units", "tens", "huns"])

# %%
b_table

# %%
type(b_table["tens"])

# %% [markdown]
# ## Conversion from Pandas to PyArrow
#
# Pandas serves as the established memory format for many data science projects.  Here is code to help you convert a Pandas data frame to a PyArrow table.  Factors such as space occupied in memory, support for downstream packages and suitability for compute operations, among others, will help you decide whether to use PyArrow or Pandas.

# %%
# Create a dummy data frame

import pandas as pd

pdf = pd.DataFrame({"A_Column":[1,2,4,5,6], "B_Column":[10,20,40,50,60], "C_Column":["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]})

# %%
# Create a list of column values.  T

list_of_lists =[]

for col in pdf.columns.values:
   list_of_lists.append(pdf[col].tolist())

# %% [markdown]
# ### The above step is to illustrate the structure.  There is a readymade function to convert to Pandas

# %%
a_table = pa.table(list_of_lists, names=pdf.columns.values)
b_table = pa.Table.from_pandas(pdf)

# %%
a_table

# %%
b_table

# %% [markdown]
# ## To summarise:
#
# 1. We have seen how to import and use the package
# 2. We have seen how to create PyArrow arrays
# 3. We have seen how to create PyArrow table objects.
# 4. We have an appreciation of how to plan the datatype of an array.
# 5. We have seen how to convert a Pandas dataframe to a PyArrow table.
#
