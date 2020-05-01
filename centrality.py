import os
import sys
import time
import plotly.graph_objs as go
import networkx as nx
from plotly.offline import download_plotlyjs, init_notebook_mode, plot


from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
from os import path


FORM_CLASS,_= loadUiType(path.join(path.dirname(__file__),"GUI.ui"))

def main():
   app = QApplication(sys.argv)
   window = mainapp()
   window.show()
   app.exec()

class mainapp(QMainWindow,FORM_CLASS):

    def __init__(self,parent=None):
        super(mainapp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_UI()
        self.draw.clicked.connect(self.handle_graph)


    def Handle_UI (self):
       self.setWindowTitle("Centrality grapher")
       self.setFixedSize(700,900)

    def handle_graph(self):

        my_graph = self.graph.toPlainText()
        f = open("input.txt", "w")
        f.write(my_graph)
        f.close()
        if self.degree.isChecked():
            self.handle_degree()
        if self.close.isChecked():
            self.handle_close()
        if self.between.isChecked():
            self.handle_between()



    def handle_degree(self):

        os.startfile("C:/Users/ledar/PycharmProjects/data_struc/2nd project/degree/degree/bin/Debug/degree.exe")
        time.sleep(0.5)


        my_graph = open("input.txt")

        file = my_graph.read()

        lines = file.split("\n")

        num = lines[0].split()

        my_edges = []

        for x in range(1, int(num[1]) + 1):
            words = lines[x].split()
            my_edges.append((int(words[0]), int(words[1])))

        G = nx.random_geometric_graph(int(num[0]), 0)
        pos = nx.get_node_attributes(G, 'pos')
        dmin = 1
        ncenter = 0
        for n in pos:
            x, y = pos[n]
            d = (x - 0.5) ** 2 + (y - 0.5) ** 2
            if d < dmin:
                ncenter = n
                dmin = d

        p = nx.single_source_shortest_path_length(G, ncenter)

        edge_trace = go.Scatter(
            x=[],
            y=[],
            line=dict(width=1.5, color='#231'),
            hoverinfo='none',
            mode='lines')

        for edge in my_edges:
            x0, y0 = G.node[edge[0]]['pos']
            x1, y1 = G.node[edge[1]]['pos']

            edge_trace['x'] += tuple([x0, x1, None])
            edge_trace['y'] += tuple([y0, y1, None])

        node_trace = go.Scatter(
            x=[],
            y=[],
            text=[],
            textfont=dict(
                family='sans serif',
                size=25,
            ),
            hovertext=[],
            mode='markers+text',
            hoverinfo='text',
            marker=dict(
                showscale=True,
                # colorscale options
                # 'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
                # 'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
                # 'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
                colorscale='YlGnBu',
                reversescale=True,
                color=[],
                size=[],
                colorbar=dict(
                    thickness=15,
                    title='Node Connections',
                    xanchor='left',
                    titleside='right'
                ),
                line=dict(width=2)))

        for node in G.nodes():
            x, y = G.node[node]['pos']
            node_trace['x'] += tuple([x])
            node_trace['y'] += tuple([y])

        output = open("output.txt")
        file2 = output.read()
        lines2 = file2.split("\n")

        for x in range (len(lines2)-1) :
            node_trace['marker']['color'] += tuple([int(lines2[x])])
            node_info = ' degree = ' + (lines2[x])
            node_trace['marker']['size'] += tuple([int(lines2[x]) * (100 / int(num[0])) + 20])
            node_trace['hovertext'] += tuple([node_info])
            node_text =  str(x)
            node_trace['text'] += tuple([node_text])


        fig = go.Figure(data=[edge_trace, node_trace],
                        layout=go.Layout(
                            title='<br>Network graph made with Python',
                            titlefont=dict(size=16),
                            showlegend=False,
                            hovermode='closest',
                            margin=dict(b=20, l=5, r=5, t=40),
                            annotations=[dict(
                                text="Python code: <a href='https://plot.ly/ipython-notebooks/network-graphs/'> https://plot.ly/ipython-notebooks/network-graphs/</a>",
                                showarrow=False,
                                xref="paper", yref="paper",
                                x=0.005, y=-0.002)],
                            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)))

        plot(fig, filename='networkx.html')



    def handle_close(self):

        os.startfile("C:/Users/ledar/PycharmProjects/data_struc/2nd project/clossness/closness/bin/Debug/closness.exe")

        time.sleep(1)
        my_graph = open("input.txt")

        file = my_graph.read()

        lines = file.split("\n")

        num = lines[0].split()

        my_edges = []

        for x in range(1, int(num[1]) + 1):
            words = lines[x].split()
            my_edges.append((int(words[0]), int(words[1])))

        G = nx.random_geometric_graph(int(num[0]), 0)
        pos = nx.get_node_attributes(G, 'pos')
        dmin = 1
        ncenter = 0
        for n in pos:
            x, y = pos[n]
            d = (x - 0.5) ** 2 + (y - 0.5) ** 2
            if d < dmin:
                ncenter = n
                dmin = d

        p = nx.single_source_shortest_path_length(G, ncenter)

        edge_trace = go.Scatter(
            x=[],
            y=[],
            line=dict(width=1.5, color='#231'),
            hoverinfo='none',
            mode='lines')

        for edge in my_edges:
            x0, y0 = G.node[edge[0]]['pos']
            x1, y1 = G.node[edge[1]]['pos']

            edge_trace['x'] += tuple([x0, x1, None])
            edge_trace['y'] += tuple([y0, y1, None])

        node_trace = go.Scatter(
            x=[],
            y=[],
            text=[],
            textfont=dict(
                family='sans serif',
                size=25,
            ),
            hovertext=[],
            mode='markers+text',
            hoverinfo='text',
            marker=dict(
                showscale=True,
                # colorscale options
                # 'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
                # 'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
                # 'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
                colorscale='YlGnBu',
                reversescale=True,
                color=[],
                size=[],
                colorbar=dict(
                    thickness=15,
                    title='Node Connections',
                    xanchor='left',
                    titleside='right'
                ),
                line=dict(width=2)))

        for node in G.nodes():
            x, y = G.node[node]['pos']
            node_trace['x'] += tuple([x])
            node_trace['y'] += tuple([y])

        output = open("output.txt")
        file2 = output.read()
        lines2 = file2.split("\n")

        for x in range (len(lines2)-1) :
            node_trace['marker']['color'] += tuple([float(lines2[x])])
            node_info =  ' clossness = ' + (lines2[x])
            node_trace['marker']['size'] += tuple([float(lines2[x]) * (400) + 20]  )
            node_trace['hovertext'] += tuple([node_info])
            node_text =  str(x)
            node_trace['text'] += tuple([node_text])


        fig = go.Figure(data=[edge_trace, node_trace],
                        layout=go.Layout(
                            title='<br>Network graph made with Python',
                            titlefont=dict(size=16),
                            showlegend=False,
                            hovermode='closest',
                            margin=dict(b=20, l=5, r=5, t=40),
                            annotations=[dict(
                                text="Python code: <a href='https://plot.ly/ipython-notebooks/network-graphs/'> https://plot.ly/ipython-notebooks/network-graphs/</a>",
                                showarrow=False,
                                xref="paper", yref="paper",
                                x=0.005, y=-0.002)],
                            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)))

        plot(fig, filename='Network.html')



    def handle_between(self):

        os.startfile("C:/Users/ledar/PycharmProjects/data_struc/2nd project/betweeness/between/bin/Debug/between.exe")

        time.sleep(1.5)
        my_graph = open("input.txt")

        file = my_graph.read()

        lines = file.split("\n")

        num = lines[0].split()

        my_edges = []

        for x in range(1, int(num[1]) + 1):
            words = lines[x].split()
            my_edges.append((int(words[0]), int(words[1])))

        G = nx.random_geometric_graph(int(num[0]), 0)
        pos = nx.get_node_attributes(G, 'pos')
        dmin = 1
        ncenter = 0
        for n in pos:
            x, y = pos[n]
            d = (x - 0.5) ** 2 + (y - 0.5) ** 2
            if d < dmin:
                ncenter = n
                dmin = d

        p = nx.single_source_shortest_path_length(G, ncenter)

        edge_trace = go.Scatter(
            x=[],
            y=[],
            line=dict(width=1.5, color='#231'),
            hoverinfo='none',
            mode='lines')

        for edge in my_edges:
            x0, y0 = G.node[edge[0]]['pos']
            x1, y1 = G.node[edge[1]]['pos']

            edge_trace['x'] += tuple([x0, x1, None])
            edge_trace['y'] += tuple([y0, y1, None])

        node_trace = go.Scatter(
            x=[],
            y=[],
            text=[],
            textfont=dict(
                family='sans serif',
                size=25,
            ),
            hovertext=[],
            mode='markers+text',
            hoverinfo='text',
            marker=dict(
                showscale=True,
                # colorscale options
                # 'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
                # 'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
                # 'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
                colorscale='YlGnBu',
                reversescale=True,
                color=[],
                size=[],
                colorbar=dict(
                    thickness=15,
                    title='Node Connections',
                    xanchor='left',
                    titleside='right'
                ),
                line=dict(width=2)))

        for node in G.nodes():
            x, y = G.node[node]['pos']
            node_trace['x'] += tuple([x])
            node_trace['y'] += tuple([y])

        output = open("output.txt")
        file2 = output.read()
        lines2 = file2.split("\n")

        for x in range (len(lines2)-1) :
            node_trace['marker']['color'] += tuple([float(lines2[x])])
            node_info =' betweenness = ' + (lines2[x])
            node_trace['marker']['size'] += tuple([float(lines2[x]) * (10) + 30]  )
            node_trace['hovertext'] += tuple([node_info])
            node_text =  str(x)
            node_trace['text'] += tuple([node_text])

        fig = go.Figure(data=[edge_trace, node_trace],
                        layout=go.Layout(
                            title='<br>Network graph made with Python',
                            titlefont=dict(size=16),
                            showlegend=False,
                            hovermode='closest',
                            margin=dict(b=20, l=5, r=5, t=40),
                            annotations=[dict(
                                text="Python code: <a href='https://plot.ly/ipython-notebooks/network-graphs/'> https://plot.ly/ipython-notebooks/network-graphs/</a>",
                                showarrow=False,
                                xref="paper", yref="paper",
                                x=0.005, y=-0.002)],
                            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)))

        plot(fig, filename='networkx.html')





if __name__ == '__main__':
   main()
