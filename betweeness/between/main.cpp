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


void dijkstra( vector<vector< list<int> > > &parent,vector< vector<int> > &graph, int src, int nodes)
{
	int dist[nodes];
	bool sptSet[nodes];
    parent[src][src].push_front(-1);
    parent[src][src].push_front(0);

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
            parent[src][i].push_front(u);
			parent[src][i].push_front(dist[i]);
        }

	}

}


void get_pathe(  vector<vector<list<int> > > &parent, int src, int dest, int nodes, int node_serched,int &node_path_count,int &path_count, int dest_flag)
{
    if(dest==src)
    {
        if(src==node_serched)
            node_path_count++;
        return;
    }
        list <int> :: iterator dis;
        list <int> :: iterator min_dis;
        list <int> :: iterator it;

        int new_path=0;
        min_dis = parent[src][dest].begin();
		for (dis = parent[src][dest].begin(); dis != parent[src][dest].end(); advance(dis,2) )
        {

            it=dis;
            it++;
            if(*min_dis==*dis)
            {
                if(dest==node_serched)
                {
                    if(new_path==0)
                        node_path_count++;
                    dest_flag=1;
                }


                if(new_path==1)
                {
                    if (dest_flag==1)
                    {
                        node_path_count++;
                    }
                    path_count++;
                }

                get_pathe( parent, src, *it, nodes,node_serched, node_path_count, path_count,dest_flag);
            }
            new_path=1;
        }
}


int main()
{
    int nodes,edges;
    int e1,e2,w8,pathe_count=1,nodee_count=0;
    int dest_flag=0;
    float betw_cent=-nodes+1;
    string line;

    ifstream myfile  ("C:\\Users\\ledar\\PycharmProjects\\data_struc\\2nd project\\dist\\centrality\\input.txt");
    ofstream myfileo  ("C:\\Users\\ledar\\PycharmProjects\\data_struc\\2nd project\\dist\\centrality\\output.txt");
    getline (myfile,line);
    istringstream is( line );

    is >> nodes;

    is >> edges;

    vector<vector<int> > adj_mat(nodes, vector<int>(nodes));
    vector<vector<list<int> > > parent(nodes, vector< list<int> >(nodes));




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
	dijkstra(parent, adj_mat, i, nodes);

    for(int k=0;k<nodes;k++)
    {
        betw_cent=-nodes+1;

    for(int j=0;j<nodes;j++)
    for(int i=j+1;i<nodes;i++)
    {
    nodee_count=0;
    pathe_count=1;
    dest_flag=0;
    get_pathe(parent, j, i, nodes, k, nodee_count, pathe_count,dest_flag);
    betw_cent=betw_cent+(float(nodee_count)/float(pathe_count));
    }
    if (myfileo.is_open())
    {
        myfileo << betw_cent <<"\n";
    }
    }
    myfileo.close();
}
