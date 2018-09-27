import numpy as np

import math
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib import collections as mc
from a_star import find_path, node

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

    
def main():
    
    teststart = node(-6,-6)
    testgoal = node(-6,-4)
    
    find_path(teststart,testgoal)
    
    print(testgoal.parent.x)
    
    #Add Lines for robot path
    lines = []
    iterator = testgoal
    while iterator.parent != None:
        print("(%d,%d),(%d,%d)"%(iterator.x,iterator.y,iterator.parent.x,iterator.parent.y))
        lines.append([(iterator.x,iterator.y),(iterator.parent.x,iterator.parent.y)])
        iterator=iterator.parent
    
#    for n in neighbors:
#        print("%d, %d" % (n.x,n.y))
#        lines.append([(n.x,n.y),(test.x,test.y)])
    
    #start grid
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
    
    #draw lines to the plot
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