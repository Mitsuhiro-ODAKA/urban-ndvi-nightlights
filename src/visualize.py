import matplotlib.pyplot as plt
import numpy as np

def plot_ndvi_map(array, title='NDVI Map'):
    plt.figure(figsize=(8, 6))
    plt.imshow(array, cmap='YlGn', vmin=-1, vmax=1)
    plt.colorbar(label='NDVI')
    plt.title(title)
    plt.axis('off')
    plt.show()

def plot_nightlights_map(array, title='Nightlights Map'):
    plt.figure(figsize=(8, 6))
    plt.imshow(array, cmap='inferno')
    plt.colorbar(label='Nighttime Light Intensity')
    plt.title(title)
    plt.axis('off')
    plt.show()
