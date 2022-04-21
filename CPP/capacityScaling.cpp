#include <bits/stdc++.h>
#include <chrono>

using namespace std;
using namespace std::chrono;

void importGraph(vector<vector<pair<int, int>>> &adj, int &n, int &s, int &t) {
	ifstream infile("../input.txt");
	int e;
	int u, v, cap;
	infile >> n >> e;
	adj = vector<vector<pair<int, int>>> (n);
	while(infile >> u >> v >> cap) {
		//cout << u << ' ' << v  << " " << cap << "\n";
		adj[u].push_back({v, cap});
	}
	s = n-2;
	t = n-1;
}

void constructGraph(vector<vector<pair<int, int>>> &adj, int n, int s, int t) {
	adj = vector<vector<pair<int, int>>> (n);
	
	// Edges from source
	adj[s].push_back({0, 10});
	adj[s].push_back({1, 5});
	adj[s].push_back({2, 10});

	// Middle Edges
	adj[0].push_back({3, 10});
	adj[1].push_back({2, 10});
	adj[2].push_back({5, 15});
	adj[3].push_back({1, 2});
	adj[3].push_back({6, 15});
	adj[4].push_back({1, 15});
	adj[4].push_back({3, 3});
	adj[5].push_back({4, 4});
	adj[5].push_back({8, 10});
	adj[6].push_back({7, 10});
	adj[7].push_back({4, 10});
	adj[7].push_back({5, 7});

	// Edges to sink
	adj[6].push_back({t, 15});
	adj[8].push_back({t, 10});
}

bool DFS(vector<vector<int>> &graph, vector<int> &parent, vector<bool> &visited, int n, int node, int t, int delta) {
	if (node == t) return true;
	visited[node] = true;

	for(int u = 0; u < n; u++) {
		if (graph[node][u] >= delta && !visited[u]) {
			parent[u] = node;
			if (DFS(graph, parent, visited, n, u, t, delta))
				return true;
		}
	}
	return false;
}

int CapacityScaling(vector<vector<pair<int, int>>> &adj, int n, int s, int t) {
	vector<vector<int>> rGraph(n, vector<int> (n, 0));
//	vector<vector<pair<int, int>>> rGraph = adj;
	vector<int> parent(n);
	vector<bool> visited(n);

	// Construct Adjacency matrix
	int max_capacity = 0;
	for(int u = 0; u < n; u++) {
		for(auto p : adj[u]) {
			rGraph[u][p.first] = p.second;
			max_capacity = max(max_capacity, p.second);
		}
	}

	int max_flow = 0;
	int delta = (1 << (int)log2(max_capacity));

	for(; delta > 0; delta /= 2) {
		while(DFS(rGraph, parent, visited, n, s, t, delta)) {
			fill(visited.begin(), visited.end(), false);
			int path_flow = 0xfffffff;

			for(int v = t; v != s; v = parent[v]) {
				int u = parent[v];
				path_flow = min(path_flow, rGraph[u][v]);
			}

			for(int v = t; v != s; v = parent[v]) {
				int u = parent[v];
				rGraph[u][v] -= path_flow;
				rGraph[v][u] += path_flow;
			}

			max_flow += path_flow;
		}
	}
	
	return max_flow;
}

int main(){
	int n = 12;
	int s = n-2;
	int t = n-1;

	// Edge from i_th node to j_th node with cap = c_{ij} where adj[i] = {j, c_{ij}}
	vector<vector<pair<int, int>>> adj;	

	//constructGraph(adj, n, s, t);
	importGraph(adj, n, s, t);
	// Max Flow of this graph
	auto start = steady_clock::now();
	int max_flow = CapacityScaling(adj, n, s, t);
	auto stop = steady_clock::now();
	auto dur = duration<double, milli>(stop - start);
	cout << "Max Flow: " << max_flow << "\n";
	cout << "Compute Time: " << dur.count() << " ms\n";
	return 0;
}
