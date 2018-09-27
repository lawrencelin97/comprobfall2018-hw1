import numpy as np

import math

from scipy.spatial import distance
import matplotlib as mp
import heapq as hq


#Using straight line distance as heuristic
def heuristic(n, goal):
#    print ("(%d,%d)(%d,%d)" % (n.x,n.y,goal.x,goal.y))
    dx = abs(n.x - goal.x)
    dy = abs(n.y - goal.y)
    h_n = dx + dy
    return h_n 

######################
# A* implementation  # 
######################
def find_path(start, goal):
    fringe = [] #Nodes we are considering expanding
    closed = [] #Nodes we have visited
    start.g = 0 #Starting node has g value = 0
    
    #Put start in the fringe with f value = 0:
    hq.heappush(fringe, (0,start))
    last_tuple=None
    current_tuple=None
    
    while(fringe):
        #Pop node with the smallest f value from heap
        if current_tuple != None:
            last_tuple=current_tuple
        
        current_tuple = hq.heappop(fringe)
        print ("(%d,%d)" % (current_tuple[1].x,current_tuple[1].y))
        
        if last_tuple != None:
            current_tuple[1].parent = last_tuple[1]
            
        test=current_tuple[1]
        while test != None:
            print ("(%d,%d)" % (test.x,test.y))
            test = test.parent
            
        closed.append(current_tuple[1])
        g_n = current_tuple[1].g
        
#        print ("(%d,%d)" % (current_tuple[1].x,current_tuple[1].y))
#        print ("(%d,%d)" % (goal.x,goal.y))
        
        if current_tuple[1].x == goal.x and current_tuple[1].y == goal.y:
                print "Found Goal!"
                goal.parent=current_tuple[1].parent
                return closed
        
        current_tuple[1].get_neighbors()
        
        for neighbor in current_tuple[1].neighbors:
#                neighbor.parent = current_tuple[1]
                h_n = heuristic(neighbor,goal)
                print ("(%d,%d)" % (neighbor.x,neighbor.y))
                ###FIX THIS THING
#                if is_diagonal(current_tuple[1], neighbor):
#                    neighbor.g = g_n + 1.4 
#                else:
#                    neighbor.g = g_n + 1 
                difx=neighbor.x-current_tuple[1].x
                dify=neighbor.y-current_tuple[1].y
                neighbor.g = g_n + np.sqrt(math.pow(difx,2)+math.pow(dify,2))
                
                f_n = h_n + neighbor.g 
                hq.heappush(fringe, (f_n,neighbor))

    return "No path found"

class node():
    g=0
    minx=-7
    maxx=4
    miny=-7
    maxy=4
    scale=1
    parent = None
    neighbors=[]
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        
    def get_neighbors(self):
        print ("(%d,%d)" % (self.x,self.y))
        for a in range(-1,2):
            if self.x+a>=self.minx and self.x+a<=self.maxx:
                for b in range(-1,2):
                    if self.y+b>=self.miny and self.y+b<=self.maxy and (a!=0 or b!=0):
                        self.neighbors.append(node(self.x+a,self.y+b))             
    
    