import re
import os
import sys
import numpy as np

import matplotlib.lines as lines
import matplotlib.patches as patches
import matplotlib.text as text
import matplotlib.collections as collections
import matplotlib as mp
import matplotlib.pyplot as plt
from ast import literal_eval as make_tuple

#def create(mapname):
mapname = sys.argv[1]

#read in file from turtlebot_maps/map_1.txt
f = open(os.getcwd() + '/turtlebot_maps/' + mapname)
s = ""
for line in f:
     s += line   

coordinates = s.split('---')

# Create figure and axes
fig,ax = plt.subplots(1)

verts = []
for points in coordinates[0].split(' '):
        boundaries = make_tuple(points)
        verts.append(boundaries)

rect = patches.Rectangle((50,100),40,30,linewidth=1,edgecolor='r',facecolor='none')
