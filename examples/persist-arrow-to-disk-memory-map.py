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

# %%
# Imports

# %%
import pyarrow as pa
import os

# %%
# Save an array to disk

# %%
example_array = pa.array([1,2,3,4,5,6])

# %%
schema = pa.schema([
    pa.field('numbers', example_array.type)
])

# %%
schema

# %%
with pa.OSFile(os.path.join(os.getcwd(),"data","example_array.arrow"), 'wb') as sink:
    with pa.ipc.new_file(sink, schema=schema) as writer:
        batch = pa.record_batch([example_array], schema=schema)
        writer.write(batch)

# %%
# This is nice.  But, what abt a table?

# %%
a_table = pa.table([[1,2,3,4],[10,20,30,40],[100,200,300,400]],  names=["units", "tens", "huns"])

# %%
with pa.OSFile(os.path.join(os.getcwd(),"data","example_table_two.arrow"), 'wb') as sink:
    with pa.ipc.new_file(sink, schema = a_table.schema) as writer:
        writer.write(a_table)


# %%
# Alternative:  Convert to a record batch (Which requires you to extract the schema)

# %%
a_rb = pa.record_batch(a_table.to_pandas(), schema=a_table.schema)

with pa.OSFile(os.path.join(os.getcwd(),"data","example_table_three.arrow"), 'wb') as sink:
    with pa.ipc.new_file(sink, schema = a_table.schema) as writer:
        writer.write(a_rb)

# %%
## Map to Memory

# %%
with pa.memory_map(os.path.join(os.getcwd(),"data","example_array.arrow"), 'r') as source:
    loaded_arrays = pa.ipc.open_file(source).read_all()

# %%
loaded_arrays

# %%
with pa.memory_map(os.path.join(os.getcwd(),"data","example_table_two.arrow"), 'r') as source:
    loaded_table = pa.ipc.open_file(source).read_all()

# %%
loaded_table

# %%
with pa.memory_map(os.path.join(os.getcwd(),"data","example_table_three.arrow"), 'r') as source:
    loaded_table_three = pa.ipc.open_file(source).read_all()

# %%
loaded_table_three

# %%
