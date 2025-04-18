import json
import requests
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def LoadJson(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data

data = LoadJson('example_json.json')

fig, ax = plt.subplots()
fig.suptitle('Properties', fontsize=16)

for prop in data:
    boundaries = json.loads(prop['boundaries'])
    coordinates = boundaries['coordinates']
    for coords in coordinates:
        # Flatten if necessary (handle [[[x, y], ...]] and [[x, y], ...])
        if len(coords) > 0 and isinstance(coords[0][0], list):
            # It's a MultiPolygon or a Polygon with holes, take the exterior ring
            coords = coords[0]
        color = 'white'
        # Create the polygon patch
        if(prop['status'] == 'Owned'):
          color = '#b6d7ff'
        if(prop['status'] == 'For sale'):
          color = '#34a400'
        polygon = Polygon(coords, closed=True, edgecolor='black', facecolor=color, linewidth=2)
        ax.add_patch(polygon)

# Optionally, set the plot limits for better view
all_x = []
all_y = []
for prop in data:
    boundaries = json.loads(prop['boundaries'])
    coordinates = boundaries['coordinates']
    for coords in coordinates:
        if len(coords) > 0 and isinstance(coords[0][0], list):
            coords = coords[0]
        for x, y in coords:
            all_x.append(x)
            all_y.append(y)

if all_x and all_y:
    ax.set_xlim(min(all_x)-0.0005, max(all_x)+0.0005)
    ax.set_ylim(min(all_y)-0.0005, max(all_y)+0.0005)

# Hide axis ticks if you want
ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect('equal')

plt.show()



