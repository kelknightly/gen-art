# Cheela

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random

def draw_cheela(ax, center, size):
    x, y = center
    # body
    for _ in range(5):  
        width, height = size
        ellipse = patches.Ellipse((x, y), width, height, 
                                  color=(random.uniform(0, 0.5), random.uniform(0, 0.5), random.uniform(0, 0.5), random.uniform(0.5, 0.9)),
                                  angle=random.uniform(0, 360))
        ax.add_patch(ellipse)
        size = (size[0] * 0.8, size[1] * 0.8)  

    # eyes
    for _ in range(12):  
        eye_x, eye_y = x + random.uniform(-width/2, width/2), y + random.uniform(-height/2, height/2)
        eye_size = min(width, height) * 0.1
        eye = patches.Circle((eye_x, eye_y), eye_size, color='yellow')
        ax.add_patch(eye)

fig, ax = plt.subplots(figsize=(10, 10))

fig.patch.set_facecolor((0.7, 0.85, 0.9))

ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)
ax.axis('off')

ax.set_facecolor((0.7, 0.85, 0.9))

# magnetic fields
charcoal_grey = (0.21, 0.27, 0.31)  
for y_line in np.linspace(-80, 80, 3):  
    ax.axhline(y=y_line, color=charcoal_grey, linestyle=':', linewidth=1.5)

for i in range(3):  # Place Cheela on each gridline
    y = np.linspace(-80, 80, 3)[i]
    for _ in range(2):  # Number of Cheela per line
        x = random.uniform(-80, 80)
        size = (random.uniform(20, 40), random.uniform(10, 20))  
        draw_cheela(ax, (x, y), size)

plt.show()