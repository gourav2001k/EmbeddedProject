# Folder Stucture

```
📦Project
 ┣ 📂Python
 ┃ ┣ 📜capacityScaling.py
 ┃ ┣ 📜dinics.py
 ┃ ┣ 📜edmondsKarp.py
 ┃ ┗ 📜fordFulkerson.py
 ┣ 📂CPP
 ┃ ┣ 📜capacityScaling.cpp
 ┃ ┣ 📜dinics.cpp
 ┃ ┣ 📜edmondsKarp.cpp
 ┃ ┗ 📜fordFulkerson.cpp
 ┣ 📜README.md
 ┣ 📜generator.py
 ┣ 📜input.txt
 ┗ 📜visualiser.py
```

# Steps to Run the Code

-   Generate Input graph:  
    `python generator.py > input.txt`
-   Visualize the graph:  
    `python visualiser.py`
-   To test a Python code:  
    `python Python/<variant>.py < input.txt`
-   To test a CPP code:  
    `g++ CPP/<variant>.cpp -o <variant>; ./<variant> < input.txt`

    (Here \<variant\> should be replaced with the one's listed above)

# Input Format

The graph has $n$ nodes numbered $0$ to $n-1$

$n-2$ represents source and $n-1$ represents sink

The first line contains $n$,$e$ representing total number of nodes and number of edges in the graph

Following next $e$ lines contains $u$,$v$,$c$ representing a directed edge from $u$ to $v$ with a capacity $c$

# Output Format

    Max Flow     : Value
    Compute Time : time

## Sample Input

```
4 6
0 1 5
2 0 4
0 3 8
1 3 7
2 1 3
0 1 6
```

## Sample Output

```
Max Flow     : 7
Compute Time : 0.347 ms
```
