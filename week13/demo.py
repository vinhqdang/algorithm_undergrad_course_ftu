"""Week 13 Demo — Week 13
Run this file to see demonstrations of the algorithms.
"""

# Compute Z-function of string. z[i]=length of longest substring starting at i that is a prefix.
def z_function(s):
    n=len(s);z=[0]*n;z[0]=n;l=r=0
    for i in range(1,n):
        if i<r: z[i]=min(r-i,z[i-l])
        while i+z[i]<n and s[z[i]]==s[i+z[i]]: z[i]+=1
        if i+z[i]>r: l,r=i,i+z[i]
    return z

# 2-approx vertex cover. graph={node:set_of_neighbors}. Return cover set.
def vertex_cover_approx(graph):
    cover=set();visited_edges=set()
    for u in graph:
        for v in graph[u]:
            e=frozenset([u,v])
            if e not in visited_edges:
                cover.add(u);cover.add(v);visited_edges.add(e)
    return cover

# TSP nearest neighbor heuristic. cities=list of (x,y). Return tour length.
def tsp_nearest_neighbor(cities):
    import math
    if len(cities)<=1: return 0
    def dist(a,b): return math.hypot(a[0]-b[0],a[1]-b[1])
    unvisited=list(range(1,len(cities)));current=0;total=0
    while unvisited:
        nearest=min(unvisited,key=lambda c:dist(cities[current],cities[c]))
        total+=dist(cities[current],cities[nearest]);current=nearest;unvisited.remove(nearest)
    total+=dist(cities[current],cities[0]);return total

# Find all occurrences of pattern in text using Z-algorithm. Return indices.
def string_match_z(text,pattern):
    s=pattern+'$'+text;z=z_function(s);m=len(pattern);matches=[]
    for i in range(m+1,len(s)):
        if z[i]==m: matches.append(i-m-1)
    return matches
def z_function(s):
    n=len(s);z=[0]*n;z[0]=n;l=r=0
    for i in range(1,n):
        if i<r: z[i]=min(r-i,z[i-l])
        while i+z[i]<n and s[z[i]]==s[i+z[i]]: z[i]+=1
        if i+z[i]>r: l,r=i,i+z[i]
    return z


def main():
    print("Week 13 Demo")
    print("="*50)
    # Demonstration runs
    print("All functions defined. See starter.py for exercises.")

if __name__ == "__main__":
    main()
