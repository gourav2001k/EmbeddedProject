from collections import defaultdict,deque
import time

class EdmodsKarp:
    def __init__(self,n,s,t):
        self.n=n # Total Nodes
        self.s=s # Source
        self.t=t # Sink
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
        
        self.g[u][v]=[c,0]
        self.g[v][u]=[0,0]
    
    def augmentEdge(self,u,v,bottleNeck):
        self.g[u][v][1]+=bottleNeck
        self.g[v][u][1]-=bottleNeck

    def solve(self):
        if self.solved:return
        
        f=self.bfs()
        while f!=0:
            self.maxFlow+=f
            self.visToken+=1
            f=self.bfs()
        
        self.solved=True

    def bfs(self):
        prev=dict()
        q=deque([self.s])
        self.visited[self.s]=self.visToken
        while q:
            cur=q.popleft()
            if cur==self.t:break
            for child in self.g[cur]:
                remCap=self.g[cur][child][0]-self.g[cur][child][1]
                if remCap>0 and self.visited[child]!=self.visToken:
                    prev[child]=cur
                    self.visited[child]=self.visToken
                    q.append(child)
        
        if self.t not in prev:return 0
        bottleNeck=10**18
        e=self.t
        while e in prev:
            bottleNeck=min(bottleNeck,self.g[prev[e]][e][0]-self.g[prev[e]][e][1])
            e=prev[e]
        
        e=self.t
        while e in prev:
            self.augmentEdge(prev[e],e,bottleNeck)
            e=prev[e]

        return bottleNeck


if __name__=="__main__":
    n,e=map(int,input().split())
    
    flowGraph=EdmodsKarp(n,n-2,n-1)

    for i in range(e):
        u,v,c=map(int,input().split())
        flowGraph.addEdge(u,v,c)
    
    x=time.time()
    flowGraph.solve()
    print("Max Flow     :",flowGraph.maxFlow)
    print("Compute Time : %.3f"%((time.time()-x)*1000),"ms")