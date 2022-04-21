from collections import defaultdict, deque
import time

class Dinics:
    def __init__(self,n,s,t):
        self.n=n # Total Nodes
        self.s=s # Source
        self.t=t # Sink
        self.g=defaultdict(list)

        ## Container for answers
        self.solved=False
        self.maxFlow=0

    def addEdge(self,u,v,c):
        # Storing capacity, flow each edge
        if u>=self.n or v>=self.n: 
            raise ValueError("u and v must be less than n(total number of nodes)")
        if c<=0:
            raise ValueError("capacity should be positive")
        
        self.g[u].append([v,c,0,len(self.g[v])])
        self.g[v].append([u,0,0,len(self.g[u])-1])
    
    def augmentEdge(self,u,idx,bottleNeck):
        self.g[u][idx][2]+=bottleNeck
        v,idx2=self.g[u][idx][0],self.g[u][idx][3]
        self.g[v][idx2][2]-=bottleNeck

    def solve(self):
        if self.solved:return
        level=[-1 for i in range(self.n)]
        while self.levelGraph(level):
            nxt=[0 for i in range(self.n)]
            f = self.dfs(self.s, nxt,level, 10**18)
            while f!=0:
                self.maxFlow+=f
                f = self.dfs(self.s, nxt,level, 10**18)
            level=[-1 for i in range(self.n)]
        
        self.solved=True

    def levelGraph(self,level):
        q=deque([self.s])
        level[self.s]=0
        while q:
            cur=q.popleft()
            for edge in self.g[cur]:
                remCap=edge[1]-edge[2]
                if remCap>0 and level[edge[0]]==-1:
                    level[edge[0]]=level[cur]+1
                    q.append(edge[0])
        if level[self.t]==-1:return 0
        return 1

    def dfs(self,root,nxt,level,flow):
        if root==self.t:return flow
        l=len(self.g[root])
        s=nxt[root]
        for idx in range(s,l):
            to,cap,crr,idx2=self.g[root][idx]
            if cap-crr>0 and level[to]==level[root]+1:
                bottleNeck=self.dfs(to,nxt,level,min(flow,cap-crr))
                if bottleNeck>0:
                    self.augmentEdge(root,idx,bottleNeck)
                    return bottleNeck
            nxt[root]+=1
        return 0

if __name__=="__main__":
    
    n,e=map(int,input().split())
    
    flowGraph=Dinics(n,n-2,n-1)

    for i in range(e):
        u,v,c=map(int,input().split())
        flowGraph.addEdge(u,v,c)
    
    x=time.time()
    flowGraph.solve()
    print("Max Flow     :",flowGraph.maxFlow)
    print("Compute Time : %.3f"%((time.time()-x)*1000),"ms")