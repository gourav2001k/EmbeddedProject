import graphviz
import os

f = graphviz.Digraph('Graph', filename='fsm.gv', node_attr={'color': 'lightblue2', 'style': 'filled'})

with open('input.txt', 'r') as fp:
    lines = fp.readlines()
    n, e = [int(i) for i in lines[0].split(' ')]
    s = n-2
    t = n-1
    f.attr(rankdir='LR', size='8,5')

    f.attr('node', shape='doublecircle')
    f.node("Source", style='filled', fillcolor='#40e0d0')
    f.node("Sink", style='filled', fillcolor='#ff000042')

    f.attr('node', shape='circle')
    for i in range(1, len(lines)):
        u, v, cap = [int(x) for x in lines[i].split(' ')]
        u = "Source" if (u == s) else u
        v = "Source" if (v == s) else v
        u = "Sink" if (u == t) else u
        v = "Sink" if (v == t) else v
        f.edge(str(u), str(v), label=str(cap))

f.view()
