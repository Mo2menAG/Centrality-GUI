#include <iostream>
#include <list>
#include <vector>
#include <fstream>
#include <string>
#include <sstream>


using namespace std;



int minDistance(int dist[], bool sptSet[], int nodes)
{
int min = INT_MAX, min_index;
for (int i = 0; i < nodes; i++)
	if (sptSet[i] == false && dist[i] <= min)
		min = dist[i], min_index = i;

return min_index;
}

void dijkstra(vector< vector<int> > &graph, int src, int nodes, float &closness,int i)
{
	int dist[nodes];
	bool sptSet[nodes];
	int sum=0;

	for (int i = 0; i < nodes; i++)
		dist[i] = INT_MAX, sptSet[i] = false;

	dist[src] = 0;

	for (int count = 0; count < nodes-1; count++)
	{
	int u = minDistance(dist, sptSet, nodes);

	sptSet[u] = true;
	for (int i = 0; i < nodes; i++)
		if (!sptSet[i] && graph[u][i] &&  dist[u]+graph[u][i] <= dist[i])
        {
            dist[i] = dist[u] + graph[u][i];
        }
	}
    for (int i = 0; i < nodes; i++)
    {
        sum=sum+dist[i];
    }
    closness = (float(nodes-1)/float(sum));


}




int main()
{
    int nodes,edges;
    int e1,e2,w8;
    string line;
    float closnes;


    ifstream myfile  ("C:\\Users\\ledar\\PycharmProjects\\data_struc\\2nd project\\dist\\centrality\\input.txt");
    ofstream myfileo  ("C:\\Users\\ledar\\PycharmProjects\\data_struc\\2nd project\\dist\\centrality\\output.txt");


    getline (myfile,line);
    istringstream is( line );

    is >> nodes;

    is >> edges;

    vector<vector<int> > adj_mat(nodes, vector<int>(nodes));


    if (myfile.is_open())
    {
    while ( getline (myfile,line) )
    {

        istringstream in( line );

        in >> e1;

        in >> e2;

        in >> w8;

        adj_mat[e1][e2]=w8;
        adj_mat[e2][e1]=w8;


    }
    myfile.close();
    }



    for(int i=0;i<nodes;i++)
    {
        if (myfileo.is_open())
            {
            dijkstra( adj_mat, i, nodes, closnes, i);
            myfileo << closnes <<"\n";
            }

    }
    myfileo.close();




}
