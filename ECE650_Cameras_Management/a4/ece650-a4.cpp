#include <vector>
#include <memory>
#include <string>
#include <sstream>
#include <algorithm> // for std::sort
#include <iostream>		// for std::cout
#include "minisat/core/Solver.h"
#include "minisat/core/SolverTypes.h"


using namespace std;
using Minisat::mkLit;
using Minisat::lbool;

class Graph {
private:
	int numV;	// No. of vertices
	vector<int>* adj;	// Pointer to an array with adjacency lists

public:
	Graph(int val) {
		this->numV = val + 1;
		adj = new vector<int>[numV];
	}
	void setVertices(int val);
	bool addEdge(int src, int dest);	// Add an edge from vertex v to w
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
	this->numV = val + 1;
	adj = new vector<int>[numV];
}

bool Graph::addEdge(int src, int dest) {
	try {
		if (src == dest) {
			// throw "Error: Invalid Edge Input - Self-loop Occurs";
			throw " ";
		}
		if (src > (numV - 1) || dest > (numV - 1)) {
			// throw "Error: Invalid Edge Input - No Such Vertex";
			throw " ";
		}
		else
		{
			for (int vertex : adj[src]) {
				if (vertex == dest) {	// Because we focus on undirected edges
					// throw "Error: Invalid Edge Input - Repeated Edges";
					throw " ";
				}
			}
			adj[src].push_back(dest);
			adj[dest].push_back(src);
			return 1;
		}
	}
	catch (const char* msg) {
		// throw msg;
		cout << msg << endl;
		return 0;
	}

}

// m is the number of vertices, and k is the size of the vertex cover

vector<int> getVertexCover(int n, int k, vector<int> edges){
    unique_ptr<Minisat::Solver> solver(new Minisat::Solver());
    vector<vector<Minisat::Lit>> mat(n);    // X[n,k]

    // create positive literals
    for (int i = 0; i<n; i++){
        for (int j=0; j<k; j++){
            Minisat::Lit l = Minisat::mkLit(solver->newVar());
            mat[i].push_back(l);
        }
    }

    // Convert Vertex Cover Problem to SAT
    // 1. At least one vertex is the ith vertex in the vertex cover
    for (int i=0; i<k; i++){
        Minisat::vec<Minisat::Lit> literals;
        for (int j=0; j<n; j++){
            literals.push(mat[j][i]);
        }
        solver->addClause(literals);
        literals.clear();
    }

    // 2. No one vertex can appear twice in a vertex cover
    for (int m=0; m<n; m++){
        for (int p=0; p<k-1; p++){
            for (int q=p+1; q<k; q++){
                solver->addClause(~mat[m][p], ~mat[m][q]);
            }
        }
    }

    // 3. No more than one vertex appears in the mth position of the vertex cover
    for (int m=0; m<k; m++){
        for (int p=0; p<n-1; p++){
            for (int q=p+1; q<n; q++){
                solver->addClause(~mat[p][m], ~mat[q][m]);
            }
        }
    }

    // 4. Every edge is incident to at least one vertex in the vertex cover
	for (vector<int>::size_type i=0; i<edges.size(); i+=2){
		Minisat::vec<Minisat::Lit> literals;
		for (int j=0; j<k; j++){
			literals.push(mat[edges[i]-1][j]);	// we need to minus 1 here!!! Because our input's index is starting from 1, not 0
			literals.push(mat[edges[i+1]-1][j]);
		}
		solver->addClause(literals);
		literals.clear(); //for next edges
	}

    bool isSatisfied = solver->solve();
    // cout << "The result is: " << isSatisfied << endl;

    if (isSatisfied){   // meaning there is a safisfied assignment
        vector<int> res;    // Store for the vertices in the resulted vertex cover list
        for (int i=0; i<n; i++){
            for (int j=0; j<k; j++){
                if (Minisat::toInt(solver->modelValue(mat[i][j]) == Minisat::l_True)){  
                    res.push_back(i+1);  // We find a vertex in vertex cover list, but we need to add 1 here, because our input's index starting from 1 not 0
                }
            }
        }
        return res;
    } 
    return {-1};
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
	
	vector<int> tempRes;	// We need to use binary search to find the best k - minimum vertex cover 
	vector<int> finalRes;
	vector<int> noSAT = {-1};

	input >> spec;

	try
	{
		if (spec == "V") {
			input >> numVertices;
			if (numVertices == 0){
				// Accept it
				;
			}
			else if (numVertices <= 1) {
				// throw "Error: Invalid Vertex Input";
				throw " ";
			}
		}
		else if (spec == "E")
		{
			g.setVertices(numVertices);
			char delimiter = ',';
			string num;
			vector<int> nums;
			input >> edges;

			string::iterator iter;

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
						// throw "Error: Invalid Vertex Input - Do not accept vertex with index 0";
						throw " ";
					}
					nums.push_back(stoi(num));
				}
				catch(exception const&){
					// throw "Error: Invalid Edge Input - No Path exists";
					throw " ";
				}
			}

			if (nums.size() % 2 == 0) {
				// Actually, it is not necessary to addEdge because it will not influence the result
				// But addEdge() can be used to examine whether the edges meet requirements
				bool flag = 1;
				for (vector<int>::size_type v = 0; v < nums.size(); v+=2) {
					src = nums[v];
					dest = (nums[v + 1]);
					flag = g.addEdge(src, dest);
					if (!flag){	// flag == 0
						break;
					}
				}
				if (flag){
					int left = 0;
					int right = numVertices;

					while (left <= right){
						int mid = floor((left + right) / 2);

						tempRes = getVertexCover(numVertices, mid, nums);

						if (tempRes == noSAT){	// NOT FOUND - need to increase k
							left = mid + 1;

						} else{	// FOUND - try to decrease k to find optimized k
							right = mid - 1;
							finalRes = tempRes;
						}
					}
					sort(finalRes.begin(), finalRes.end());
					for (vector<int>::size_type i=0; i<finalRes.size(); i++){
						cout << finalRes[i] << " ";
					}
					cout << endl;	
				}
			}
			else {
				// throw "Error: Invalid Edge Input";
				throw " ";
			}
		}
		else if (spec == ""){
			;
		}
		else
		{
			// throw "Error: Invalid Command Input :(";
			throw " ";
		}
	}
	catch (const char* msg) {
		// throw msg;
		cout << msg << endl;
	}
}


int main(int argc, char **argv) {
    while(!cin.eof()){
        string line;
        getline(cin, line);
        inputParse(line);
    }
}


// Tests
// V 5
// E {<1,5>,<5,2>,<1,4>,<4,5>,<4,3>,<2,4>}

// V 12
// E {<1,5>,<2,8>,<2,4>,<11,5>,<4,7>,<4,3>,<12,5>,<6,2>,<7,3>,<10,12>}

// V 5
// E {<1,2>,<2,3>,<2,4>,<2,5>,<4,5>,<4,3>,<1,5>}

// V 4
// E {<1,2>,<2,3>,<2,4>,<4,3>}

// V 8
// E {<1,2>,<2,3>,<2,4>,<4,3>,<4,7>,<2,8>}

// V 9
// E {<6,2>,<1,3>,<2,4>,<4,3>,<4,7>,<2,8>}

