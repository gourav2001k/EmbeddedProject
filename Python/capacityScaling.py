from collections import defaultdict
import math
import time

class CapacityScaling:
    def __init__(self,n,s,t):
        self.n=n # Total Nodes
        self.s=s # Source
        self.t=t # Sink
        self.delta=0 # Hueristic
        self.g=defaultdict(dict)

        ## To be used for finding augmenting paths
        self.visited=[0 for i in range(n)]
        self.visToken=1

        ## Container for answers
        self.solved=False
        self.maxFlow=0

    def addEdge(self,u,v,c):
        # Storing capacity, flow each edge
        if u>=self.n or v>=self.n: 
            raise ValueError("u and v must be less than n(total number of nodes)")
        if c<=0:
            raise ValueError("capacity should be positive")
        if c>self.delta:self.delta=c
        self.g[u][v]=[c,0]
        self.g[v][u]=[0,0]
    
    def augmentEdge(self,u,v,bottleNeck):
        self.g[u][v][1]+=bottleNeck
        self.g[v][u][1]-=bottleNeck

    def solve(self):
        if self.solved:return
        # self.delta=1<<int(math.log2(self.delta))
        while self.delta!=0:
            f=self.dfs(self.s,10**18)
            while f!=0:
                self.maxFlow+=f
                self.visToken+=1
                f=self.dfs(self.s,10**18)
            self.delta>>=1
            
        
        self.solved=True

    def dfs(self,root,flow):
        if root==self.t:return flow
        self.visited[root]=self.visToken
        for child in self.g[root]:
            remCap=self.g[root][child][0]-self.g[root][child][1]
            if self.visited[child]!=self.visToken and remCap>=self.delta:
                bottleNeck=self.dfs(child,min(flow,remCap))
                if bottleNeck>0:
                    self.augmentEdge(root,child,bottleNeck)
                    return bottleNeck
        return 0


if __name__=="__main__":
    n,e=map(int,input().split())
    
    flowGraph=CapacityScaling(n,n-2,n-1)

    for i in range(e):
        u,v,c=map(int,input().split())
        flowGraph.addEdge(u,v,c)
    
    x=time.time()
    flowGraph.solve()
    print("Max Flow     :",flowGraph.maxFlow)
    print("Compute Time : %.3f"%((time.time()-x)*1000),"ms")