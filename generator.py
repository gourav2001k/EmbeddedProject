from random import randint

def main():
    n=randint(15,25) # Number of intermediate nodes
    e=randint(50,(n*(n+1))//4) # Nuumber of edges
    deg=[[0,0]for i in range(n)] # Storing degree of nodes
    edges=dict()
    idx=0
    while idx<e:
        a=randint(0,n-1)
        b=randint(0,n-1)
        while b==a:
            b=randint(0,n-1)
        c=randint(1,n*(n+1))
        if (a,b) not in edges:
            deg[a][1]+=1
            deg[b][0]+=1
            edges[(a,b)]=c
            idx+=1
        

    source=randint(3,10)
    idx=n
    while idx<source+n:
        edges[(source+n,idx)]=randint(1,n*(n+1))
        for j in range(randint(3,10)):
            v=randint(0,n-1)
            if (idx,v) not in edges:
                edges[(idx,v)]=randint(1,n*(n+1))
        ## Ading Sink nodes
        u=randint(0,n-1)
        if (u,n+source+1) not in edges:
            edges[(u,n+source+1)]=randint(1,n*(n+1))
        idx+=1
    
    for i in range(n):
        if not deg[i][0]:
            edges[(n+source,i)]=randint(1,n*(n+1))
        if not deg[i][1]:
            edges[(i,n+source+1)]=randint(1,n*(n+1))
    
    print(n+2+source,len(edges))
    for a,b in  edges:
        print(a,b,edges[(a,b)])


if __name__=="__main__":
    main()
