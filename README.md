# Scifi Generative Art
The Python generative art scripts in this repo revolves around a few of my favourite science fiction books, creating abstract representations of quotes and objects described by the authors. The repo also includes a few more general scripts that are just for dabbling and testing.

## Current booklist

- Dragon's Egg by Robert L. Forward: [dragons-egg.py](https://github.com/kelknightly/gen-art/blob/master/dragons-egg.py) and [dragons-egg.png](https://github.com/kelknightly/gen-art/blob/master/dragons-egg.png)
- Noumenon by Marina J. Lostetter: [noumenon.py](https://github.com/kelknightly/gen-art/blob/master/noumenon.py) and [noumenon.png](https://github.com/kelknightly/gen-art/blob/master/noumenon.png)
- Rendezvous with Rama by Arthur C. Clarke: [rendezvous-with-rama.py](https://github.com/kelknightly/gen-art/blob/master/rendezvous-with-rama.py) and [rendezvous-with-rama.png](https://github.com/kelknightly/gen-art/blob/master/rendezvous-with-rama.png)
- The Bees by Laline Paull: [the-bees.py](https://github.com/kelknightly/gen-art/blob/master/the-bees.py) and [the-bees.png](https://github.com/kelknightly/gen-art/blob/master/the-bees.png)

### Dragon's Egg by Robert L. Forward
[dragons-egg.py](https://github.com/kelknightly/gen-art/blob/master/dragons-egg.py)
[dragons-egg.png](https://github.com/kelknightly/gen-art/blob/master/dragons-egg.png)

"Dragon's Egg," published in 1980, is a masterclass in hard science fiction by Robert L. Forward. Set in the 21st century, the novel explores the extraordinary life and civilization of the Cheela, intelligent creatures living on the surface of a neutron star named Dragon's Egg. In this environment of extreme gravity and harsh conditions, the Cheela evolve at a rapid pace, experiencing thousands of years of development within mere hours of human time.

[This artwork](https://github.com/kelknightly/gen-art/blob/master/dragons-egg.png) represents the [Cheela](https://aliens.fandom.com/wiki/Cheela). Their bodies are based on nuclear structures and they have 12 eyes. The average member of the species has a flat elliptical body about five millimeters in diameter and half a millimeter high. Because of their evolution on the surface of a neuetron star, they are only able to travel East to West along magnetic lines. 

#### Challenges
##### Cheela Body
The script uses randomness to generate unique shapes and positions for the Cheela's body and eyes. Managing this randomness was tricky. I used the uniform function in the random module to generate a random floating-point number from within a range. The selection is uniform, meaning that each value in the specified range has an equal probability of being chosen. 
The patches.Ellipse class is part of the matplotlib.patches module and is used to create the ellipse shape for the Cheela body.

##### Cheela Eyes
The next challenge was to generate 12 eyes for the Cheela. The script iterates 12 times ('range(12)') to create 12 eyes. For each eye, it randomly determines the eye's position ('eye_x', eye_y') around the center of the Cheela's body ('x, y'). The random.uniform() calls generate random values within the bounds of the Cheela's body dimensions to ensure that eyes are placed within or on the edge of the body. The size of each eye is set to 10% ('0.1') of the smaller of the body's width or height ('min(width, height) * 0.1'). Each eye is then created as a yellow circle ('patches.Circle') and added to the plot ('ax.add_patch(eye)'). And voila, Cheela eyes on a Cheela body.

##### Placing Cheela on Magnetic Lines
Once the grey horizontal dotted lines were created to represent the magnetic lines, the final challenge was to pin the Cheela to those dotted lines to represent their movement patterns.  First, 'np.linspace(-80, 80, 3)' generates three evenly spaced y-coordinates betwween -80 and 80. For each of these y-cordinates ('y_line'), a horizontal line (magnetic field line) is drawn on the plot. Then, in the second 'for' loop, the code iterates over these three y-coordinates. For each y-coordinate, it randomly generates two x-coordinates within the range -80 to 80. At each of these (x, y) positions, a Cheela is drawn by calling 'draw_cheela(ax, (x, y), size)', where 'size' is also randomly determined for each Cheela, resulting in two Cheelse being placed on each magnetic field line. 

### Noumenon by Marina J. Lostetter
[noumenon.py](https://github.com/kelknightly/gen-art/blob/master/noumenon.py)
[noumenon.png](https://github.com/kelknightly/gen-art/blob/master/noumenon.png)

"Noumenon" revolves around a deep-space mission to investigate an anomalous star, proposed by astrophysicist Reggie Straifer. This ambitious journey spans aeons and is undertaken by clones to maintain the genetic talent of the original crew. As generations pass, each clone exhibits unique quirks and neuroses, highlighting the complexities of cloning and the evolution of society aboard the fleet. A significant element of the story involves the construction of a Dyson Sphere, a colossal structure envisioned to harness the energy of a star.

[This artwork](https://github.com/kelknightly/gen-art/blob/master/noumenon.png) represents the Dyson Sphere structure, with the star at the centre and expanding rings of solar cells (grey dotted lines) and rings made from advanced materials to withstand extreme temperatures and radiation (blue solid lines) that may also possibly include facilities for maintenance, habitation, and systems for transmitting energy back to where it's needed.

#### Challenges
##### Solar Cells
For every even-indexed ring in the loop (checked using 'i % 2 == 0'), the 'linestyle' is set to a custom dash pattern '(0, (dash_length, dash_length))'. This pattern creates a dotted line, where 'dash_length' determines the length of both dashes and gaps. Solid circles are created for odd-indexed rings by setting 'linestyle' to 'solid', creating an alternating pattern between dotted and solid lines. 
I admit I'm not fully satisfied with this solution. It lacks the three-dimensionality and complexity of a Dyson Sphere. I do feel it is a suitable abstract representation but it just lacks panache. 
##### Sun
The script creates the sun at the center using the 'patches.Circle' function from Matplotlib's 'matplotlib.patches' module. It defines a small circle with a specified radius (0.05 in this case), color ('star_color'), and position (centered at coordinates (0,0)). This circle is then added to the plot ('ax.add_patch(star)'). The 'zorder' parameter is set to 1 to ensure the star is layered above the Dyson Sphere rings in the visualization. 

### Rendezvous with Rama by Arthur C. Clarke
[rendezvous-with-rama.py](https://github.com/kelknightly/gen-art/blob/master/rendezvous-with-rama.py)
[rendezvous-with-rama.png](https://github.com/kelknightly/gen-art/blob/master/rendezvous-with-rama.png)

"Rendezvous with Rama" centers around the discovery of an alien starship entering the Solar System. The story is set in the 22nd century when a group of human explorers, members of the space survey vessel Endeavour, are sent to investigate the mysterious cylindrical object named Rama. Upon arrival, they discover that Rama is a hollow, artificial world with its own internal landscape and ecosystem. As they explore this enigmatic, rotating vessel, they encounter various technological wonders and mysteries, revealing no signs of its creators. The novel focuses on the exploration and the sense of wonder at the unknown, culminating in the realization that Rama is a probe sent through space by an advanced alien civilization, leaving the humans with more questions than answers as it exits the Solar System.

[This artwork](https://github.com/kelknightly/gen-art/blob/master/rendezvous-with-rama.png) represents the Rama landscape, whcih is divided by Cylindrical Seas (represented by the blue circle) and has a narrow strip of land featuring mysterious structures including strange geometric buildings (represented by the green rectangular shapes). Inhabiting Rama are a variety of robotic creatures known as "biots" (represented by the small grey circles). These biots appear to be tasked with maintaining the ship and its internal environment. They vary in shape and function, some resembling terrestrial animals and others utterly alien in design. 

#### Challenges
##### Biots
The 'draw_biot' function randomly generates coordinates (x, y) within a specified range (-100 to 100), and a random radius between 1 and 3 units, simulating the biots' smaller size. Each biot is represented as a circle, drawn using 'plt.Circle', with a color in shades of great ('grey_shade'). These circles are then addeed to the plot using 'ax.add_patch(circle)'. The script randomly places 50 biots across the plot, creating an abstract representation of biots scattered in the Rama environment.
##### Landscape
Technically, the Rama landscape is divided lengthwise into three sections by two Cylindrical Seas, which are vast bodies of liquid stretching along the ship's axis. The Central Plain is a narrow strip of land between these two seas and the building structures are towering spires. This tripped me up and trying to recreate these elements resulted in a hot mess, so I decided to use a single blue circle to represent the water and green to represent the building structures and to forgo the rest. I may revisit this one at a later date.

### The Bees by Laline Paull
[the-bees.py](https://github.com/kelknightly/gen-art/blob/master/the-bees.py)
[the-bees.png](https://github.com/kelknightly/gen-art/blob/master/the-bees.png)

"The Bees" offers a glimpse into the complex and hierarchical world of a beehive through the eyes of a worker bee named Flora 717. Born into the lowest class of her society, Flora is different from her kin – larger, more curious, and with an ability to speak, which is unusual for her kind. The story follows Flora's journey as she breaks the rigid boundaries of her caste system, taking on various roles within the hive, from nursery to foraging, and even ventures into the dangerous outside world. 
[This artwork](https://github.com/kelknightly/gen-art/blob/master/the-bees.png) is an abstract visual representation of a quote from the book:

> "From their place in the Drones' Arrival Hall, all the sanitation workers could hear the massed choirs of the hive singing through the carved walls. As the vocal vibrations sent the fragrance of the Queen's Love shimmering through the membrane of the honeycomb and deep into their bodies, some of the floras made incoherent sounds of happiness, while others made rhythmic movements as if they were trying to dance. Flora was one of the many who stood transfixed by the blissful sense of being loved - until the divine surge began to ebb away."

#### Challenges
##### Honeycomb
Creating the honeycomb shape was easily the biggest challenge of all of these scripts. It was extremely difficult to create hexagons without overlapping edges or hexagons that weren't standalone shapes floating on the canvas with gaps between them. This was resolved by adjusting the distance calculations (dx and dy) to perfectly align the hexagons so their sides touch with gaps or overlaps. The calculation is based on the hexagon's radius and trigonometric properties to make them fit together seamlessly. The horizontal distance between hexagon centers (dx) is computed as 'radius * 3 / 2', and the vertical distance (dy) as 'radius * np.sqrt(3)', which are derived from t he geometric properties of hexagons. The code iterates over rows and columns, placing hexagons at calculated (x, y) positions. Every other column is vertically shifted by 'dy / 2' to align the hexagons. I hated this and nearly picked a different book. 



