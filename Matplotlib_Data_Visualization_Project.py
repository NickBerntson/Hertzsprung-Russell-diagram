# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 18:57:05 2024

@author: nicol
"""

# Sample data for the scatter plot
#x = [1, 2, 3, 4, 5]
#y = [10, 20, 25, 30, 40]

# Create a scatter plot
#plt.scatter(x, y, color='blue', marker='o')

# Add a title and labels to the axes
#plt.title("Simple Scatter Plot")
#plt.xlabel("X Axis")
#plt.ylabel("Y Axis")

# Display the plot
#plt.show()

#Super Giants

import matplotlib.pyplot as plt
import numpy as np

plt.xticks([40000, 20000, 10000, 5000, 2500])
plt.yticks([1e-4, 1e-2, 1, 1e2, 1e4, 1e6], 
           labels=["$10^{-4}$", "$10^{-2}$", "$10^{0}$", "$10^{2}$", "$10^{4}$", "$10^{6}$"])

supergiant_stars = ["Rigel", "Deneb", "Antares", "Betelgeuse", "Polaris"]
supergiant_temp = [11000, 8500, 3500, 3500, 7200]
supergiant_lum = [47000, 196000, 65000, 10200, 2000]

giant_stars = ["Aldebaren", "Acturus", "Pollux"]
giant_temp = [3900 ,4300, 4900]
giant_lum = [500, 200, 43]

mainseq_stars = ["Sun", "Alpha Centauri", "Sirius", "Procyon A", "Proxima Centauri", "Bellatrix"]
mainseq_temp = [5800, 5800, 9900, 6500, 3000, 22000]
mainseq_lum = [1, 2, 25, 7, 0.0017, 9200]

whitedwarf_stars = ["Sirius B", "Procyon B"]
whitedwarf_temp = [25000, 20000]
whitedwarf_lum = [0.026, 0.00055]

plt.figure(figsize=(8,6))

plt.scatter(supergiant_temp, supergiant_lum, color='lightblue', label='Supergiant', s=100)
plt.scatter(giant_temp, giant_lum, color='red', label='Giant', s=100)
plt.scatter(mainseq_temp, mainseq_lum, color='orange', label='Main Sequence', s=100)
plt.scatter(whitedwarf_temp, whitedwarf_lum, color='yellow', label='White Dwarf', s=100)

plt.xscale('linear')  
plt.yscale('log')  
plt.gca().invert_xaxis()

for i, star in enumerate(supergiant_stars):
    plt.text(supergiant_temp[i], supergiant_lum[i], star, fontsize=9, ha='center', va='center')

for i, star in enumerate(giant_stars):
    plt.text(giant_temp[i], giant_lum[i], star, fontsize=9, ha='center', va='center')

for i, star in enumerate(mainseq_stars):
    plt.text(mainseq_temp[i], mainseq_lum[i], star, fontsize=9, ha='center', va='center')

for i, star in enumerate(whitedwarf_stars):
    plt.text(whitedwarf_temp[i], whitedwarf_lum[i], star, fontsize=9, ha='center', va='center')

plt.xlabel("Surface Temperature (K)")
plt.ylabel("Luminosity (L)")
plt.title("Hertzsprung-Russell Diagram")

plt.grid(True)
plt.legend()

plt.show()