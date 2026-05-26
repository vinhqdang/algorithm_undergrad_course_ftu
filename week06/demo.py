"""Week 6 Demo — Week 6
Run this file to see demonstrations of the algorithms.
"""

# Dijkstra's algorithm. graph={node:[(neighbor,weight)]}, src. Return {node:dist}.
def dijkstra(graph,src):
    import heapq
    dist={v:float('inf') for v in graph};dist[src]=0
    pq=[(0,src)]
    while pq:
        d,u=heapq.heappop(pq)
        if d>dist[u]: continue
        for v,w in graph.get(u,[]):
            nd=dist[u]+w
            if nd<dist[v]: dist[v]=nd;heapq.heappush(pq,(nd,v))
    return dist

# Kruskal MST. edges=[(u,v,w)], n=nodes. Return (edges,total_weight).
def kruskal_mst(edges,n):
    par=list(range(n));rnk=[0]*n
    def find(x):
        while par[x]!=x: par[x]=par[par[x]];x=par[x]
        return x
    def union(a,b):
        ra,rb=find(a),find(b)
        if ra==rb: return False
        if rnk[ra]<rnk[rb]: ra,rb=rb,ra
        par[rb]=ra
        if rnk[ra]==rnk[rb]: rnk[ra]+=1
        return True
    mst=[];tot=0
    for u,v,w in sorted(edges,key=lambda e:e[2]):
        if union(u,v): mst.append((u,v,w));tot+=w
    return mst,tot

# Prim's MST. graph={node:[(neighbor,weight)]}. Return total weight.
def prim_mst(graph):
    import heapq
    if not graph: return 0
    start=min(graph);vis={start};heap=[(w,v) for v,w in graph.get(start,[])];heapq.heapify(heap);tot=0
    while heap and len(vis)<len(graph):
        w,u=heapq.heappop(heap)
        if u in vis: continue
        vis.add(u);tot+=w
        for v,nw in graph.get(u,[]):
            if v not in vis: heapq.heappush(heap,(nw,v))
    return tot

# Bellman-Ford. edges=[(u,v,w)], n=nodes, src. Return dist dict or 'NEGATIVE CYCLE'.
def bellman_ford(edges,n,src):
    dist={i:float('inf') for i in range(n)};dist[src]=0
    for _ in range(n-1):
        for u,v,w in edges:
            if dist[u]+w<dist[v]: dist[v]=dist[u]+w
    for u,v,w in edges:
        if dist[u]+w<dist[v]: return 'NEGATIVE CYCLE'
    return dist


def main():
    print("Week 6 Demo")
    print("="*50)
    # Demonstration runs
    print("All functions defined. See starter.py for exercises.")

if __name__ == "__main__":
    main()
