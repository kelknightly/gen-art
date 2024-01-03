import matplotlib.pyplot as plt
import random
import numpy as np

def random_color():
    return [random.random() for _ in range(3)]

def draw_shape(ax):
    shape_type = random.choice(['circle', 'rectangle', 'triangle'])
    color = random_color()

    if shape_type == 'circle':
        circle = plt.Circle((random.random(), random.random()), 0.1 * random.random(), color=color, alpha=0.5)
        ax.add_artist(circle)
    elif shape_type == 'rectangle':
        rect = plt.Rectangle((random.random(), random.random()), 0.1 * random.random(), 0.1 * random.random(), color=color, alpha=0.5)
        ax.add_artist(rect)
    elif shape_type == 'triangle':
        triangle = plt.Polygon(np.random.rand(3, 2), color=color, alpha=0.5)
        ax.add_artist(triangle)

fig, ax = plt.subplots()

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

ax.axis('off')

for _ in range(100):  
    draw_shape(ax)

plt.savefig('abstract_art.pdf', format='pdf')

plt.show()
