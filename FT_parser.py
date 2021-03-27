#!/usr/bin/env python3
import re
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import write_dot, graphviz_layout
import sys
import netgraph

f_path = 'FTree.py'


class GenerateFT:
    def __init__(self):
        pass

    def partition_cond(self, ft_list, cond):
        new_list = []
        part_list = []
        for x in ft_list:
            if x in [cond]:
                new_list.append(part_list)
                part_list = []
                continue
            part_list.append(x)
        return new_list

    def add_nodes(self, G, list):
        G.add_nodes_from(list)

    def add_edges(self, G, list):
        edge_list = []
        edge_list = edge_list + ([(list[0], list[1])])
        for x in list[2:]:
            edge_list = edge_list + ([(list[1], x)])
        G.add_edges_from(edge_list)

    def filter_comments(self, txt):
        return [i for i in txt if not re.search('^([#])', i)]

    def gates_regex(self, _file):
        regex = r'([a-zA-Z]+\.((and)|(or))_gate)'
        return [lines for lines in _file if re.search(regex, lines)]

    def strip_gates_param(self, txt):
        frag = []
        for i in txt:
            frag += re.split(r'=|,|\(|\)', i)
        frag = [r.strip() for r in frag]
        frag_t = []
        for r in frag:
            if '[' in r:
                frag_t.append(r.split('[')[-1])
            elif ']' in r:
                frag_t.append(r.split(']')[0])
            else:
                frag_t.append(r)
        return frag_t

    def index_gates(self, nodes):
        nodes_t = []
        index = 1
        for i in nodes:
            if i == "z.and_gate" or i == "z.or_gate":
                nodes_t.append(
                    i.split('.')[-1].split('_')[0] + ' ' + '(G' + str(index) + ')'
                )
                index += 1
            else:
                nodes_t.append(i)
        return nodes_t

    def plot_graph_ft(self, parsed_ft):
        n_size = 320
        G = nx.DiGraph()
        for i in parsed_ft:
            self.add_nodes(G, i)
            self.add_edges(G, i)
        plt.subplot(111)
        # write_dot(G, 'test.dot')

        # same layout using matplotlib with no labels
        plt.title('Fault Tree Diagram')
        pos = graphviz_layout(G, prog='dot')
        nx.draw_networkx(
            G,
            pos=pos,
            with_labels=True,
            # node_size=[len(v) * n_size for v in G.nodes()],
            alpha=0.3,
            arrows=True,
            arrowsize=20,
            width=2,
            bbox=dict(facecolor="skyblue", edgecolor='black', boxstyle='round,pad=0.2'),
        )
        # draw white circles over the lines
        nx.draw_networkx(
            G,
            pos=pos,
            with_labels=True,
            # node_size=[len(v) * n_size for v in G.nodes()],
            alpha=1,
            arrows=True,
            arrowsize=20,
            width=2,
            node_color='w',
            bbox=dict(facecolor="skyblue", edgecolor='black', boxstyle='round,pad=0.2'),
        )
        # draw the nodes as desired
        nx.draw_networkx(
            G,
            pos=pos,
            # node_size=[len(v) * n_size for v in G.nodes()],
            alpha=0.3,
            arrows=True,
            arrowsize=20,
            width=2,
            bbox=dict(facecolor="skyblue", edgecolor='black', boxstyle='round,pad=0.2'),
        )
        nx.draw_networkx_labels(G, pos=pos)
        plt.axis("off")
        plt.show()

    def print_FT(self, file_path):
        with open(file_path) as file:
            gates_search = self.gates_regex(file)
            # clean the data extracted from program file
            clean_ft = self.filter_comments(gates_search)
            ft_frag = self.strip_gates_param(clean_ft)
            print(ft_frag)
            ft_frag = self.index_gates(ft_frag)
            print(ft_frag)
            part_ft = self.partition_cond(ft_frag, '')
            self.plot_graph_ft(part_ft)


if __name__ == "__main__":
    gen_ft = GenerateFT()
    gen_ft.print_FT(f_path)
