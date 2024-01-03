'''
import matplotlib.pyplot as plt
import random

# Function to generate a wide variety of blue shades
def random_blue_color():
    return (random.uniform(0, 0.3), random.uniform(0, 0.3), random.uniform(0, 1))  
    # R and G up to 0.3 for subtle variation, B between 0 to 1 for full range of blues

def draw_circle(ax):
    color = random_blue_color()
    radius = 0.05 + 0.1 * random.random() 
    circle = plt.Circle((random.random(), random.random()), radius, color=color, alpha=0.5)
    ax.add_artist(circle)

fig, ax = plt.subplots()

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

ax.axis('off')

for _ in range(100):  
    draw_circle(ax)

plt.savefig('blue_circles_art.pdf', format='pdf')

plt.show()
'''

import matplotlib.pyplot as plt
import numpy as np
import random

def random_blue_color():
    return (random.uniform(0, 0.3), random.uniform(0, 0.3), random.uniform(0, 1))

def draw_filled_heart(ax, x, y, size):
    color = random_blue_color()
    t = np.linspace(0, 2 * np.pi, 100)
    x_vals = 16 * np.sin(t)**3
    y_vals = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

    scaled_x_vals = x + x_vals * size
    scaled_y_vals = y + y_vals * size

    ax.fill(scaled_x_vals, scaled_y_vals, color=color, alpha=0.5)

fig, ax = plt.subplots()

ax.set_xlim(-120, 120)
ax.set_ylim(-120, 120)

ax.axis('off')

for _ in range(50):  
    draw_filled_heart(ax, random.uniform(-100, 100), random.uniform(-100, 100), random.uniform(1, 2))

plt.savefig('blue_filled_hearts_art.pdf', format='pdf')

plt.show()
