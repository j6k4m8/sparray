"""
Various utilities for spatial arrays.
"""

import numpy as np


class Unit:
    m = 10e0
    cm = 10e-2
    mm = 10e-3
    um = 10e-6
    nm = 10e-9

    @staticmethod
    def from_string(s):
        lookup = {
            "m":  10e0,
            "cm": 10e-2,
            "mm": 10e-3,
            "um": 10e-6,
            "μm": 10e-6,
            "nm": 10e-9
        }
        return lookup[s]


class spndarray:

    def __init__(self, array, voxelsize=(1., 1., 1.), unit=Unit.m):
        self.backend = array
        self.voxelsize = voxelsize
        self.unit = Unit.from_string(unit)
        self.str_unit = unit

    def __getitem__(self, key):
        multiplier = 1
        if type(key[-1]) is str:
            multiplier = Unit.from_string(key[-1]) / self.unit
            key = tuple(key[:-1])
        _intkey = list(key)
        if type(key) is tuple:
            for i in range(len(key)):
                _intkey[i] = int((key[i] / self.voxelsize[i]) * multiplier)
            return self.backend[tuple(_intkey)]

    def np(self):
        return self.backend
