#include <bits/stdc++.h>
#include <chrono>

using namespace std;
using namespace std::chrono;

struct FlowEdge {
    int v, u;
    long long cap, flow = 0;
    FlowEdge(int v, int u, long long cap) : v(v), u(u), cap(cap) {}
};

struct Dinic {
    const long long flow_inf = 1e18;
    vector<FlowEdge> edges;
    vector<vector<int>> adj;
    int n, m = 0;
    int s, t;
    vector<int> level, ptr;
    queue<int> q;

    Dinic(int n, int s, int t) : n(n), s(s), t(t) {
        adj.resize(n);
        level.resize(n);
        ptr.resize(n);
    }

    void add_edge(int v, int u, long long cap) {
        edges.emplace_back(v, u, cap);
        edges.emplace_back(u, v, 0);
        adj[v].push_back(m);
        adj[u].push_back(m + 1);
        m += 2;
    }

    bool bfs() {
        while (!q.empty()) {
            int v = q.front();
            q.pop();
            for (int id : adj[v]) {
                if (edges[id].cap - edges[id].flow < 1)
                    continue;
                if (level[edges[id].u] != -1)
                    continue;
                level[edges[id].u] = level[v] + 1;
                q.push(edges[id].u);
            }
        }
        return level[t] != -1;
    }
long long dfs(int v, long long pushed) {
        if (pushed == 0)
            return 0;
        if (v == t)
            return pushed;
        for (int& cid = ptr[v]; cid < (int)adj[v].size(); cid++) {
            int id = adj[v][cid];
            int u = edges[id].u;
            if (level[v] + 1 != level[u] || edges[id].cap - edges[id].flow < 1)
                continue;
            long long tr = dfs(u, min(pushed, edges[id].cap - edges[id].flow));
            if (tr == 0)
                continue;
            edges[id].flow += tr;
            edges[id ^ 1].flow -= tr;
            return tr;
        }
        return 0;
    }

    long long flow() {
        long long f = 0;
        while (true) {
            fill(level.begin(), level.end(), -1);
            level[s] = 0;
            q.push(s);
            if (!bfs())
                break;
            fill(ptr.begin(), ptr.end(), 0);
            while (long long pushed = dfs(s, flow_inf)) {
                f += pushed;
            }
        }
        return f;
    }
};


Dinic importGraph(int &n, int &s, int &t) {
	ifstream infile("../input.txt");
	int e;
	int u, v, cap;
	infile >> n >> e;

	s = n-2;
	t = n-1;
	Dinic graph(n, s, t);


	while(infile >> u >> v >> cap) {
		//cout << u << ' ' << v  << " " << cap << "\n";
		graph.add_edge(u, v, cap);
	}
	return graph;
}

void constructGraph(Dinic &graph, int n, int s, int t) {
	
	// Edges from source
	graph.add_edge(s, 0, 10);
	graph.add_edge(s, 1, 5);
	graph.add_edge(s, 2, 10);

	// Middle Edges
	graph.add_edge(0, 3, 10);
	graph.add_edge(1, 2, 10);
	graph.add_edge(2, 5, 15);
	graph.add_edge(3, 1, 2);
	graph.add_edge(3, 6, 15);
	graph.add_edge(4, 1, 15);
	graph.add_edge(4, 3, 3);
	graph.add_edge(5, 4, 4);
	graph.add_edge(5, 8, 10);
	graph.add_edge(6, 7, 10);
	graph.add_edge(7, 4, 10);
	graph.add_edge(7, 5, 7);

	// Edges to sink
	graph.add_edge(6, t, 15);
	graph.add_edge(8, t, 10);
}

int main(){
	int n = 12;
	int s = n-2;
	int t = n-1;

	// Edge from i_th node to j_th node with cap = c_{ij} where adj[i] = {j, c_{ij}}
	vector<vector<pair<int, int>>> adj;	

	// Max Flow of this graph
	// constructGraph(dinic_flow_graph, n, s, t);
	Dinic dinic_flow_graph = importGraph(n, s, t);
	auto start = steady_clock::now();

	int max_flow = dinic_flow_graph.flow();

	auto stop = steady_clock::now();
	auto dur = duration<double, milli>(stop - start);

	cout << "Max Flow: " << max_flow << "\n";
	cout << "Compute Time: " << dur.count() << " ms\n";
	return 0;
}
