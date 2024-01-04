# noumenon

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

def draw_dyson_sphere(ax, center, num_rings, max_radius, solid_line_color, dashed_line_color, dash_length):
    for i in range(num_rings):
        radius = (i + 1) * max_radius / num_rings
        if i % 2 == 0:  # Dashed lines for alternate rings
            linestyle = (0, (dash_length, dash_length))  
            color = dashed_line_color
            line_weight = 0.5  
        else:  
            linestyle = 'solid'
            color = solid_line_color
            line_weight = 2  

        circle = patches.Circle(center, radius, fill=False, linestyle=linestyle, 
                                edgecolor=color, lw=line_weight)
        ax.add_patch(circle)


solid_line_color = '#46827F'  
dashed_line_color = '#A0A0A0'  
background_color = '#0B3D91'   
star_color = '#FFD55A'         
dash_length = 10  

fig, ax = plt.subplots(figsize=(10, 10))
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.axis('off')

fig.patch.set_facecolor(background_color)
ax.set_facecolor(background_color)

star = patches.Circle((0, 0), 0.05, color=star_color, zorder=1)
ax.add_patch(star)

num_rings = 10
max_radius = 1
draw_dyson_sphere(ax, (0, 0), num_rings, max_radius, solid_line_color, dashed_line_color, dash_length)

plt.show()