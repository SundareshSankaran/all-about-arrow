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

# %% [markdown]
# # Read and write Parquet - Tutorial

# %% [markdown]
# ## Imports

# %%
import pyarrow as pa

# %%
import pyarrow.parquet as pq

# %% [markdown]
# ## Read a dummy CSV
#

# %%
import pandas as pd
import os

pdf = pd.read_csv(os.path.join(os.getcwd(),"data","sample-data-for-file-reads.csv"))

# %%
a_table = pa.Table.from_pandas(pdf)

# %% [markdown]
# ## Write table to Parquet

# %%
pq.write_table(a_table, os.path.join(os.getcwd(),"data","a_table_example.parquet"), compression=None)

# %% [markdown]
# ## Read from Parquet

# %%
a_new_table = pq.read_table(os.path.join(os.getcwd(),"data","a_table_example.parquet"))

# %%
a_new_table

# %% [markdown]
# ## An example of how to read in specific columns and apply filtering on the base Parquet file
# #### This helps you take advantage of the columnar format of Parquet

# %%
filtered_table = pq.read_table(os.path.join(os.getcwd(),"data","a_table_example.parquet"),
                      columns=["Date_Field", "Categorical", "Char"],
                      filters=[
                          ("Num", ">", 3),
                          ("Num", "<", 5),
                      ])

# %%
filtered_table

# %% [markdown]
# #### Also note that the column used as a filter need not be carried over

# %%

# %%
