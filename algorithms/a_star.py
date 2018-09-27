from scipy.spatial import distance
import matplotlib as mp
import heapq as hq


#Using straight line distance as heuristic
def heuristic(n, goal):
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
    hq.heappush(fringe, (start,0))
     
    while(fringe):
        #Pop node with the smallest f value from heap
        current = hq.heappop(fringe)
        closed.append(current)
        g_n = current.g

        if current == goal:
                print "Found Goal!"
                return closed
        
        current.get_neighbors()
        
        for neighbor in current.neighbors:
                neighbor.parent = current
                h_n = heuristic(neighbor)

                ###FIX THIS THING
                if is_diagonal(current, neighbor):
                    neighbor.g = g_n + 1.4 
                else:
                    neighbor.g = g_n + 1 
                f_n = h_n + neighbor.g 
                hq.heappush(fringe, (neighbor, f_n))

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
        for a in range(-1,2):
            if self.x+a>=self.minx and self.x+a<=self.maxx:
                for b in range(-1,2):
                    if self.y+b>=self.miny and self.y+b<=self.maxy and (a!=0 or b!=0):
                        self.neighbor.append(node(self.x+a,self.y+b))             
    
    