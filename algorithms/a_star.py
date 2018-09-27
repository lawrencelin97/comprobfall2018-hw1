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
        closed.push(current)
        g_n = current.g

       if current == goal:
                print "Found Goal!"
                return closed
        
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


    
    