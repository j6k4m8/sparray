# spndarray


```python

import numpy as np
import spndarray

# We have a dataset...
>>> data = np.zeros((10, 10, 10))
# It has a peculiar value at [5, 5, 5].
>>> data[5, 5, 5] = 3.14

# WE know that each voxel of this block is one meter:
>>> block = spndarray.spndarray(data, unit="m")

# Now we can access that same data in whatever unit we'd like:
>>> print(block[5000, 5000, 5000, "mm"])
3.14

# What if the voxels aren't perfect unit-cubes?
# In this example, the data are 0.5 x 0.5 x 5 meters per voxel:
>>> aniso_block = spndarray.spndarray(
    data,
    voxelsize=(0.5, 0.5, 5),
    unit="m"
)
>>> print(aniso_block[2.5, 2.5, 25, 'm'])
3.14
```
