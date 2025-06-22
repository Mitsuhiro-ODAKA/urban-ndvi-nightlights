import rasterio
import numpy as np

def load_raster_as_array(path):
    with rasterio.open(path) as src:
        return src.read(1)

def calculate_difference(arr1, arr2):
    return arr1.astype(float) - arr2.astype(float)
