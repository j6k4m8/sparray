"""
Various utilities for spatial arrays.
"""

import numpy as np


class Unit:
    yd = 0.9144
    inch = 0.0254
    mi = 1609.344
    km = 1e3
    m = 1e0
    cm = 1e-2
    mm = 1e-3
    um = 1e-6
    nm = 1e-9

    @staticmethod
    def from_string(s):
        s = s.lower().rstrip("s")  # trim plurals and convert to lowercase
        lookup = {
            "yd": 0.9144,
            "yard": 0.9144,

            "in": 0.0254,
            "inch": 0.0254,

            "mi": 1609.344,
            "mile": 1609.344,

            "ly": 9.461e+15,
            "lightyear": 9.461e+15,

            "km": 1e3,
            "kilometer": 1e3,

            "m":  1e0,
            "meter":  1e0,

            "cm": 1e-2,
            "centimeter": 1e-2,

            "mm": 1e-3,
            "millimeter": 1e-3,

            "um": 1e-6,
            "μm": 1e-6,
            "micrometer": 1e-6,
            "micron": 1e-6,

            "nm": 1e-9,
            "nanometer": 1e-9
        }
        return lookup[s]


class spndarray:

    def __init__(self, array, voxelsize=(1., 1., 1.), unit=Unit.m):
        self.backend = array
        self.voxelsize = voxelsize
        self.unit = Unit.from_string(unit)
        self.str_unit=unit

    def __getitem__(self, key):
        multiplier = 1
        if type(key[-1]) is str:
            multiplier = Unit.from_string(key[-1]) / self.unit
            key = tuple(key[:-1])
        numpy_key = list(key)
        if isinstance(key, tuple):
            for i, k in enumerate(key):
                # For each key in the index, if the dimension is of type
                # slice, then convert the _slice_ instead of the scalar.
                if isinstance(k, slice):
                    numpy_key[i] = slice(
                        round((k.start / self.voxelsize[i]) * multiplier),
                        round((k.stop / self.voxelsize[i]) * multiplier)
                    )
                else:
                    # This dimension is a scalar:
                    numpy_key[i] = round((k / self.voxelsize[i]) * multiplier)
            return self.backend[tuple(numpy_key)]
        else:
            raise ValueError(f"Invalid index {key}.")

    def np(self):
        return self.backend
