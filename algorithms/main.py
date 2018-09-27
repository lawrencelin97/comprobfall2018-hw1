import numpy as np

import math
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib import collections as mc
    
def updateVertex(node1 = None, node2 = None):
    #if line of sight parent of 1 and node 2
    if True:
        if node1.parent.g_val + c_val(node1.parent,node2) < node2.g_val:
            node2.g_val = node1.parent.g_val + c_val(node1.parent,node2)
            node2.parent=node1.parent
            #fringe part
    else:
        print("bye")
    
def c_val(node1, node2):
    difx=node1.x-node2.x
    dify=node1.y-node2.y
    return math.sqrt(difx*difx+dify*dify)

class node():
    g=0
    minx=-7
    maxx=4
    miny=-7
    maxy=4
    scale=1
    neighbor=[]
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        
    def get_neighbor(self):
        for a in range(-1,2):
            if self.x+a>=self.minx and self.x+a<=self.maxx:
                for b in range(-1,2):
                    if self.y+b>=self.miny and self.y+b<=self.maxy and (a!=0 or b!=0):
                        self.neighbor.append(node(self.x+a,self.y+b))             
        return self.neighbor
    
def main():
    
    i=2
    test = node(-7,-7)
    neighbors= test.get_neighbor()
    
    
#    start = node()
#    start.x=-6
#    start.y=-6
#    
#    goal = node()
#    goal.x=-6
#    goal.y=0
  
    fig, ax = plt.subplots()
    
    #Add Obstacles
    patches = []
    patches.append(Polygon([[-1,-1],[-5,-1],[-5,2],[-3,2]]))
    patches.append(Polygon([[-2,2],[2,2],[2,-4]]))
    patches.append(Polygon([[-1,-2.5],[-5,-2.5],[-5,-5],[1.2,-5],[1.2,-4]]))
    for poly in patches:
        ax.add_patch(poly)
    
    #Set boundaries
    ax.set_xlim([-7,4])
    ax.set_ylim([-7,4])

    
    #Set size of plot
    fig_size = plt.rcParams["figure.figsize"]
    fig_size[0] = 12
    fig_size[1] = 9
    plt.rcParams["figure.figsize"] = fig_size

    #Add Lines for robot path
    lines = []
    for n in neighbors:
        print("%d, %d" % (n.x,n.y))
        lines.append([(n.x,n.y),(test.x,test.y)])
        
    lc = mc.LineCollection(lines,linewidths = 2)
    
    ax.add_collection(lc)
    
    #Set up Axis 
    ax.minorticks_on()
    ax.xaxis.set_major_locator(plt.MultipleLocator(1))
    ax.yaxis.set_major_locator(plt.MultipleLocator(1))
    ax.xaxis.set_minor_locator(plt.MultipleLocator(0.25))
    ax.yaxis.set_minor_locator(plt.MultipleLocator(0.25))
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='black')
    ax.grid(which='minor', linestyle='-', linewidth='0.2', color='black')
    
    plt.show()
#
    
    '''plt.axis([-7,4,-7,4])
    polygon = Polygon(5,True)
    plt.plot(polygon)
    plt.show()'''
main()