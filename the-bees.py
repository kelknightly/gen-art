# The Bees

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

def draw_honeycomb(ax, center, radius, edge_color, num_rows, num_cols, line_width):
    dx = radius * 3 / 2  
    dy = radius * np.sqrt(3)  

    for i in range(num_cols):
        for j in range(num_rows):
            x = center[0] + i * dx
            y = center[1] + j * dy

            if i % 2 == 1:
                y -= dy / 2

            hexagon = patches.RegularPolygon((x, y), numVertices=6, radius=radius, 
                                             orientation=np.pi / 6, edgecolor=edge_color, 
                                             facecolor='none', lw=line_width)
            ax.add_patch(hexagon)

fig, ax = plt.subplots(figsize=(8, 8))

num_rows = 10
num_cols = 7
radius = 2

ax.set_xlim(-3 * radius, num_cols * 1.5 * radius)
ax.set_ylim(-3 * radius, num_rows * radius * np.sqrt(3) / 2)
ax.axis('off')

soft_yellow = '#ffffe5'  
fig.patch.set_facecolor(soft_yellow)
ax.set_facecolor(soft_yellow)

draw_honeycomb(ax, center=(0, 0), radius=radius, edge_color='pink', num_rows=num_rows, num_cols=num_cols, line_width=2)

# second honeycomb
offset_yellow = (-radius / 2, 0)  
dark_yellow = '#f0e68c'  #
draw_honeycomb(ax, center=offset_yellow, radius=radius, edge_color=dark_yellow, num_rows=num_rows, num_cols=num_cols, line_width=1)

# third honeycomb
offset_gray = (radius / 4, 0) 
gray_color = '#DCDCDC'  
draw_honeycomb(ax, center=offset_gray, radius=radius, edge_color=gray_color, num_rows=num_rows, num_cols=num_cols, line_width=0.5)

plt.show()

