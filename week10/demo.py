"""Week 10 Demo — Week 10
Run this file to see demonstrations of the algorithms.
"""

# BFS traversal. graph={node:[neighbors]}, start. Return visited order.
def bfs(graph,start):
    from collections import deque
    visited=[start];queue=deque([start]);seen={start}
    while queue:
        u=queue.popleft()
        for v in graph.get(u,[]):
            if v not in seen: seen.add(v);visited.append(v);queue.append(v)
    return visited

# DFS traversal iterative. graph={node:[neighbors]}, start. Return visited order.
def dfs(graph,start):
    visited=[];stack=[start];seen=set()
    while stack:
        u=stack.pop()
        if u in seen: continue
        seen.add(u);visited.append(u)
        for v in reversed(graph.get(u,[])):
            if v not in seen: stack.append(v)
    return visited

# Bellman-Ford. edges=[(u,v,w)], n, src. Return dist dict or 'NEGATIVE CYCLE'.
def bellman_ford(edges,n,src):
    dist={i:float('inf') for i in range(n)};dist[src]=0
    for _ in range(n-1):
        for u,v,w in edges:
            if dist[u]!=float('inf') and dist[u]+w<dist[v]: dist[v]=dist[u]+w
    for u,v,w in edges:
        if dist[u]!=float('inf') and dist[u]+w<dist[v]: return 'NEGATIVE CYCLE'
    return dist

# Detect cycle in directed graph using DFS coloring. Return bool.
def has_cycle_directed(graph):
    WHITE,GRAY,BLACK=0,1,2
    color={v:WHITE for v in graph}
    def dfs(u):
        color[u]=GRAY
        for v in graph.get(u,[]):
            if color[v]==GRAY: return True
            if color[v]==WHITE and dfs(v): return True
        color[u]=BLACK;return False
    return any(dfs(v) for v in graph if color[v]==WHITE)


def main():
    print("Week 10 Demo")
    print("="*50)
    # Demonstration runs
    print("All functions defined. See starter.py for exercises.")

if __name__ == "__main__":
    main()
