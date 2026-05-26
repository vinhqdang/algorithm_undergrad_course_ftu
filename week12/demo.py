"""Week 12 Demo — Week 12
Run this file to see demonstrations of the algorithms.
"""

# Build KMP failure function (prefix function) for pattern. Return list.
def kmp_failure(pattern):
    n=len(pattern);f=[0]*n;k=0
    for i in range(1,n):
        while k>0 and pattern[k]!=pattern[i]: k=f[k-1]
        if pattern[k]==pattern[i]: k+=1
        f[i]=k
    return f

# KMP pattern matching. Return list of start indices.
def kmp_search(text,pattern):
    if not pattern: return []
    f=kmp_failure(pattern);matches=[];k=0
    for i,c in enumerate(text):
        while k>0 and pattern[k]!=c: k=f[k-1]
        if pattern[k]==c: k+=1
        if k==len(pattern): matches.append(i-k+1);k=f[k-1]
    return matches
def kmp_failure(p):
    n=len(p);f=[0]*n;k=0
    for i in range(1,n):
        while k>0 and p[k]!=p[i]: k=f[k-1]
        if p[k]==p[i]: k+=1
        f[i]=k
    return f

# Rabin-Karp pattern matching using rolling hash. Return list of indices.
def rabin_karp(text,pattern,base=256,mod=101):
    n,m=len(text),len(pattern)
    if m>n: return []
    h=pow(base,m-1,mod)
    ph=th=0
    for i in range(m): ph=(base*ph+ord(pattern[i]))%mod;th=(base*th+ord(text[i]))%mod
    matches=[]
    for i in range(n-m+1):
        if ph==th and text[i:i+m]==pattern: matches.append(i)
        if i<n-m: th=(base*(th-ord(text[i])*h)+ord(text[i+m]))%mod
    return matches

# Ford-Fulkerson max flow. cap=2D capacity list, src,sink. Return max flow.
def ford_fulkerson(cap,src,sink):
    n=len(cap)
    def bfs(s,t,parent):
        visited={s};queue=[s]
        while queue:
            u=queue.pop(0)
            for v in range(n):
                if v not in visited and cap[u][v]>0:
                    visited.add(v);parent[v]=u;queue.append(v)
                    if v==t: return True
        return False
    flow=0
    while True:
        parent=[-1]*n
        if not bfs(src,sink,parent): break
        path_flow=float('inf');s=sink
        while s!=src: u=parent[s];path_flow=min(path_flow,cap[u][s]);s=u
        v=sink
        while v!=src: u=parent[v];cap[u][v]-=path_flow;cap[v][u]+=path_flow;v=u
        flow+=path_flow
    return flow


def main():
    print("Week 12 Demo")
    print("="*50)
    # Demonstration runs
    print("All functions defined. See starter.py for exercises.")

if __name__ == "__main__":
    main()
