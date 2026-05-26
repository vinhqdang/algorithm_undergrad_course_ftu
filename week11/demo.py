"""Week 11 Demo — Week 11
Run this file to see demonstrations of the algorithms.
"""

# Topological sort of DAG. graph={node:[neighbors]}. Return sorted list.
def topological_sort(graph):
    visited=set();order=[]
    def dfs(u):
        visited.add(u)
        for v in graph.get(u,[]):
            if v not in visited: dfs(v)
        order.append(u)
    for v in graph:
        if v not in visited: dfs(v)
    return order[::-1]

# Count strongly connected components (Kosaraju's). graph={node:[neighbors]}. Return count.
def count_scc(graph):
    visited=set();order=[]
    def dfs1(u):
        visited.add(u)
        for v in graph.get(u,[]): 
            if v not in visited: dfs1(v)
        order.append(u)
    for u in graph:
        if u not in visited: dfs1(u)
    rev={v:[] for v in graph}
    for u in graph:
        for v in graph[u]: rev[v].append(u)
    visited2=set();count=0
    def dfs2(u):
        visited2.add(u)
        for v in rev.get(u,[]):
            if v not in visited2: dfs2(v)
    for u in reversed(order):
        if u not in visited2: dfs2(u);count+=1
    return count

# Prim MST total weight. graph={node:[(neighbor,weight)]}. Return int.
def prim_mst_weight(graph):
    import heapq
    if not graph: return 0
    s=min(graph);vis={s};heap=[(w,v) for v,w in graph.get(s,[])];heapq.heapify(heap);tot=0
    while heap and len(vis)<len(graph):
        w,u=heapq.heappop(heap)
        if u in vis: continue
        vis.add(u);tot+=w
        for v,nw in graph.get(u,[]):
            if v not in vis: heapq.heappush(heap,(nw,v))
    return tot

# Check if graph is bipartite using BFS 2-coloring. Return bool.
def is_bipartite(graph):
    from collections import deque
    color={}
    for start in graph:
        if start in color: continue
        color[start]=0;q=deque([start])
        while q:
            u=q.popleft()
            for v in graph.get(u,[]):
                if v not in color: color[v]=1-color[u];q.append(v)
                elif color[v]==color[u]: return False
    return True


def main():
    print("Week 11 Demo")
    print("="*50)
    # Demonstration runs
    print("All functions defined. See starter.py for exercises.")

if __name__ == "__main__":
    main()
