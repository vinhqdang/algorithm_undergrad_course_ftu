"""Week 15 SOLUTION — Do not distribute before deadline."""
import math, heapq, random

# SA for maximising f(x) on interval [a,b]. Return best x found.
def simulated_annealing(f,x0,a,b,T0=100,cool=0.99,iterations=1000):
    import random,math
    x=x0;best_x=x;best_f=f(x);T=T0
    for _ in range(iterations):
        xn=x+(random.random()-0.5)*(b-a)*0.1
        xn=max(a,min(b,xn))
        df=f(xn)-f(x)
        if df>0 or random.random()<math.exp(df/T): x=xn
        if f(x)>best_f: best_f=f(x);best_x=x
        T*=cool
    return best_x

# GA for OneMax (maximise 1-bits in bitstring of length n). Return best fitness.
def genetic_algorithm_onemax(n,pop_size=50,generations=100):
    import random
    pop=[list(random.choices([0,1],k=n)) for _ in range(pop_size)]
    def fitness(ind): return sum(ind)
    for _ in range(generations):
        pop.sort(key=fitness,reverse=True)
        new_pop=pop[:pop_size//2]
        while len(new_pop)<pop_size:
            p1,p2=random.choices(pop[:20],k=2)
            c=random.randint(0,n)
            child=p1[:c]+p2[c:]
            if random.random()<0.1:
                i=random.randint(0,n-1);child[i]=1-child[i]
            new_pop.append(child)
        pop=new_pop
    return max(fitness(ind) for ind in pop)

# Hill climbing for f maximisation. f=callable, x0=start, step=0.1. Return best x found.
def hill_climbing(f,x0,lo=-10,hi=10,step=0.1,iterations=1000):
    x=x0;best=f(x)
    for _ in range(iterations):
        for dx in [-step,step]:
            xn=max(lo,min(hi,x+dx))
            if f(xn)>best: best=f(xn);x=xn;break
    return x

# 1D Particle Swarm Optimisation to minimise f. Return best position.
def particle_swarm_1d(f,lo,hi,n=20,iterations=100):
    import random
    pos=[random.uniform(lo,hi) for _ in range(n)]
    vel=[random.uniform(-1,1) for _ in range(n)]
    pbest=pos[:];gbest=min(pos,key=f)
    w,c1,c2=0.7,1.5,1.5
    for _ in range(iterations):
        for i in range(n):
            r1,r2=random.random(),random.random()
            vel[i]=w*vel[i]+c1*r1*(pbest[i]-pos[i])+c2*r2*(gbest-pos[i])
            pos[i]=max(lo,min(hi,pos[i]+vel[i]))
            if f(pos[i])<f(pbest[i]): pbest[i]=pos[i]
            if f(pos[i])<f(gbest): gbest=pos[i]
    return gbest

if __name__=="__main__": print("Solution loaded.")
