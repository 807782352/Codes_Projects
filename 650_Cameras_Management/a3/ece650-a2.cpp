// Compile with c++ ece650-a2.cpp -std=c++11 -o ece650-a2
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <queue>

using namespace std;

class Graph {
private:
	int numV;	// No. of vertices
	vector<int>* adj;	// Pointer to an array with adjacency lists

public:
	Graph(int val) {
		numV = val + 1;
		adj = new vector<int>[numV];
	}
	void setVertices(int val);
	void addEdge(int src, int dest);	// Add an edge from vertex v to w
	bool BFS(int src, int dest, int* predecessor);	// Check whether there is a short distance between src and dest
	void printShortestPath(int src, int dest);
	void clear();
	bool isAdjEmpty();
};

bool Graph::isAdjEmpty() {
	// cout << "true or false" << (*adj).empty() << endl;
	return (*adj).empty();
}

void Graph::clear() {
	adj->clear();
	setVertices(0);
}

void Graph::setVertices(int val) {
	numV = val + 1;
	adj = new vector<int>[numV];
}

void Graph::addEdge(int src, int dest) {
	try {
		if (src == dest) {
			throw "Error: Invalid Edge Input - Self-loop Occurs";
		}
		if (src > (numV - 1) || dest > (numV - 1)) {
			throw "Error: Invalid Edge Input - No Such Vertex";
		}
		else
		{
			for (int vertex : adj[src]) {
				if (vertex == dest) {	// Because we focus on undirected edges
					throw "Error: Invalid Edge Input - Repeated Edges";
				}
			}
			adj[src].push_back(dest);
			adj[dest].push_back(src);
		}


	}
	catch (const char* msg) {
		// throw msg;
		cout << msg << endl;
	}

}

bool Graph::BFS(int src, int dest, int* predecessor) {
	bool *isVisited = new bool[numV];
	for (int i = 0; i < numV; i++) {
		isVisited[i] = false;
		predecessor[i] = -1;
	}

	queue<int> myqueue;
	isVisited[src] = true;
	myqueue.push(src);

	while (!myqueue.empty()) {
		int cur = myqueue.front();
		myqueue.pop();
		for (vector<int>::size_type i = 0; i < adj[cur].size(); i++) {
			int curAdjVertex = adj[cur][i];
			if (!isVisited[curAdjVertex]) {	// meaning NOT visited
				isVisited[curAdjVertex] = true;
				myqueue.push(curAdjVertex);
				predecessor[curAdjVertex] = cur;
				if (curAdjVertex == dest) {
					delete[] isVisited;
					return true;
				}
			}
		}
	}
	delete[] isVisited;
	return false;
}

void Graph::printShortestPath(int src, int dest) {
	int *predecessor = new int[numV];

	if (!BFS(src, dest, predecessor)) {
		delete[] predecessor;
		cout << "Error: There is no path between these two vertices\n";
		return;
	}

	vector<int> shortPath;
	int temp = dest;
	while (temp != -1) {	// shortPath get the path form dest to src, so we need to print path inversely
		shortPath.push_back(temp);
		temp = predecessor[temp];
	}

	delete[] predecessor;

	string str = "";
	for (int i = shortPath.size()-1; i >= 0; i--) {
		str += to_string(shortPath[i]);
		if (i == 0) {
			str += "\n";
		}
		else {
			str += "-";
		}
	}
	cout << str;
}

Graph g(0);
int numVertices;

void inputParse(string line) {
	istringstream input(line);
	//unsigned nums;
	string spec;
	string edges;
	string vertex;
	int src;
	int dest;

	input >> spec;

	try
	{
		if (spec == "V") {
			cout << line << endl;
			input >> numVertices;
			if (numVertices == 0){
				// Accept it
				;
			}
			else if (numVertices <= 1) {
				throw "Error: Invalid Vertex Input";
			}
		}
		else if (spec == "E")
		{
			//if (!g.isAdjEmpty()) {
			//	g.clear();
			//}
			cout << line << endl;
			g.setVertices(numVertices);
			char delimiter = ',';
			string num;
			vector<int> nums;
			input >> edges;

			string::iterator iter;
			if (edges.back() != '}') {
				throw "Error: Invalid Edge Input";
			}

			for (iter = edges.begin(); iter != edges.end();) {
				if (*iter == '{') {
					edges.erase(iter);
				}
				if (*iter == '<') {
					edges.erase(iter);
				}
				if (*iter == '>') {
					edges.erase(iter);
				}
				if (*iter == '}') {
					*iter = ' ';
				}
				else
				{
					++iter;
				}
			}

			istringstream iss(edges);
			while (getline(iss, num, delimiter)) {
				try {
					if (stoi(num) == 0) {
						throw "Error: Invalid Vertex Input - Do not accept vertex with index 0";
					}
					nums.push_back(stoi(num));
				}
				catch(exception const&){
					throw "Error: Invalid Edge Input - No Path exists";
				}
			}

			if (nums.size() % 2 == 0) {
				for (vector<int>::size_type v = 0; v < nums.size(); v+=2) {
					src = nums[v];
					dest = nums[v + 1];
					g.addEdge(src, dest);
				}
			}
			else {
				throw "Error: Invalid Edge Input";
			}
		}
		else if (spec == "s"){
			input >> vertex;

			try{
				if (stoi(vertex) > numVertices) {
					throw "Error: Invalid Vertex Input - no such path";
				} else if(stoi(vertex) < 0){
					throw "Error: Invalid Vertex Input - no vertex index lower than 0";
				}
				src = stoi(vertex);

				input >> vertex;
				if (stoi(vertex) > numVertices) {
					throw "Error: Invalid Vertex Input - no such path";
				}else if(stoi(vertex) < 0){
					throw "Error: Invalid Vertex Input - no vertex index lower than 0";
				}
				dest = stoi(vertex);
				g.printShortestPath(src, dest);
			}catch(exception const&){
				throw "Error: Invalid s Command";
			}
		}
		else if (spec == ""){
			;
		}
		else
		{
			throw "Error: Invalid Command Input :(";
		}
	}
	catch (const char* msg) {
		// throw msg;
		cout << msg << endl;
	}
}

int main(int argc, char** argv) {
	while (!cin.eof()) {
		string line;
		getline(cin, line);
		inputParse(line);
	}
	return 0;
}
