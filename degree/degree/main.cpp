#include <iostream>
#include <list>
#include <vector>
#include <fstream>
#include <string>
#include <sstream>


using namespace std;


void get_degree( vector<list<pair<int,int > > >  adj_list , int nodes)
{
    ofstream myfile  ("C:\\Users\\ledar\\PycharmProjects\\data_struc\\2nd project\\dist\\centrality\\output.txt");
    for (int i=0; i<nodes; i++)
    {
        if (myfile.is_open())
        {
            myfile << adj_list[i].size()<<"\n";
        }
    }
    myfile.close();
}


int main()
{
    int nodes,edges;
    int e1,e2,w8;
    string line;
    ifstream myfile ("C:\\Users\\ledar\\PycharmProjects\\data_struc\\2nd project\\dist\\centrality\\input.txt");


    getline (myfile,line);
    istringstream is( line );

    is >> nodes;

    is >> edges;

    vector<list<pair<int,int> > > adj_list(nodes);


    if (myfile.is_open())
    {
    while ( getline (myfile,line) )
    {

        istringstream in( line );

        in >> e1;

        in >> e2;

        in >> w8;

        adj_list[e1].push_back(make_pair(e2,w8));
        adj_list[e2].push_back(make_pair(e1,w8));


    }
    myfile.close();
    }

    get_degree( adj_list, nodes);

    return 0;
}
