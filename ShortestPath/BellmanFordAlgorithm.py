'''Bellman-Ford algorithm'''

def relax(u,v,w,dist,prev):
    if dist[u]+w < dist[v]:
        dist[v] = dist[u]+w
        prev[v] = u
 
def bellmanFord(V,E):
    dist = [float('inf')] * V
    prev = [None] * V
    dist[0] = 0
 
    for i in range(V-1):
        for edge in E:
            relax(edge[0],edge[1],edge[2],dist,prev)
 
    #checks for negative cycles        
    for e in E:
        u = e[0]
        v = e[1]
        w = e[2]
        if dist[u]+w < dist[v]:
            return 1
 
    return 0
 
# edges = []
# edges.append([0, 1, 5])
# edges.append([2, 3, -5])
# edges.append([3, 4, -6])
# edges.append([4, 2, -5])
# edges.append([1, 2, 5])
#  
# print(bellmanFord(5, edges))

edges = []
edges.append([0, 1, 5])
edges.append([2, 3, -5])
edges.append([3, 4, -6])
edges.append([4, 2, -5])
 
print(bellmanFord(5, edges))
