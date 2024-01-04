# Rendezvous with Rama

import matplotlib.pyplot as plt
import numpy as np
import random

def draw_structure(ax, center, size):
    # internal structures
    x, y = center
    width, height = size
    green_shade = (random.uniform(0, 0.5), random.uniform(0.5, 1), random.uniform(0, 0.5))
    rect = plt.Rectangle((x - width/2, y - height/2), width, height, 
                         color=green_shade, alpha=0.7)
    ax.add_patch(rect)

def draw_cylindrical_sea(ax, radius):
    # cylindrical sea
    circle = plt.Circle((0, 0), radius, color='blue', fill=False, linewidth=2)
    ax.add_patch(circle)

def draw_biot(ax):
    x, y = random.uniform(-100, 100), random.uniform(-100, 100)
    radius = random.uniform(1, 3)  # Smaller radius for biots
    grey_shade = (random.uniform(0.5, 0.8), random.uniform(0.5, 0.8), random.uniform(0.5, 0.8))
    circle = plt.Circle((x, y), radius, color=grey_shade, alpha=0.8)
    ax.add_patch(circle)


fig, ax = plt.subplots(figsize=(10, 10))

ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)
ax.axis('off')

draw_cylindrical_sea(ax, 80)

for _ in range(90):
    x, y = random.uniform(-80, 80), random.uniform(-80, 80)
    size = (random.uniform(5, 15), random.uniform(5, 15))
    draw_structure(ax, (x, y), size)

for _ in range(50):  # Number of biots
    draw_biot(ax)

plt.show()
